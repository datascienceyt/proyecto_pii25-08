#!/usr/bin/env python3
import os
import re
import csv
import time
import shutil
import pandas as pd
from pathlib import Path
from clickhouse_driver import Client, errors
from datetime import datetime

# =====================
# Environment / Config
# =====================
UNPROCESSED_DIR = os.getenv("LATINOBAROMETRO_NORM_CSV", "/data/latinobarometro/normalized_csv")
PROCESSED_DIR   = os.getenv("LATINOBAROMETRO_PROCESSED", "/data/latinobarometro/processed")

# Logging / errors
LOG_DIR         = os.getenv("LOG_DIR", "/ingest/logs")
ERR_DIR         = os.getenv("ERR_DIR", "/ingest/errors")

# Behavior flags
MAX_RETRIES     = int(os.getenv("MAX_RETRIES", 12))
RETRY_DELAY     = int(os.getenv("RETRY_DELAY", 5))           # seconds between CH connect retries
STOP_ON_ERROR   = os.getenv("STOP_ON_ERROR", "false").lower() in ("1", "true", "yes")

# ClickHouse connection / destination
CH_HOST   = os.getenv("CH_HOST", "clickhouse_server")
CH_PORT   = int(os.getenv("CH_PORT", 9000))
CH_USER   = os.getenv("CH_USER", "admin")
CH_PASS   = os.getenv("CH_PASSWORD", "secret_pw")
CH_DB     = os.getenv("CH_DATABASE", "indicadores")
CH_TABLE  = os.getenv("CH_TABLE", "latinobarometro")

# CSV reading
CSV_SEP         = ";"
CSV_ENCODING    = "utf-8"
LOW_MEMORY_READ = False

# Fallback insert tuning
FALLBACK_CHUNK          = int(os.getenv("FALLBACK_CHUNK", 20000))
SMALL_CHUNK_THRESHOLD   = int(os.getenv("SMALL_CHUNK_THRESHOLD", 256))

# =====================
# Schema (exactly as provided)
# =====================
SCHEMA = [
    ("research_year", "Int16"),
    ("resp_country", "Int32"),
    ("country_name", """ALIAS transform(
        resp_country,
        [32, 68, 76, 152, 170, 188, 218, 222, 724, 320, 340, 484, 558, -3, -2, -4, -1, -5, 591, 600, 604, 214, 858, 862],
        ['Argentina','Bolivia','Brasil','Chile','Colombia','Costa Rica','Ecuador','El Salvador','España','Guatemala','Honduras','México','Nicaragua','No aplicable','No contesta','No preguntada','No sabe','No sabe / No contesta','Panamá','Paraguay','Perú','Rep. Dominicana','Uruguay','Venezuela'],
        'Desconocido'
    )"""),
    ("research_region", "Int32"),
    ("research_city_size", "Nullable(Int32)"),
    ("research_city", "Int32"),
    ("democ_supp", "Nullable(Int16)"),
    ("democ_satis", "Nullable(Int16)"),
    ("left_right_scale", "Nullable(Int16)"),
    ("elections_vote", "Nullable(Int16)"),
    ("job_concern", "Nullable(Int16)"),
    ("econ_situation", "Nullable(Int16)"),
    ("goods_wash_mach", "Nullable(Int16)"),
    ("goods_car", "Nullable(Int16)"),
    ("goods_sewage", "Nullable(Int16)"),
    ("goods_hot_water", "Nullable(Int16)"),
    ("confidence_congress", "Nullable(Int16)"),
    ("confidence_judiciary", "Nullable(Int16)"),
    ("confidence_church", "Nullable(Int16)"),
    ("confidence_police", "Nullable(Int16)"),
    ("confidence_army", "Nullable(Int16)"),
    ("confidence_political_parties", "Nullable(Int16)"),
    ("resp_sex", "Nullable(Int16)"),
    ("resp_age", "Nullable(Int16)"),
    ("resp_chief", "Nullable(Int16)"),
    ("resp_education", "Nullable(Int16)"),
    ("resp_employment", "Nullable(Int16)"),
    ("resp_economic_perception", "Nullable(Int16)"),
    ("resp_religion", "Nullable(Int16)"),
]

ORDER_BY = "(research_year, resp_country, research_region, research_city)"

def log(msg: str):
    ts = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts} UTC] {msg}", flush=True)

def ensure_dirs():
    for d in (LOG_DIR, ERR_DIR):
        Path(d).mkdir(parents=True, exist_ok=True)
    if PROCESSED_DIR:
        Path(PROCESSED_DIR).mkdir(parents=True, exist_ok=True)

def get_ch_client():
    last_err = None
    for i in range(MAX_RETRIES):
        try:
            client = Client(host=CH_HOST, port=CH_PORT, user=CH_USER, password=CH_PASS, database=CH_DB)
            client.execute("SELECT 1")
            log("[OK] Conectado a ClickHouse")
            return client
        except errors.NetworkError as e:
            last_err = e
            log(f"[WARN] Intento {i+1}/{MAX_RETRIES} fallido, reintentando en {RETRY_DELAY}s… ({e})")
            time.sleep(RETRY_DELAY)
    raise RuntimeError(f"No pude conectar a ClickHouse: {last_err}")

def require_paths():
    if not UNPROCESSED_DIR:
        raise RuntimeError("UNPROCESSED_DIR no está definido. Establécelo en tu entorno.")
    if not PROCESSED_DIR:
        raise RuntimeError("PROCESSED_DIR no está definido. Establécelo en tu entorno.")
    Path(UNPROCESSED_DIR).mkdir(parents=True, exist_ok=True)

def ensure_db_and_table(client: Client):
    client.execute(f"CREATE DATABASE IF NOT EXISTS {CH_DB}")
    client.execute(f"USE {CH_DB}")

    cols = ",\n    ".join(f"`{name}` {dtype}" for name, dtype in SCHEMA)
    ddl = f"""
    CREATE TABLE IF NOT EXISTS {CH_DB}.{CH_TABLE}
    (
        {cols}
    )
    ENGINE = MergeTree
    ORDER BY {ORDER_BY}
    """
    client.execute(ddl)
    log(f"[OK] Tabla {CH_DB}.{CH_TABLE} verificada/creada.")

def fetch_table_columns(client: Client, db: str, tbl: str):
    rows = client.execute(
        """
        SELECT
            name,
            type,
            position,
            default_kind  -- '' | DEFAULT | MATERIALIZED | ALIAS
        FROM system.columns
        WHERE database = %(db)s AND table = %(tbl)s
        ORDER BY position
        """,
        {"db": db, "tbl": tbl},
    )
    cols = []
    for name, dtype, _pos, default_kind in rows:
        is_nullable = dtype.startswith("Nullable(")
        is_computed = (default_kind in ("ALIAS", "MATERIALIZED"))
        cols.append((name, dtype, is_nullable, is_computed))
    return cols

def write_failed_row(file_base: str, header, values):
    out_path = Path(ERR_DIR) / f"{file_base}_failed_rows.csv"
    write_header = not out_path.exists()
    with out_path.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        if write_header:
            w.writerow(header)
        w.writerow(values)

def move_to_processed(path: Path):
    dest = Path(PROCESSED_DIR) / path.name
    shutil.move(str(path), str(dest))
    log(f"→ Movido '{path.name}' a processed")

def _is_intish(s: str) -> bool:
    s = s.strip()
    if s.startswith(("+", "-")):
        return s[1:].isdigit()
    return s.isdigit()

def _clip_int16(x: int):
    return max(-32768, min(32767, x))

def _clip_int32(x: int):
    return max(-2147483648, min(2147483647, x))

def _parse_nullable_int(raw, bits=16):
    # Acepta None/NaN
    if raw is None or (isinstance(raw, float) and pd.isna(raw)):
        return None

    v = None

    # Caso 1: ya viene como número
    if isinstance(raw, int):
        v = raw
    elif isinstance(raw, float):
        # Sólo aceptamos floats que representen enteros (1.0, -3.0, 0.0)
        if not pd.isna(raw) and float(raw).is_integer():
            v = int(raw)
        else:
            return None
    else:
        # Caso 2: cadena -> normalizamos "1.0", "1.000", espacios y comas
        s = str(raw).strip()
        if s == "":
            return None
        s2 = s.replace(" ", "").replace(",", "")

        # Si es del tipo 123.0 o -45.000 -> quitar la parte decimal de ceros
        m = re.match(r'^([+-]?\d+)\.0+$', s2)
        if m:
            s2 = m.group(1)

        if _is_intish(s2):
            try:
                v = int(s2)
            except Exception:
                return None
        else:
            return None

    # Clip según el tipo destino
    if bits == 16:
        return _clip_int16(int(v))
    else:
        return _clip_int32(int(v))

def _parse_int_nonnull(raw, bits=16, default_zero=True):
    v = _parse_nullable_int(raw, bits)
    if v is None:
        return 0 if default_zero else None
    return v

def _is_type(dtype: str, name: str):
    return dtype == name or dtype.startswith(f"{name}(")

def _normalize_research_year(val):
    """
    '23' -> 2023, '24' -> 2024 (y futuros). Regla:
    0..30 -> 2000+yy, 31..99 -> 1900+yy. Otros: int si posible, si no None.
    """
    if val is None:
        return None
    s = str(val).strip()
    if s == "":
        return None
    s2 = s.replace(" ", "").replace(",", "")
    if s2.endswith(".0"):
        s2 = s2[:-2]
    if s2.isdigit() or (s2.startswith("-") and s2[1:].isdigit()):
        try:
            x = int(s2)
        except Exception:
            return None
        if 0 <= x < 100:
            return 2000 + x if x <= 30 else 1900 + x
        return x
    return None

def coerce_int16_nullable(raw, is_nullable: bool):
    if raw is None or (isinstance(raw, float) and pd.isna(raw)):
        return None if is_nullable else 0
    s = str(raw).strip()
    if s == "":
        return None if is_nullable else 0
    s2 = s.replace(" ", "").replace(",", "")
    if _is_intish(s2):
        try:
            return _clip_int16(int(s2))
        except Exception:
            pass
    return None if is_nullable else 0

def row_to_values(row_dict, columns_meta_insert):
    vals = []
    for (name, dtype, is_nullable, _is_computed) in columns_meta_insert:
        raw = row_dict.get(name, None)

        if name == "research_year":
            y = _normalize_research_year(raw)
            vals.append(_clip_int16(int(y)) if y is not None else 0)
            continue

        # Int16 / Nullable(Int16)
        if _is_type(dtype, "Int16"):
            vals.append(_parse_int_nonnull(raw, bits=16))
            continue
        if _is_type(dtype, "Nullable(Int16)"):
            vals.append(_parse_nullable_int(raw, bits=16))
            continue

        # Int32 / Nullable(Int32)
        if _is_type(dtype, "Int32"):
            vals.append(_parse_int_nonnull(raw, bits=32))
            continue
        if _is_type(dtype, "Nullable(Int32)"):
            vals.append(_parse_nullable_int(raw, bits=32))
            continue

        # Strings (LowCardinality(String) / String / Nullable(String))
        if "String" in dtype:
            if raw is None or (isinstance(raw, float) and pd.isna(raw)) or str(raw).strip() == "":
                vals.append(None if is_nullable else "")
            else:
                vals.append(str(raw))
            continue

        # Fallback: deja None/0 según nulabilidad
        vals.append(None if is_nullable else 0)
    return vals

def sort_key(path: Path):
    m = re.match(r"(\\d{4})_(\\d{2})_", path.name)
    if m:
        year, month = int(m.group(1)), int(m.group(2))
        return (year, month, path.name)
    return (9999, 99, path.name)

def insert_values(client: Client, db: str, tb: str, cols: list[str], values: list[tuple]):
    client.execute(f"INSERT INTO {db}.{tb} ({', '.join('`'+c+'`' for c in cols)}) VALUES", values)

def insert_chunk_recursive(client, db, tb, cols, chunk, base_idx, csv_stem, header_out):
    try:
        insert_values(client, db, tb, cols, chunk)
        return (len(chunk), 0)
    except Exception:
        if len(chunk) > SMALL_CHUNK_THRESHOLD:
            mid = len(chunk) // 2
            ok1, fail1 = insert_chunk_recursive(client, db, tb, cols, chunk[:mid], base_idx, csv_stem, header_out)
            ok2, fail2 = insert_chunk_recursive(client, db, tb, cols, chunk[mid:], base_idx + mid, csv_stem, header_out)
            return (ok1 + ok2, fail1 + fail2)
        ok_cnt, fail_cnt = 0, 0
        for off, values in enumerate(chunk, start=0):
            try:
                insert_values(client, db, tb, cols, [values])
                ok_cnt += 1
            except Exception as e_row:
                fail_cnt += 1
                rowno = base_idx + off + 1
                log(f"[FAIL] {csv_stem}.csv fila {rowno}: {e_row}")
                write_failed_row(csv_stem, header_out, list(values))
        return ok_cnt, fail_cnt

def insert_with_chunk_fallback(client, db, tb, cols, all_values, csv_stem, header_out):
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
                break
    return ok_total, fail_total

def main():
    ensure_dirs()
    require_paths()

    client = get_ch_client()
    ensure_db_and_table(client)

    columns_meta = fetch_table_columns(client, CH_DB, CH_TABLE)
    # Excluir columnas computadas del INSERT
    columns_meta_insert = [c for c in columns_meta if not c[3]]
    col_names = [c[0] for c in columns_meta_insert]
    log(f"Columnas en destino ({CH_DB}.{CH_TABLE}): {', '.join(col_names)}")

    for csv_path in sorted(Path(UNPROCESSED_DIR).glob("*.csv"), key=sort_key):
        log(f"Procesando {csv_path.name} …")
        try:
            df = pd.read_csv(csv_path, sep=CSV_SEP, encoding=CSV_ENCODING, dtype=str, low_memory=LOW_MEMORY_READ, header=0)
        except Exception as e:
            log(f"[ERROR] No pude leer el CSV {csv_path.name}: {e}")
            if PROCESSED_DIR:
                move_to_processed(csv_path)
            continue

        df = df.where(pd.notnull(df), None)
        header_out = col_names

        # Normaliza research_year (e.g., '23' -> 2023, '24' -> 2024; seguro hacia adelante)
        if 'research_year' in df.columns:
            df['research_year'] = df['research_year'].apply(_normalize_research_year)

        batch_values = [tuple(row_to_values(row.to_dict(), columns_meta_insert)) for _, row in df.iterrows()]
        total = len(batch_values)

        try:
            client.execute(f"INSERT INTO {CH_DB}.{CH_TABLE} ({', '.join('`'+c+'`' for c in col_names)}) VALUES", batch_values)
            log(f"→ Insertadas {total} filas en bloque exitosamente.")
            if PROCESSED_DIR:
                move_to_processed(csv_path)
            continue
        except Exception as e:
            log(f"[FAIL- BATCH] {csv_path.name}: {e}")
            ok_cnt, fail_cnt = insert_with_chunk_fallback(client, CH_DB, CH_TABLE, col_names, batch_values, csv_path.stem, header_out)
            log(f"→ Tras fallback por bloques, {ok_cnt} filas OK, {fail_cnt} fallidas.")
            if PROCESSED_DIR:
                move_to_processed(csv_path)

    log("Proceso completado latinobarometro (schema fijo).")

if __name__ == "__main__":
    main()
