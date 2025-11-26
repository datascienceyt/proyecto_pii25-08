#!/usr/bin/env python3
# limpieza_persona.py
# Extrae y copia sólo CSV nuevos a unprocessed, omitiendo los que ya existan en processed o unprocessed.

import os
import re
import shutil
import zipfile
import tempfile
from pathlib import Path

# ─── CONFIGURACIÓN vía ENV ───
BASE_DIR = Path(os.getenv("ENEMDU_ROOT", "/data/raw/ENEMDU"))
UNPROCESSED_DIR = Path(os.getenv("PERSONA_UNPROC", "/data/enemdu_persona/unprocessed"))
PROCESSED_DIR = Path(os.getenv("PERSONA_PROCESSED", "/data/enemdu_persona/processed"))

# Asegura existencia de carpetas
for d in (UNPROCESSED_DIR, PROCESSED_DIR):
    d.mkdir(parents=True, exist_ok=True)

# Patrones para distinguir CSV de persona(s)
regex_personas = re.compile(r'personas.*\.csv$', re.IGNORECASE)
regex_persona = re.compile(r'persona(?!s).*\.csv$', re.IGNORECASE)

# Lista de raw procesados (nombres sin prefijo)
processed_raw = {p.name for p in PROCESSED_DIR.glob("*.csv")}

def match_csv(filename: str, year: int) -> bool:
    """
    Devuelve True si el nombre de archivo debe copiarse,
    según las reglas:
      - <=2019: solo 'personas'
      - >=2020: solo 'persona' y NO contener 'tics'
    """
    lower = filename.lower()
    if year <= 2018:
        return bool(regex_personas.search(lower))
    elif year == 2019:
        return bool(regex_personas.search(lower)) or bool(regex_persona.search(lower))
    elif year >= 2020:
        return bool(regex_persona.search(lower)) and ('tics' not in lower)

def es_recalculado(p: Path) -> bool:
    return "recalculado" in str(p).lower()

def copiar_csv(src: Path, year: str, period: str):
    nombre_dst = f"{year}_{period.replace(' ', '_')}_{src.name}"
    dst = UNPROCESSED_DIR / nombre_dst
    chk = PROCESSED_DIR / nombre_dst
    if chk.exists():
        print(f"⚠️  Ya existe (omitido): {chk.name}")
        return
    
    try:
        shutil.copy(src, dst)
        print(f"   ✔ Copiado: {dst.name}")
    except Exception as e:
        print(f"   ❌ Error copiando {src.name}: {e}")

def extraer_zip_recursivo(zip_path: Path, temp_dir: Path):
    if not zipfile.is_zipfile(zip_path):
        print(f"⚠️  No es ZIP válido → {zip_path.name}")
        return
    try:
        with zipfile.ZipFile(zip_path, "r") as zf:
            zf.extractall(temp_dir)
    except Exception as e:
        print(f"⚠️  Falló extracción de {zip_path.name}: {e}")
        return
    # extraemos zips anidados
    for nested in temp_dir.rglob("*.zip"):
        subdir = nested.with_suffix('')
        subdir.mkdir(parents=True, exist_ok=True)
        extraer_zip_recursivo(nested, subdir)

# --- Procesamiento principal ---
for year_dir in sorted(BASE_DIR.iterdir()):
    if not year_dir.is_dir():
        continue

    # Accept only 4-digit year directories, e.g. "2018", "2025"
    if not (year_dir.name.isdigit() and len(year_dir.name) == 4):
        print(f"⚠️ Skipping non-year directory: {year_dir.name}")
        continue

    year = int(year_dir.name)

    for period_dir in sorted(year_dir.iterdir()):
        if not period_dir.is_dir():
            continue
        period = period_dir.name
        print(f"\n📂 Revisando {year}/{period}")

        # 1) CSV files in any level
        for csv_file in period_dir.rglob("*.csv"):
            if match_csv(csv_file.name, year):
                copiar_csv(csv_file, year_dir.name, period)

        zip_files = sorted(
            period_dir.rglob("*.zip"),
            key=lambda p: (es_recalculado(p), p.name.lower())
        )
        # 2) ZIP files in any level
        for zip_file in zip_files:
            print(f"📦 Procesando ZIP → {zip_file.relative_to(period_dir)}")
            with tempfile.TemporaryDirectory() as tmp:
                tmp_path = Path(tmp)
                extraer_zip_recursivo(zip_file, tmp_path)
                # copy extracted CSV files
                for csv_ex in tmp_path.rglob("*.csv"):
                    if match_csv(csv_ex.name, year):
                        copiar_csv(csv_ex, year_dir.name, period)

print("\n✅ Proceso completado. Los CSV válidos están en:", UNPROCESSED_DIR)