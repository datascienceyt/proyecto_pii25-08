#!/usr/bin/env python3
import os
import csv
import time
from pathlib import Path
from datetime import datetime, date
import pandas as pd
from clickhouse_driver import Client, errors

VDEM_DATA       = os.getenv("VDEM_DATA", "/data/VDEM")
LOG_DIR        = os.getenv("LOG_DIR", "/ingest/logs")
ERR_DIR        = os.getenv("ERR_DIR", "/ingest/errors")

CH_HOST        = os.getenv("CH_HOST", "clickhouse_server")
CH_PORT        = int(os.getenv("CH_PORT", 9000))
CH_USER        = os.getenv("CH_USER", "admin")
CH_PASSWORD    = os.getenv("CH_PASSWORD", "secret_pw")
CH_DATABASE    = os.getenv("CH_DATABASE", "indicadores")
CH_TABLE       = os.getenv("CH_TABLE", "vdem")

MAX_RETRIES    = int(os.getenv("MAX_RETRIES", 12))
RETRY_DELAY    = int(os.getenv("RETRY_DELAY", 5))
STOP_ON_ERROR  = os.getenv("STOP_ON_ERROR", "false").lower() in ("1","true","yes")
BATCH_SIZE     = int(os.getenv("BATCH_SIZE", 50000))
SMALL_THRESHOLD= int(os.getenv("SMALL_THRESHOLD", 256))

CSV_SEP        = ","
CSV_ENCODING   = "utf-8"
LOW_MEMORY     = False

SCHEMA = [
    ("country_name", "String"),
    ("country_text_id", "String"),
    ("country_id", "Int32"),
    ("year", "Int32"),
    ("historical_date", "Date"),
    ("project", "Int32"),
    ("historical", "Int32"),
    ("histname", "String"),
    ("codingstart", "Int32"),
    ("codingend", "Int32"),
    ("codingstart_contemp", "Int32"),
    ("codingend_contemp", "Int32"),
    ("codingstart_hist", "Nullable(Int32)"),
    ("codingend_hist", "Nullable(Int32)"),
    ("gapstart1", "Nullable(String)"),
    ("gapstart2", "Nullable(String)"),
    ("gapstart3", "Nullable(String)"),
    ("gapend1", "Nullable(String)"),
    ("gapend2", "Nullable(String)"),
    ("gapend3", "Nullable(String)"),
    ("gap_index", "Int32"),
    ("COWcode", "Int32"),
    ("v2x_polyarchy", "Float64"),
    ("v2x_libdem", "Float64"),
    ("v2x_partipdem", "Float64"),
    ("v2x_delibdem", "Nullable(Float64)"),
    ("v2x_egaldem", "Nullable(Float64)"),
    # ("v2x_api", "Float64"),
    # ("v2x_mpi", "Float64"),
    ("v2x_freexp_altinf", "Float64"),
    ("v2xel_frefair", "Float64"),
    # ("v2x_liberal", "Float64"),
    ("v2xcl_rol", "Float64"),
    ("v2x_jucon", "Float64"),
    ("v2xlg_legcon", "Nullable(Float64)"),
    # ("v2x_partip", "Float64"),
    ("v2xeg_eqprotec", "Float64"),
    ("v2xeg_eqaccess", "Float64"),
    ("v2xeg_eqdr", "Nullable(Float64)"),
    ("v2pepwrses", "Float64"),
    ("v2pepwrsoc", "Float64"),
    ("v2pepwrgen", "Float64"),
    ("v2pepwrort", "Float64"),
    ("v2pepwrgeo", "Float64"),
]

ORDER_BY = "(country_id, year)"

PD_DTYPES = {
    "country_name": "string",
    "country_text_id": "string",
    "country_id": "Int32",
    "year": "Int32",
    "historical_date": "string",
    "project": "Int32",
    "historical": "Int32",
    "histname": "string",
    "codingstart": "Int32",
    "codingend": "Int32",
    "codingstart_contemp": "Int32",
    "codingend_contemp": "Int32",
    "codingstart_hist": "Int32",
    "codingend_hist": "Int32",
    "gapstart1": "string",
    "gapstart2": "string",
    "gapstart3": "string",
    "gapend1": "string",
    "gapend2": "string",
    "gapend3": "string",
    "gap_index": "Int32",
    "COWcode": "Int32",
    "v2x_polyarchy": "float64",
    "v2x_libdem": "float64",
    "v2x_partipdem": "float64",
    "v2x_delibdem": "float64",
    "v2x_egaldem": "float64",
    # "v2x_api": "float64",
    # "v2x_mpi": "float64",
    "v2x_freexp_altinf": "float64",
    "v2xel_frefair": "float64",
    # "v2x_liberal": "float64",
    "v2xcl_rol": "float64",
    "v2x_jucon": "float64",
    "v2xlg_legcon": "float64",
    # "v2x_partip": "float64",
    "v2xeg_eqprotec": "float64",
    "v2xeg_eqaccess": "float64",
    "v2xeg_eqdr": "float64",
    "v2pepwrses": "float64",
    "v2pepwrsoc": "float64",
    "v2pepwrgen": "float64",
    "v2pepwrort": "float64",
    "v2pepwrgeo": "float64",
}

USECOLS = [name for name, _ in SCHEMA]

def log(msg: str):
    ts = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts} UTC] {msg}", flush=True)

def ensure_dirs():
    for d in (LOG_DIR, ERR_DIR):
        Path(d).mkdir(parents=True, exist_ok=True)

def get_client():
    last = None
    for i in range(MAX_RETRIES):
        try:
            c = Client(host=CH_HOST, port=CH_PORT, user=CH_USER, password=CH_PASSWORD, database=CH_DATABASE)
            c.execute("SELECT 1")
            log("[OK] Conectado a ClickHouse")
            return c
        except Exception as e:
            last = e
            log(f"[WARN] Conexión fallida ({i+1}/{MAX_RETRIES}): {e}. Reintento en {RETRY_DELAY}s…")
            time.sleep(RETRY_DELAY)
    raise RuntimeError(f"No pude conectar a ClickHouse: {last}")

def ensure_db_and_table(client: Client):
    """
    Crea la base de datos si no existe y
    SIEMPRE elimina y recrea la tabla VDEM.
    """
    client.execute(f"CREATE DATABASE IF NOT EXISTS {CH_DATABASE}")
    # 💣 Drop de la tabla para que cada ingesta sea limpia
    client.execute(f"DROP TABLE IF EXISTS {CH_DATABASE}.{CH_TABLE}")

    cols = ",\n    ".join(f"`{n}` {t}" for n, t in SCHEMA)
    ddl = f"""
    CREATE TABLE {CH_DATABASE}.{CH_TABLE} (
        {cols}
    )
    ENGINE = MergeTree
    ORDER BY {ORDER_BY}
    """
    client.execute(ddl)
    log(f"[OK] Tabla {CH_DATABASE}.{CH_TABLE} recreada (DROP + CREATE).")

def parse_date_ymd(val):
    if val is None:
        return None
    s = str(val).strip()
    if not s:
        return None
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%d/%m/%Y", "%m/%d/%Y", "%Y"):
        try:
            dt = datetime.strptime(s, fmt)
            if fmt == "%Y":
                return date(dt.year, 1, 1)
            return dt.date()
        except Exception:
            continue
    try:
        dt = pd.to_datetime(s, errors="coerce")
        if pd.isna(dt):
            return None
        return dt.date()
    except Exception:
        return None

def to_int(v, nullable=False):
    if v is None or (isinstance(v, float) and pd.isna(v)) or (isinstance(v, str) and v == ""):
        return None if nullable else 0
    try:
        return int(v)
    except Exception:
        return None if nullable else 0

def to_float(v, nullable=False):
    if v is None or (isinstance(v, float) and pd.isna(v)) or (isinstance(v, str) and v == ""):
        return None if nullable else 0.0
    try:
        return float(v)
    except Exception:
        return None if nullable else 0.0

def to_str(v, nullable=False):
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return None if nullable else ""
    s = str(v)
    return s if s != "" else (None if nullable else "")

def build_row(df_row: dict):
    out = []
    for name, ch_type in SCHEMA:
        v = df_row.get(name, None)
        if ch_type == "Date":
            out.append(parse_date_ymd(v) or date(1970,1,1))
        elif ch_type.startswith("Nullable(Int"):
            out.append(to_int(v, nullable=True))
        elif ch_type == "Int32":
            out.append(to_int(v, nullable=False))
        elif ch_type.startswith("Nullable(Float"):
            out.append(to_float(v, nullable=True))
        elif ch_type == "Float64":
            out.append(to_float(v, nullable=False))
        elif ch_type.startswith("Nullable(String)"):
            out.append(to_str(v, nullable=True))
        elif ch_type == "String":
            out.append(to_str(v, nullable=False))
        else:
            out.append(v)
    return tuple(out)

def insert_values(client: Client, rows):
    cols = ", ".join(f"`{n}`" for n, _ in SCHEMA)
    client.execute(f"INSERT INTO {CH_DATABASE}.{CH_TABLE} ({cols}) VALUES", rows)

def insert_chunk_recursive(client, chunk, base_index):
    try:
        insert_values(client, chunk)
        return (len(chunk), 0)
    except Exception:
        if len(chunk) > SMALL_THRESHOLD:
            mid = len(chunk) // 2
            ok1, fail1 = insert_chunk_recursive(client, chunk[:mid], base_index)
            ok2, fail2 = insert_chunk_recursive(client, chunk[mid:], base_index + mid)
            return (ok1 + ok2, fail1 + fail2)
        ok, fail = 0, 0
        for i, row in enumerate(chunk):
            try:
                insert_values(client, [row])
                ok += 1
            except Exception as e:
                fail += 1
                fail_csv = Path(ERR_DIR) / "vdem_failed_rows.csv"
                write_header = not fail_csv.exists()
                with fail_csv.open("a", newline="", encoding="utf-8") as f:
                    w = csv.writer(f)
                    if write_header:
                        w.writerow([n for n, _ in SCHEMA])
                    w.writerow(list(row))
        return ok, fail

def main():
    ensure_dirs()

    if not VDEM_DATA:
        raise RuntimeError("Define VDEM_DATA con la ruta al directorio o archivo CSV de V-Dem.")
    
    vdem_path = Path(VDEM_DATA)
    
    if vdem_path.is_dir():
        candidates = sorted(vdem_path.glob("*.csv")) + sorted(vdem_path.glob("*.csv.gz"))
        if not candidates:
            raise FileNotFoundError(f"No se encontró ningún CSV en {vdem_path}")
        csv_path = max(candidates, key=lambda p: p.stat().st_mtime)
    elif vdem_path.is_file():
        csv_path = vdem_path
    else:
        raise FileNotFoundError(f"La ruta {vdem_path} no existe")

    client = get_client()
    ensure_db_and_table(client)

    log(f"[INFO] Leyendo CSV: {csv_path}")
    df = pd.read_csv(
        csv_path,
        sep=CSV_SEP,
        encoding=CSV_ENCODING,
        dtype=PD_DTYPES,
        usecols=[n for n,_ in SCHEMA],
        low_memory=LOW_MEMORY,
    )

    if "historical_date" in df.columns:
        df["historical_date"] = df["historical_date"].apply(parse_date_ymd)

    df = df.where(pd.notnull(df), None)
    total = len(df)
    log(f"[INFO] Filas leídas: {total} | Columnas usadas: {len(SCHEMA)}")

    ok_total, fail_total = 0, 0
    for start in range(0, total, BATCH_SIZE):
        end = min(start + BATCH_SIZE, total)
        batch_df = df.iloc[start:end]
        rows = [build_row(dict(r)) for _, r in batch_df.iterrows()]
        try:
            insert_values(client, rows)
            ok_total += len(rows)
        except Exception:
            ok, fail = insert_chunk_recursive(client, rows, base_index=start)
            ok_total += ok
            fail_total += fail
            if STOP_ON_ERROR and fail > 0:
                log(f"[STOP] Errores en batch {start}-{end}, deteniendo por STOP_ON_ERROR.")
                break
        log(f"[BATCH] {start}-{end}: OK={ok_total} FAIL={fail_total}")

    log(f"[DONE] V-Dem insertadas: OK={ok_total}, FAIL={fail_total}")

def write_failed_row(header, values):
    fail_csv = Path(ERR_DIR) / "vdem_failed_rows.csv"
    write_header = not fail_csv.exists()
    with fail_csv.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if write_header:
            w.writerow(header)
        w.writerow(values)

if __name__ == "__main__":
    main()
