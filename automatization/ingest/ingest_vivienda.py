#!/usr/bin/env python3
import os
import re
import time
import shutil
import pandas as pd
from pathlib import Path
from clickhouse_driver import Client, errors
from datetime import datetime

# ========= Parámetros generales =========
MAX_RETRIES     = int(os.getenv('MAX_RETRIES', 12))
RETRY_DELAY     = int(os.getenv('RETRY_DELAY', 5))    # segundos
LOG_DIR         = os.getenv('LOG_DIR', '/ingest/logs')
ERR_DIR         = os.getenv('ERR_DIR', '/ingest/errors')
STOP_ON_ERROR   = os.getenv('STOP_ON_ERROR', 'false').lower() in ('1', 'true', 'yes')
USE_SENTINELS   = os.getenv('USE_SENTINELS', 'false').lower() in ('1', 'true', 'yes')

# Parámetros específicos para vivienda_data
PROCESSED_DIR   = os.getenv('PROCESSED_DIR_VIVIENDA', '/data/enemdu_vivienda/processed')
DATA_DIR        = os.getenv('VIVIENDA_DIR', '/data/enemdu_vivienda/unprocessed')
DATABASE        = os.getenv('CH_DATABASE', 'indicadores')
TABLE           = os.getenv('CH_TABLE', 'enemdu_vivienda')
TARGET_YEARS = set(range(2007, 2014))  # 2007..2013 inclusive
CITY_CORRECTIONS = [
    ("0808", "2302"),  # LA CONCORDIA
    ("0915", "2403"),  # SALINAS
    ("0917", "2401"),  # SANTA ELENA
    ("1706", "2301"),  # SANTO DOMINGO
    ("0926", "2402"),  # LA LIBERTAD
]

def normalize_ciudad_inplace(df: pd.DataFrame) -> None:
    """
    Si periodo (YYYYMM) ∈ [2007..2013] y ciudad = PPCCPP,
    reescribe el prefijo PPCC según CITY_CORRECTIONS, conservando los últimos 2 dígitos (parroquia).
    """
    if 'ciudad' not in df.columns or 'periodo' not in df.columns:
        return

    # Series tolerantes a nulos
    s_ciudad  = df['ciudad'].fillna('').astype(str).str.strip().str.zfill(6)
    s_periodo = df['periodo'].fillna('').astype(str)

    # Año como número; NaN si no es parseable
    years = pd.to_numeric(s_periodo.str.slice(0, 4), errors='coerce')
    mask_year = years.isin(TARGET_YEARS)

    # Reescritura por prefijo
    for old, new in CITY_CORRECTIONS:
        m = mask_year & s_ciudad.str.startswith(old)
        # Conservar parroquia (últimos 2 dígitos)
        s_ciudad = s_ciudad.where(~m, new + s_ciudad.str[-2:])

    # Escribimos de vuelta (si estaba vacío/nulo originalmente, lo dejamos igual)
    was_empty = df['ciudad'].isna() | (df['ciudad'].astype(str).str.strip() == '')
    df['ciudad'] = s_ciudad.mask(was_empty, df['ciudad'])

# Columnas por tipo
questions = [
    "vi01", "vi02", "vi03a", "vi03b", "vi04a", "vi04b", "vi05a", "vi05b",
    "vi06", "vi07", "vi07a", "vi07b", "vi08", "vi09", "vi09a", "vi09b",
    "vi10", "vi101", "vi102", "vi10a", "vi11", "vi12", "vi13", "vi14",
    "vi141", "vi142", "vi143", "vi144", "vi1511", "vi1512", "vi1521", "vi1522",
    "vi1531", "vi1532", "vi1533", "vi1534", "vi1541", "vi1542", "vi1543", "vi1544",
    "vi1551", "vi1552", "vi1553", "vi1554", "vi1561", "vi1562", "vi1563", "vi1564",
    "vi16", "vi161", "vi162", "vi163", "vi164", "vi165", "vi166", "vi167",
    "vi168", "vi169", "vi1610", "vi1611", "vi1612", "vi1613", "vi1614",
    "vi17", "vi171", "vi172", "vi173", "vi174", "vi175", "vi176", "vi177",
    "vi178", "vi179", "vi1710", "vi1711", "vi1712", "vi1713", "vi1714",
    "vi18", "vi181", "vi182", "vi183", "vi184", "vi185", "vi186", "vi187",
    "vi188", "vi189", "vi1810", "vi1811", "vi1812", "vi1813", "vi1814", "vivienda"
]
STRING_COLS = {'area','ciudad','conglomerado','estrato','periodo','panelm',
               'id_hogar','id_vivienda','sector','upm','hogar', 'zona'}
INT_COLS    = set(questions)
FLOAT_COLS  = {'fexp'}

# Sentinelas
SENTINEL_INT    = -404
SENTINEL_FLOAT  = -404.0
SENTINEL_STRING = "-404"

# ========= Utilidades =========
def ensure_dirs():
    for d in (LOG_DIR, ERR_DIR, PROCESSED_DIR):
        Path(d).mkdir(parents=True, exist_ok=True)

def log(msg: str):
    ts = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{ts} UTC] {msg}", flush=True)

def _is_float(x: str) -> bool:
    try: 
        float(x)
        return True
    except:
        return False

def coerce_value(col: str, raw):
    s = None if raw is None or (isinstance(raw, float) and pd.isna(raw)) else str(raw)
    if col in FLOAT_COLS:
        if s is None:
            return SENTINEL_FLOAT if USE_SENTINELS else None
        s2 = s.replace(' ', '').replace(',', '.')
        return float(s2) if _is_float(s2) else (SENTINEL_FLOAT if USE_SENTINELS else None)
    if col in INT_COLS:
        if s is None:
            return SENTINEL_INT if USE_SENTINELS else None
        if s.strip().lstrip('-').isdigit():
            return int(s)
        return SENTINEL_INT if USE_SENTINELS else None
    if col in STRING_COLS:
        if not s or s.strip() == "":
            return SENTINEL_STRING if USE_SENTINELS else None
        if col == 'ciudad':
            s = s.strip().zfill(6)
        return s.strip()
    return SENTINEL_STRING if USE_SENTINELS else None

def get_ch_client():
    last_err = None
    for i in range(MAX_RETRIES):
        try:
            client = Client(
                host=os.getenv('CH_HOST','clickhouse_server'),
                port=int(os.getenv('CH_PORT',9000)),
                user=os.getenv('CH_USER','admin'),
                password=os.getenv('CH_PASSWORD','secret_pw'),
                database=DATABASE
            )
            client.execute('SELECT 1')
            log("[OK] Conectado a ClickHouse")
            return client
        except errors.NetworkError as e:
            last_err = e
            log(f"[WARN] Intento {i+1}/{MAX_RETRIES} fallido: {e}")
            time.sleep(RETRY_DELAY)
    raise RuntimeError(f"No pude conectar: {last_err}")

def write_failed_row(base, header, values):
    out = Path(ERR_DIR) / f"{base}_failed.csv"
    write_header = not out.exists()
    import csv
    with out.open('a', newline='', encoding='utf-8') as f:
        w = csv.writer(f, delimiter=';')
        if write_header:
            w.writerow(header)
        w.writerow(values)

def move_to_processed(path: Path):
    dest = Path(PROCESSED_DIR) / path.name
    shutil.move(str(path), str(dest))
    log(f"→ Movido '{path.name}' a processed")

def sort_key(path: Path):
    # Extrae año y mes del nombre tipo "2025_01_X.CSV"
    m = re.match(r"(\d{4})_(\d{2})_", path.name)
    if m:
        year, month = int(m.group(1)), int(m.group(2))
        return (year, month, path.name)
    return (9999, 99, path.name)  # fallback alfabético si no cumple el patrón

# ========= Procesar CSVs =========
def main():
    ensure_dirs()
    client = get_ch_client()
    client.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")
    client.execute(f"USE {DATABASE}")

    # Obtener esquema destino
    cols_meta = client.execute(
        "SELECT name FROM system.columns "
        "WHERE database=%(db)s AND table=%(tbl)s "
        "ORDER BY position",
        {'db': DATABASE, 'tbl': TABLE}
    )
    col_names = [r[0] for r in cols_meta]
    log(f"Columnas destino {TABLE}: {col_names}")

    # for csvf in Path(DATA_DIR).glob('*.csv'):
    for csvf in sorted(Path(DATA_DIR).glob("*.csv"), key=sort_key):
        log(f"Procesando {csvf.name}...")
        # Intento de lectura
        try:
            df = pd.read_csv(csvf, sep=';', dtype={c: str for c in STRING_COLS if c in col_names}, low_memory=False)
        except Exception as e:
            log(f"[ERROR] Lectura {csvf.name}: {e}")
            move_to_processed(csvf)
            continue
        normalize_ciudad_inplace(df)
        df = df.where(pd.notnull(df), None)
        batch = [[coerce_value(c, row.get(c)) for c in col_names] for _, row in df.iterrows()]

        success = False
        try:
            client.execute(
                f"INSERT INTO {DATABASE}.{TABLE} ({','.join(col_names)}) VALUES",
                batch
            )
            log(f"→ Insertadas {len(batch)} filas.")
            success = True
        except Exception as e:
            log(f"[FAIL BATCH] {e}")
            ok = fail = 0
            for i, vals in enumerate(batch, 1):
                try:
                    client.execute(
                        f"INSERT INTO {DATABASE}.{TABLE} ({','.join(col_names)}) VALUES",
                        [vals]
                    )
                    ok += 1
                except Exception as ex:
                    fail += 1
                    log(f"[FAIL fila {i}] {ex}")
                    write_failed_row(f"{TABLE}_{csvf.stem}", col_names, vals)
                    if STOP_ON_ERROR:
                        return
            log(f"→ {ok} OK, {fail} fallidas.")
            success = True  # movemos aun con fallos parciales

        if success:
            move_to_processed(csvf)

    log("Proceso completado vivienda_data.")

if __name__ == '__main__':
    main()
