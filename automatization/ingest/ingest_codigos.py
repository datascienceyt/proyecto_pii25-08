#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ingesta directa de tres CSVs:
- Diccionario de provincias/parroquias
- Líneas de pobreza
- SBU (Salario Básico Unificado) por periodo

Antes de insertar, DROPEA y CREA las tablas para evitar duplicados.

Variables de entorno relevantes (con defaults):
- CH_HOST, CH_PORT, CH_USER, CH_PASSWORD
- CH_DATABASE (default: "indicadores")

- CODIGOS_FILE (default: "/data/diccionario/codigos_parroquiales.csv")
- POVERTY_FILE (default: "/data/diccionario/poverty_lines.csv")
- SBU_FILE     (default: "/data/diccionario/salario_basico_unificado.csv")
"""
import os
import sys
import time
import pandas as pd
from clickhouse_driver import Client, errors
from datetime import datetime

# ========= Parámetros =========
MAX_RETRIES     = int(os.getenv('MAX_RETRIES', 12))
RETRY_DELAY     = int(os.getenv('RETRY_DELAY', 10))  # segundos

CH_HOST         = os.getenv('CH_HOST','clickhouse_server')
CH_PORT         = int(os.getenv('CH_PORT',9000))
CH_USER         = os.getenv('CH_USER','admin')
CH_PASSWORD     = os.getenv('CH_PASSWORD','secret_pw')
CH_DATABASE     = os.getenv('CH_DATABASE','indicadores')

# Archivos de entrada (rutas específicas)
CODIGOS_FILE    = os.getenv('CODIGOS_FILE','/data/diccionario/codigos_parroquiales.csv')
POVERTY_FILE    = os.getenv('POVERTY_FILE','/data/diccionario/poverty_lines.csv')
SBU_FILE        = os.getenv('SBU_FILE','/data/diccionario/salario_basico_unificado.csv')

# Tablas
TAB_PROV = 'diccionario_provincias'
TAB_POV  = 'poverty_lines'
TAB_SBU  = 'sbu_hist'   # <- nombre corto y claro para salario básico unificado

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
        except errors.NetworkError as e:
            last_err = e
            log(f"[WARN] Intento {i+1}/{MAX_RETRIES} fallido: {e}")
            time.sleep(RETRY_DELAY)
    raise RuntimeError(f"No pude conectar a ClickHouse: {last_err}")

def ensure_database(client: Client, db: str):
    client.execute(f"CREATE DATABASE IF NOT EXISTS {db}")
    client.execute(f"USE {db}")

# ========= (Re)creación de tablas =========
def recreate_table_provincias(client: Client, db: str):
    client.execute(f"DROP TABLE IF EXISTS {db}.{TAB_PROV}")
    client.execute(f"""
        CREATE TABLE {db}.{TAB_PROV} (
            CodigoProvincia   String,
            CodigoCanton      String,
            CodigoParroquia   String,
            NombreProvincia   String,
            NombreCanton      String,
            NombreParroquia   String
        )
        ENGINE = MergeTree()
        ORDER BY (CodigoProvincia, CodigoCanton, CodigoParroquia)
    """)
    log(f"[OK] Tabla {db}.{TAB_PROV} recreada.")

def recreate_table_poverty(client: Client, db: str):
    client.execute(f"DROP TABLE IF EXISTS {db}.{TAB_POV}")
    client.execute(f"""
        CREATE TABLE {db}.{TAB_POV} (
            periodo String,
            linea_pobreza Float64,
            linea_pobreza_extrema Float64
        )
        ENGINE = MergeTree
        ORDER BY (periodo)
    """)
    log(f"[OK] Tabla {db}.{TAB_POV} recreada.")

def recreate_table_sbu(client: Client, db: str):
    client.execute(f"DROP TABLE IF EXISTS {db}.{TAB_SBU}")
    client.execute(f"""
        CREATE TABLE {db}.{TAB_SBU} (
            periodo String,   -- 'YYYYMM'
            sbu     Float64   -- salario básico unificado del periodo
        )
        ENGINE = MergeTree
        ORDER BY (periodo)
    """)
    log(f"[OK] Tabla {db}.{TAB_SBU} recreada.")

# ========= Ingestas =========
def ingest_codigos_provincias(client: Client, db: str, csv_path: str, sep: str = ';'):
    exp_cols = [
        'CodigoProvincia','CodigoCanton','CodigoParroquia',
        'NombreProvincia','NombreCanton','NombreParroquia'
    ]
    log(f"[CODIGOS] Leyendo archivo: {csv_path}")
    try:
        df = pd.read_csv(csv_path, sep=sep, dtype=str, encoding='utf-8-sig')
    except Exception as e:
        log(f"[ERROR] No se pudo leer {csv_path}: {e}")
        raise

    df.columns = [c.strip() for c in df.columns]
    missing = [c for c in exp_cols if c not in df.columns]
    if missing:
        log(f"[ERROR] Faltan columnas requeridas en {csv_path}: {missing}")
        log(f"Columnas encontradas: {list(df.columns)}")
        raise RuntimeError("Columnas faltantes en diccionario_provincias")

    df = df[exp_cols].fillna('')
    data = [tuple(r) for r in df.itertuples(index=False, name=None)]
    if not data:
        log("[CODIGOS] No hay filas para insertar.")
        return

    log(f"[CODIGOS] Insertando {len(data)} filas en {db}.{TAB_PROV}...")
    client.execute(
        f"INSERT INTO {db}.{TAB_PROV} ({','.join(exp_cols)}) VALUES",
        data
    )
    log("[CODIGOS] Inserción completada.")

def ingest_poverty_lines(client: Client, db: str, csv_path: str, sep: str = ';', decimal: str = ','):
    exp_cols = ['periodo', 'linea_pobreza', 'linea_pobreza_extrema']
    log(f"[POVERTY] Leyendo archivo: {csv_path}")
    try:
        df = pd.read_csv(csv_path, sep=sep, decimal=decimal, encoding='utf-8-sig')
    except Exception as e:
        log(f"[ERROR] No se pudo leer {csv_path}: {e}")
        raise

    df.columns = [c.strip() for c in df.columns]
    missing = [c for c in exp_cols if c not in df.columns]
    if missing:
        log(f"[ERROR] Faltan columnas requeridas en {csv_path}: {missing}")
        log(f"Columnas encontradas: {list(df.columns)}")
        raise RuntimeError("Columnas faltantes en poverty_lines")

    df = df[exp_cols].copy()
    # periodo -> 'YYYYMM' como String (6 dígitos)
    df['periodo'] = (
        df['periodo']
        .astype(str)
        .str.replace(r'\.0$', '', regex=True)
        .str.zfill(6)
    )

    for c in ['linea_pobreza','linea_pobreza_extrema']:
        df[c] = pd.to_numeric(df[c], errors='coerce')

    df = df.where(pd.notnull(df), None)

    data = [tuple(r) for r in df.itertuples(index=False, name=None)]
    if not data:
        log("[POVERTY] No hay filas para insertar.")
        return

    log(f"[POVERTY] Insertando {len(data)} filas en {db}.{TAB_POV}...")
    client.execute(
        f"INSERT INTO {db}.{TAB_POV} ({','.join(exp_cols)}) VALUES",
        data
    )
    log("[POVERTY] Inserción completada.")

def ingest_sbu(client: Client, db: str, csv_path: str, sep: str = ';', decimal: str = ','):
    """
    CSV esperado (flexible):
      - 'periodo' (YYYYMM) y 'sbu'
    Soporta alias de 'sbu': 'salario', 'salario_basico', 'salario_basico_unificado'.
    También tolera archivos con 'anio' y 'mes' en vez de 'periodo'.
    """
    log(f"[SBU] Leyendo archivo: {csv_path}")
    try:
        df = pd.read_csv(csv_path, sep=sep, decimal=decimal, encoding='utf-8-sig')
    except Exception as e:
        log(f"[ERROR] No se pudo leer {csv_path}: {e}")
        raise

    # Normalizar headers
    cols_map = {c.strip(): c.strip() for c in df.columns}
    low = {c.lower(): c for c in cols_map}

    # Detectar columna periodo
    periodo_col = low.get('periodo')
    if periodo_col is None:
        # probar 'anio' + 'mes'
        anio_col = low.get('anio') or low.get('ano') or low.get('year')
        mes_col  = low.get('mes')  or low.get('month')
        if anio_col and mes_col:
            df['periodo'] = (
                df[anio_col].astype(str).str.replace(r'\.0$', '', regex=True).str.zfill(4) +
                df[mes_col].astype(str).str.replace(r'\.0$', '', regex=True).str.zfill(2)
            )
            periodo_col = 'periodo'
        else:
            raise RuntimeError("[SBU] No encuentro columna 'periodo' ni ('anio','mes').")

    # Detectar columna sbu
    sbu_aliases = ['sbu', 'salario', 'salario_basico', 'salario_basico_unificado']
    sbu_col = None
    for k in sbu_aliases:
        cand = low.get(k)
        if cand:
            sbu_col = cand
            break
    if sbu_col is None:
        raise RuntimeError("[SBU] No encuentro columna con SBU (intenta: sbu/salario/salario_basico/salario_basico_unificado).")

    out = (
        df[[periodo_col, sbu_col]]
        .rename(columns={periodo_col: 'periodo', sbu_col: 'sbu'})
        .copy()
    )

    # Normalizar periodo a 6 dígitos
    out['periodo'] = (
        out['periodo']
        .astype(str)
        .str.replace(r'\.0$', '', regex=True)
        .str.zfill(6)
    )
    # Asegurar numérico
    out['sbu'] = pd.to_numeric(out['sbu'], errors='coerce')

    out = out.where(pd.notnull(out), None)

    data = [tuple(r) for r in out[['periodo','sbu']].itertuples(index=False, name=None)]
    if not data:
        log("[SBU] No hay filas para insertar.")
        return

    log(f"[SBU] Insertando {len(data)} filas en {db}.{TAB_SBU}...")
    client.execute(
        f"INSERT INTO {db}.{TAB_SBU} (periodo, sbu) VALUES",
        data
    )
    log("[SBU] Inserción completada.")

# ========= Main =========
def main():
    client = get_ch_client()
    ensure_database(client, CH_DATABASE)

    # Re-crear tablas (DROP + CREATE) para evitar duplicados
    recreate_table_provincias(client, CH_DATABASE)
    recreate_table_poverty(client, CH_DATABASE)
    recreate_table_sbu(client, CH_DATABASE)

    # Ingestas directas desde archivos específicos
    ingest_codigos_provincias(client, CH_DATABASE, CODIGOS_FILE, sep=';')
    ingest_poverty_lines(client, CH_DATABASE, POVERTY_FILE, sep=';', decimal=',')
    # Para tu archivo en /mnt/data, puedes exportar SBU_FILE=/mnt/data/salario_basico_unificado.csv
    ingest_sbu(client, CH_DATABASE, SBU_FILE, sep=';', decimal=',')

    log("Proceso completado.")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        log(f"[FATAL] {e}")
        sys.exit(1)
