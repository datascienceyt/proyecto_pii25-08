#!/usr/bin/env python3
import os
import re
import csv
import shutil
import zipfile
from pathlib import Path
from typing import Optional, Dict

import pandas as pd

RAW_ROOT   = Path(os.getenv("LATINOBAROMETRO_ROOT", "data/raw/latinobarometro"))
UNPROC_DTA = Path(os.getenv("LATINOBAROMETRO_UNPROC_DTA", "data/latinobarometro/unprocessed_dta"))
UNPROC_CSV = Path(os.getenv("LATINOBAROMETRO_UNPROC_CSV", "data/latinobarometro/unprocessed_csv"))
NORM_CSV   = Path(os.getenv("LATINOBAROMETRO_NORM_CSV", "data/latinobarometro/normalized_csv"))
PROC_CSV   = Path(os.getenv("LATINOBAROMETRO_PROCESSED", "data/latinobarometro/processed"))
DICT_CSV   = Path(os.getenv("LATINOBAROMETRO_DICT_CSV", "data/latinobarometro/latinobarometro_glossary_candidates_BM.csv"))

YEAR_RX = re.compile(r"(19|20)\d{2}")

def ensure_dirs(*dirs: Path):
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)

def extract_year_from_name(name: str) -> Optional[int]:
    m = YEAR_RX.search(name)
    return int(m.group(0)) if m else None

def read_csv_semicolon(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path, sep=";", dtype=str)
    except UnicodeDecodeError:
        return pd.read_csv(path, sep=";", dtype=str, encoding="latin-1")

def safe_rename(df: pd.DataFrame, rename_map: Dict[str, str]) -> pd.DataFrame:
    new_cols = []
    target_counts = {}
    for col in df.columns:
        tgt = rename_map.get(col, col)
        count = target_counts.get(tgt, 0)
        if count == 0:
            new_cols.append(tgt)
        else:
            new_cols.append(f"{tgt}__dup{count+1}")
        target_counts[tgt] = count + 1
    df2 = df.copy()
    df2.columns = new_cols
    return df2

def iter_year_dirs(root: Path):
    for p in sorted(root.iterdir()):
        if p.is_dir():
            yield p

def build_year_to_map(dict_csv: Path) -> Dict[str, Dict[str, str]]:
    if not dict_csv.exists():
        raise FileNotFoundError(f"No se encontró el diccionario: {dict_csv}")
    dic = read_csv_semicolon(dict_csv).fillna("")
    required_cols = {"year","question","normalization"}
    missing = required_cols - set(c.lower() for c in dic.columns)
    if missing:
        raise ValueError(f"Al diccionario le faltan columnas requeridas: {missing}")
    dic.columns = [c.lower() for c in dic.columns]
    dic["year"] = dic["year"].astype(str).str.strip()
    dic["question"] = dic["question"].astype(str).str.strip().str.lower()
    dic["normalization"] = dic["normalization"].astype(str).str.strip()
    year_to_map: Dict[str, Dict[str, str]] = {}
    for y, g in dic.groupby("year"):
        year_to_map[y] = {q: n for q, n in zip(g["question"], g["normalization"])}
    return year_to_map

def process_zip_tree():
    if not RAW_ROOT.exists():
        print(f"[WARN] Directorio raíz de raw no existe: {RAW_ROOT}")
        return

    ensure_dirs(UNPROC_DTA, UNPROC_CSV, NORM_CSV)

    year_to_map = build_year_to_map(DICT_CSV)
    print(f"[INFO] Años en diccionario: {sorted(year_to_map.keys())[:10]}{' ...' if len(year_to_map)>10 else ''}")

    for year_dir in iter_year_dirs(RAW_ROOT):
        year = year_dir.name
        print(f"[INFO] Año: {year} | Carpeta: {year_dir}")

        counter = 0
        zip_files = sorted(year_dir.rglob("*.zip"))
        if not zip_files:
            print(f"  [INFO] Sin ZIPs en {year_dir}")
            continue

        for zip_path in zip_files:
            if not zipfile.is_zipfile(zip_path):
                print(f"  [WARN] No es un ZIP válido, se omite: {zip_path}")
                continue

            print(f"  [INFO] Procesando ZIP: {zip_path.name}")
            with zipfile.ZipFile(zip_path, "r") as zf:
                dta_members = []
                for m in zf.namelist():
                    m_lower = m.lower()
                    if m_lower.endswith(".dta"):
                        base = os.path.basename(m_lower)
                        if "eng" in base:
                            dta_members.append(m)

                if not dta_members:
                    print(f"    [INFO] ZIP sin STATA 'eng': {zip_path.name}")
                    continue

                for member in dta_members:
                    try_year = extract_year_from_name(zip_path.name) or extract_year_from_name(member) or extract_year_from_name(year)
                    year_str = str(try_year) if try_year else year

                    counter += 1
                    base_name = f"latinobarometro_{year_str}"
                    suffix = "" if counter == 1 else f"_{counter}"
                    dta_name = f"{base_name}{suffix}.dta"
                    csv_name = f"{base_name}{suffix}.csv"

                    dta_unproc_target = UNPROC_DTA / dta_name
                    csv_proc_target   = UNPROC_CSV / csv_name
                    csv_norm_target   = NORM_CSV / csv_name
                    csv_inget_target   = PROC_CSV / csv_name

                    # 0) ¿Existe el DTA?, sino se extrae
                    if dta_unproc_target.exists():
                        print(f"    [SKIP] Ya existe DTA en 'unprocessed': {dta_unproc_target.name}")
                    else:
                        print(f"    - Extrayendo {member} → {dta_unproc_target}")
                        with zf.open(member) as src, open(dta_unproc_target, "wb") as dst:
                            shutil.copyfileobj(src, dst)
                    # 1) ¿Ya está en BD?
                    if csv_inget_target.exists():
                        print(f"      [SKIP] Ya en base de datos (processed): {csv_inget_target.name}")
                        continue
                    # 2) ¿Ya está normalizado?
                    if csv_norm_target.exists():
                        print(f"    [SKIP] Ya normalizado, pendiente de ingesta: {csv_norm_target.name}")
                        continue
                    # 3) ¿Ya está convertido sin normalizar?
                    if csv_proc_target.exists():
                        print(f"      [SKIP] CSV sin normalizar ya existe: {csv_proc_target.name}")
                        # Aquí NO conviertes de nuevo, y dejas que otro paso haga la normalización
                        continue
                    else:
                        try:
                            print(f"      · Convirtiendo a CSV: {csv_proc_target.name}")
                            df = pd.read_stata(dta_unproc_target, convert_categoricals=False)
                            csv_proc_target.parent.mkdir(parents=True, exist_ok=True)
                            df.to_csv(csv_proc_target, index=False, sep=';', encoding='utf-8')
                        except Exception as e:
                            print(f"      [ERROR] Falló la conversión de {dta_unproc_target.name}: {e}")
                            continue

                    ykey = year_str
                    if ykey not in year_to_map:
                        print(f"      [SKIP] Año {ykey} no está en el diccionario: {csv_proc_target.name}")
                        try:
                            df_passthrough = read_csv_semicolon(csv_proc_target)
                            df_passthrough.to_csv(csv_norm_target, index=False, sep=';', encoding='utf-8')
                            print(f"      [COPY] Guardado sin renombrar: {csv_norm_target.name}")
                        except Exception as e:
                            print(f"      [ERROR] No se pudo copiar sin cambios: {e}")
                        continue

                    try:
                        df_in = read_csv_semicolon(csv_proc_target).fillna("")
                        qmap = year_to_map[ykey]
                        lower_cols = {c.lower(): c for c in df_in.columns}
                        rename_map = {}
                        applied = 0
                        for q_lower, norm_name in qmap.items():
                            if q_lower in lower_cols:
                                orig = lower_cols[q_lower]
                                rename_map[orig] = norm_name
                                applied += 1
                        df_out = safe_rename(df_in, rename_map)
                        df_out.to_csv(csv_norm_target, index=False, sep=';', encoding='utf-8')
                        print(f"      [OK] Normalizado: {csv_norm_target.name} | columnas renombradas: {applied}")
                    except Exception as e:
                        print(f"      [ERROR] Falló el renombrado/guardado de {csv_proc_target.name}: {e}")
                        continue

    print("[DONE] Pipeline Latinobarómetro completado.")

if __name__ == '__main__':
    process_zip_tree()
