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

# Parámetros específicos para enemdu_persona
DATA_DIR        = os.getenv('PERSONA_DIR', '/data/enemdu_persona/unprocessed')
PROCESSED_DIR   = os.getenv('PROCESSED_DIR_PERSONA', '/data/enemdu_persona/processed')

host     = os.getenv('CH_HOST', 'clickhouse_server')
port     = int(os.getenv('CH_PORT', 9000))
user     = os.getenv('CH_USER', 'admin')
password = os.getenv('CH_PASSWORD', 'secret_pw')
database = os.getenv('CH_DATABASE', 'indicadores')
table    = os.getenv('CH_TABLE', 'enemdu_persona')

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

def ensure_dirs():
    Path(LOG_DIR).mkdir(parents=True, exist_ok=True)
    Path(ERR_DIR).mkdir(parents=True, exist_ok=True)
    Path(PROCESSED_DIR).mkdir(parents=True, exist_ok=True)

def log(msg: str):
    ts = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{ts} UTC] {msg}", flush=True)

def _is_float(x: str) -> bool:
    try:
        float(x)
        return True
    except Exception:
        return False

FLOAT_COLS  = {'fexp','ingrl','ingpc'}
INT_COLS = {
    'condact','desempleo','empleo','secemp','estrato','nnivins','rama1',
    'vivienda','pobreza','epobreza', 'p01','p02','p03','p04','p05a','p05b','p06','p07','p09','p10a',
    'p10b','p15','p20','p21','p22','p23', 'p24','p25','p26','p27','p28','p29',
    'p32','p33','p34','p35','p36','p37','p38','p39', 'p40','p41','p42','p44f',
    'p46','p47a','p47b','p49','p50','p51a','p51b','p51c','p55','p56a','p56b','p58' ,'p63', 'p64a','p64b',
    'p65','p66','p67','p68a','p68b','p69','p70a','p70b','p71a','p71b','p72a',
    'p72b','p73a','p73b','p74a','p74b','p75','p76','p77'
}
STRING_COLS = {
    'area','ciudad','cod_inf','periodo','panelm','id_hogar','id_persona','id_vivienda','upm',
    'grupo1','hogar','zona','sector'
}



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
    except Exception:
        return False

def coerce_value(col: str, raw, is_nullable: bool):
    s = None if raw is None or (isinstance(raw, float) and pd.isna(raw)) else str(raw)

    def fallback(kind: str):  # kind: 'str' | 'int' | 'float'
        if is_nullable:
            # Permitimos NULL reales si no usamos sentinelas
            if not USE_SENTINELS:
                return None
        # Para no-nullable o si se usan sentinelas
        if kind == 'str':
            return SENTINEL_STRING if USE_SENTINELS else ""
        if kind == 'int':
            return SENTINEL_INT if USE_SENTINELS else 0
        if kind == 'float':
            return SENTINEL_FLOAT if USE_SENTINELS else 0.0

    if col in FLOAT_COLS:
        if s is None:
            return fallback('float')
        s2 = s.replace(' ', '').replace(',', '.')
        return float(s2) if _is_float(s2) else fallback('float')

    if col in INT_COLS:
        if s is None:
            return fallback('int')
        s2 = s.strip()
        if s2.lstrip('-').isdigit():
            try:
                return int(s2)
            except Exception:
                return fallback('int')
        return fallback('int')

    # STRING_COLS y cualquier columna desconocida se tratan como texto
    if s is None or s.strip() == "":
        return fallback('str')
    s = s.strip()
    if col == 'ciudad':
        s = s.zfill(6)
    return s

def get_ch_client():
    last_err = None
    for i in range(MAX_RETRIES):
        try:
            client = Client(
                host=host, port=port,
                user=user, password=password,
                database=database
            )
            client.execute('SELECT 1')
            log("[OK] Conectado a ClickHouse")
            return client
        except errors.NetworkError as e:
            last_err = e
            log(f"[WARN] Intento {i+1}/{MAX_RETRIES} fallido, reintentando en {RETRY_DELAY}s… ({e})")
            time.sleep(RETRY_DELAY)
    raise RuntimeError(f"No pude conectar a ClickHouse: {last_err}")

def ensure_db_and_table(client: Client):
    client.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
    client.execute(f"USE {database}")

def fetch_table_columns(client: Client, db: str, tbl: str):
    rows = client.execute(
        """
        SELECT name, type, position
        FROM system.columns
        WHERE database = %(db)s AND table = %(tbl)s
        ORDER BY position
        """,
        {'db': db, 'tbl': tbl}
    )
    return [(name, dtype, dtype.startswith('Nullable(')) for name, dtype, _ in rows]

def write_failed_row(file_base: str, header, values):
    out_path = Path(ERR_DIR) / f"{file_base}_failed_rows.csv"
    write_header = not out_path.exists()
    import csv
    with out_path.open('a', newline='', encoding='utf-8') as f:
        w = csv.writer(f, delimiter=';')
        if write_header:
            w.writerow(header)
        w.writerow(values)

def move_to_processed(path: Path):
    dest = Path(PROCESSED_DIR) / path.name
    shutil.move(str(path), str(dest))
    log(f"→ Movido '{path.name}' a processed")

def row_to_insert_values(row_dict, columns_meta):
    # columns_meta = [(name, dtype, is_nullable), ...]
    return [
        coerce_value(name, row_dict.get(name, None), is_nullable)
        for (name, _dtype, is_nullable) in columns_meta
    ]

# forzar lectura de string cols
string_dtypes = { col: str for col in STRING_COLS }
def sort_key(path: Path):
    # Extrae año y mes del nombre tipo "2025_01_X.CSV"
    m = re.match(r"(\d{4})_(\d{2})_", path.name)
    if m:
        year, month = int(m.group(1)), int(m.group(2))
        return (year, month, path.name)
    return (9999, 99, path.name)  # fallback alfabético si no cumple el patrón

def main():
    # ---- parámetros de fallback por bloques ----
    FALLBACK_CHUNK = 20000          # tamaño de micro-bloque para reintentos
    SMALL_CHUNK_THRESHOLD = 256     # debajo de esto, probamos fila a fila

    class StopRequested(Exception):
        pass

    def insert_values(client, db, tb, cols, values):
        client.execute(f"INSERT INTO {db}.{tb} ({', '.join(cols)}) VALUES", values)

    def insert_chunk_recursive(client, db, tb, cols, chunk, base_idx, csv_stem, header_out):
        """
        Intenta insertar 'chunk' completo; si falla, lo parte a la mitad.
        Cuando el trozo es pequeño, cae a fila-a-fila para aislar filas malas.
        Devuelve (ok_cnt, fail_cnt).
        """
        try:
            insert_values(client, db, tb, cols, chunk)
            return (len(chunk), 0)
        except Exception:
            # Demasiado grande para depurar fila a fila => divide y vencerás
            if len(chunk) > SMALL_CHUNK_THRESHOLD:
                mid = len(chunk) // 2
                ok1, fail1 = insert_chunk_recursive(client, db, tb, cols, chunk[:mid], base_idx, csv_stem, header_out)
                ok2, fail2 = insert_chunk_recursive(client, db, tb, cols, chunk[mid:], base_idx + mid, csv_stem, header_out)
                return (ok1 + ok2, fail1 + fail2)

            # Trozo pequeño: probamos fila a fila para registrar las que fallan
            ok_cnt, fail_cnt = 0, 0
            for off, values in enumerate(chunk, start=0):
                try:
                    insert_values(client, db, tb, cols, [values])
                    ok_cnt += 1
                except Exception as e_row:
                    fail_cnt += 1
                    # fila 1-based para el log global
                    rowno = base_idx + off + 1
                    log(f"[FAIL] {csv_stem}.csv fila {rowno}: {e_row}")
                    write_failed_row(csv_stem, header_out, list(values))
                    if STOP_ON_ERROR:
                        log("[STOP_ON_ERROR] Activado. Me detengo en el primer error.")
                        raise StopRequested()
            return (ok_cnt, fail_cnt)

    def insert_with_chunk_fallback(client, db, tb, cols, all_values, csv_stem, header_out):
        """
        Recorre el lote en micro-bloques; si uno falla, usa recursión para
        encontrar y aislar filas problemáticas sin generar demasiados parts.
        """
        ok_total, fail_total = 0, 0
        n = len(all_values)
        for start in range(0, n, FALLBACK_CHUNK):
            end = min(start + FALLBACK_CHUNK, n)
            chunk = all_values[start:end]
            try:
                insert_values(client, db, tb, cols, chunk)
                ok_total += len(chunk)
            except Exception:
                ok, fail = insert_chunk_recursive(client, db, tb, cols, chunk, base_idx=start, csv_stem=csv_stem, header_out=header_out)
                ok_total += ok
                fail_total += fail
                if STOP_ON_ERROR and fail > 0:
                    raise StopRequested()
        return ok_total, fail_total

    # ---- flujo original con fallback por bloques ----
    ensure_dirs()
    client = get_ch_client()
    ensure_db_and_table(client)
    columns_meta = fetch_table_columns(client, database, table)
    col_names = [c[0] for c in columns_meta]
    if 'extra' in col_names:
        raise RuntimeError("La tabla aún tiene la columna 'extra'.")
    log(f"Columnas en destino ({database}.{table}): {', '.join(col_names)}")

    for csv_path in sorted(Path(DATA_DIR).glob("*.csv"), key=sort_key):
        log(f"Procesando {csv_path.name} …")
        try:
            df = pd.read_csv(
                csv_path, sep=';', encoding='utf-8',
                dtype=string_dtypes, low_memory=False, header=0
            )
        except Exception as e:
            log(f"[ERROR] No pude leer el CSV {csv_path.name}: {e}")
            move_to_processed(csv_path)
            continue
        normalize_ciudad_inplace(df)
        df = df.where(pd.notnull(df), None)
        header_out = col_names

        batch_values = [
            tuple(row_to_insert_values(row.to_dict(), columns_meta))
            for _, row in df.iterrows()
        ]
        total = len(batch_values)

        try:
            # intento 1: inserción masiva
            client.execute(
                f"INSERT INTO {database}.{table} ({', '.join(col_names)}) VALUES",
                batch_values
            )
            log(f"→ Insertadas {total} filas en bloque exitosamente.")
            move_to_processed(csv_path)
            continue

        except Exception as e:
            log(f"[FAIL- BATCH] {csv_path.name}: {e}")
            try:
                ok_cnt, fail_cnt = insert_with_chunk_fallback(
                    client, database, table, col_names, batch_values, csv_path.stem, header_out
                )
                log(f"→ Tras fallback por bloques, {ok_cnt} filas OK, {fail_cnt} fallidas.")
                move_to_processed(csv_path)
            except StopRequested:
                # ya se registró el motivo exacto en el log
                return

    log("Proceso completado enemdu_persona.")


if __name__ == '__main__':
    main()
