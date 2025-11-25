#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ingesta de un GeoJSON de países a ClickHouse (compatible con Natural Earth).

Tabla destino: indicadores.latinobarometro_geo
Columnas:
- iso3            String
- nombre          String
- feature_id      Nullable(String)
- geom_json       String          (GeoJSON de geometry, como texto)
- feature         String          (GeoJSON Feature completo listo para Superset)
- bbox            Array(Float64)  [minLon, minLat, maxLon, maxLat]
- centroid_lon    Float64
- centroid_lat    Float64
...
"""


import os
import sys
import json
import time
from datetime import datetime
from typing import Any, Dict, List, Tuple, Optional

from clickhouse_driver import Client, errors

# ========= Parámetros =========
MAX_RETRIES  = int(os.getenv('MAX_RETRIES', 12))
RETRY_DELAY  = int(os.getenv('RETRY_DELAY', 10))  # segundos

CH_HOST      = os.getenv('CH_HOST','clickhouse_server')
CH_PORT      = int(os.getenv('CH_PORT',9000))
CH_USER      = os.getenv('CH_USER','admin')
CH_PASSWORD  = os.getenv('CH_PASSWORD','secret_pw')
CH_DATABASE  = os.getenv('CH_DATABASE','indicadores')

# Usa tu archivo GeoJSON filtrado
GEOJSON_FILE = os.getenv('GEOJSON_FILE','/data/diccionario/latinobarometro_geo.geojson')

TAB_GEO      = 'latinobarometro_geo'

# ========= Utils =========
def log(msg: str):
    ts = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{ts} UTC] {msg}", flush=True)

def get_ch_client():
    last_err = None
    for i in range(MAX_RETRIES):
        try:
            client = Client(
                host=CH_HOST, port=CH_PORT, user=CH_USER, password=CH_PASSWORD, database=CH_DATABASE
            )
            client.execute('SELECT 1')
            log("[OK] Conectado a ClickHouse")
            return client
        except errors.Error as e:
            last_err = e
            log(f"[WARN] Intento {i+1}/{MAX_RETRIES} fallido: {e}")
            time.sleep(RETRY_DELAY)
    raise RuntimeError(f"No pude conectar a ClickHouse: {last_err}")

def ensure_database(client: Client, db: str):
    client.execute(f"CREATE DATABASE IF NOT EXISTS {db}")
    client.execute(f"USE {db}")

def recreate_table_geo(client: Client, db: str):
    client.execute(f"DROP TABLE IF EXISTS {db}.{TAB_GEO}")
    client.execute(f"""
        CREATE TABLE {db}.{TAB_GEO} (
            iso3         String,
            nombre       String,
            feature_id   Nullable(String),
            geom_json    String,
            feature      String,
            bbox         Array(Float64),   -- [minLon, minLat, maxLon, maxLat]
            centroid_lon Float64,
            centroid_lat Float64
        )
        ENGINE = MergeTree
        ORDER BY (iso3)
    """)
    log(f"[OK] Tabla {db}.{TAB_GEO} recreada.")


# ---------- helpers para geometría sin dependencias externas ----------
def _iter_coords(geom: Dict[str, Any]):
    """Itera todos los pares (lon, lat) en la geometría GeoJSON (Point, MultiPoint,
    LineString, MultiLineString, Polygon, MultiPolygon)."""
    gtype = geom.get("type")
    coords = geom.get("coordinates")
    if not gtype or coords is None:
        return
    if gtype == "Point":
        yield tuple(coords)
    elif gtype in ("MultiPoint", "LineString"):
        for c in coords:
            yield tuple(c)
    elif gtype in ("MultiLineString", "Polygon"):
        for part in coords:
            for c in part:
                yield tuple(c)
    elif gtype == "MultiPolygon":
        for poly in coords:
            for ring in poly:
                for c in ring:
                    yield tuple(c)
    elif gtype == "GeometryCollection":
        for g in geom.get("geometries", []):
            yield from _iter_coords(g)

def compute_bbox(geom: Dict[str, Any]) -> Optional[Tuple[float, float, float, float]]:
    """Devuelve (minLon, minLat, maxLon, maxLat) o None si no hay coords."""
    minx = miny = float('inf')
    maxx = maxy = float('-inf')
    found = False
    for lon, lat in _iter_coords(geom):
        if lon is None or lat is None:
            continue
        found = True
        if lon < minx: minx = lon
        if lat < miny: miny = lat
        if lon > maxx: maxx = lon
        if lat > maxy: maxy = lat
    if not found:
        return None
    return (minx, miny, maxx, maxy)

def pick_name(props: Dict[str, Any]) -> str:
    """Elige un nombre legible del feature (Natural Earth prioriza ADMIN/NAME_LONG/NAME)."""
    for k in ("ADMIN", "NAME_LONG", "NAME", "admin", "name"):
        v = props.get(k)
        if isinstance(v, str) and v.strip():
            return v.strip()
    # fallback
    for k in ("SOVEREIGNT", "sovereignt"):
        v = props.get(k)
        if isinstance(v, str) and v.strip():
            return v.strip()
    return props.get("ISO_A3") or props.get("iso_a3") or "Desconocido"

def pick_iso3(props: Dict[str, Any]) -> Optional[str]:
    """Intenta sacar ISO3 del feature."""
    for k in ("ISO_A3", "iso_a3", "ADM0_A3", "adm0_a3", "iso3"):
        v = props.get(k)
        if isinstance(v, str) and len(v.strip()) == 3:
            return v.strip().upper()
    return None

# ========= Ingesta =========
def ingest_geojson(client: Client, db: str, geojson_path: str):
    """Ingiere un GeoJSON de países en ClickHouse.

    - Soporta Polygon y MultiPolygon.
    - MultiPolygon se explota en varios Polygon (una fila por polígono).
    - Además de geom_json (geometry), se guarda un GeoJSON Feature completo en la columna `feature`.
    """
    log(f"[GEO] Leyendo GeoJSON: {geojson_path}")
    try:
        with open(geojson_path, 'r', encoding='utf-8') as f:
            gj = json.load(f)
    except Exception as e:
        log(f"[ERROR] No se pudo leer {geojson_path}: {e}")
        raise

    if gj.get("type") != "FeatureCollection":
        raise RuntimeError("[GEO] El archivo no es un FeatureCollection válido.")

    features = gj.get("features", [])
    if not isinstance(features, list) or not features:
        raise RuntimeError("[GEO] El archivo no contiene 'features' válidos.")

    rows: List[Tuple[Any, ...]] = []
    total = len(features)
    sin_geom = 0
    sin_iso3 = 0
    multi_exploded = 0

    for feat in features:
        if not isinstance(feat, dict) or feat.get("type") != "Feature":
            continue

        props = feat.get("properties", {}) or {}
        geom  = feat.get("geometry")
        if geom is None:
            sin_geom += 1
            continue

        gtype = geom.get("type")
        coords = geom.get("coordinates")

        iso3 = pick_iso3(props)
        if not iso3:
            sin_iso3 += 1
            continue

        nombre = pick_name(props)
        feature_id = feat.get("id")

        # ---- Caso MultiPolygon: explotar en varios Polygon ----
        if gtype == "MultiPolygon" and isinstance(coords, list):
            for idx, poly_coords in enumerate(coords):
                poly_geom = {
                    "type": "Polygon",
                    "coordinates": poly_coords,
                }

                bb = compute_bbox(poly_geom)
                if bb is None:
                    sin_geom += 1
                    continue

                minx, miny, maxx, maxy = bb
                centroid_lon = (minx + maxx) / 2.0
                centroid_lat = (miny + maxy) / 2.0

                geom_json = json.dumps(poly_geom, ensure_ascii=False)

                feature_obj = {
                    "type": "Feature",
                    "geometry": poly_geom,
                    "properties": {
                        "ISO_A3": iso3,
                        "ADMIN": nombre,
                    },
                }
                feature_json = json.dumps(feature_obj, ensure_ascii=False)

                sub_id = f"{feature_id}_{idx}" if feature_id is not None else None

                rows.append((
                    iso3,
                    nombre,
                    sub_id,
                    geom_json,
                    feature_json,
                    [minx, miny, maxx, maxy],
                    float(centroid_lon),
                    float(centroid_lat),
                ))
                multi_exploded += 1

        # ---- Resto de geometrías (Polygon, etc.) ----
        else:
            fbbox = feat.get("bbox")
            if isinstance(fbbox, list) and len(fbbox) == 4:
                minx, miny, maxx, maxy = map(float, fbbox)
            else:
                bb = compute_bbox(geom)
                if bb is None:
                    sin_geom += 1
                    continue
                minx, miny, maxx, maxy = bb

            centroid_lon = (minx + maxx) / 2.0
            centroid_lat = (miny + maxy) / 2.0

            geom_json = json.dumps(geom, ensure_ascii=False)

            feature_obj = {
                "type": "Feature",
                "geometry": geom,
                "properties": {
                    "ISO_A3": iso3,
                    "ADMIN": nombre,
                },
            }
            feature_json = json.dumps(feature_obj, ensure_ascii=False)

            rows.append((
                iso3,
                nombre,
                feature_id,
                geom_json,
                feature_json,
                [minx, miny, maxx, maxy],
                float(centroid_lon),
                float(centroid_lat),
            ))

    log(f"[GEO] Features en archivo: {total} | sin geometría: {sin_geom} | sin ISO3: {sin_iso3} | MultiPolygon explotados: {multi_exploded}")
    if not rows:
        log("[GEO] No hay filas para insertar (¿no había features con ISO3?).")
        return

    log(f"[GEO] Insertando {len(rows)} filas en {db}.{TAB_GEO} ...")
    client.execute(
        f"""
        INSERT INTO {db}.{TAB_GEO}
        (iso3, nombre, feature_id, geom_json, feature, bbox, centroid_lon, centroid_lat)
        VALUES
        """,
        rows,
    )
    log("[GEO] Inserción completada.")

# ========= Main =========
def main():
    client = get_ch_client()
    ensure_database(client, CH_DATABASE)
    recreate_table_geo(client, CH_DATABASE)
    ingest_geojson(client, CH_DATABASE, GEOJSON_FILE)
    log("Proceso completado.")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        log(f"[FATAL] {e}")
        sys.exit(1)
