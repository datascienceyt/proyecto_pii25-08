#!/usr/bin/env python3
# limpieza_vivienda.py
# Extrae y copia sólo CSV nuevos de vivienda a unprocessed, omitiendo los que ya existan en processed o unprocessed.

import os
import re
import shutil
import zipfile
import tempfile
from pathlib import Path

# ─── CONFIGURACIÓN vía ENV ───
BASE_DIR = Path(os.getenv("ENEMDU_ROOT", "/data/raw/ENEMDU"))
UNPROCESSED_DIR = Path(os.getenv("VIVIENDA_UNPROC", "/data/enemdu_vivienda/unprocessed"))
PROCESSED_DIR = Path(os.getenv("VIVIENDA_PROCESSED", "/data/enemdu_vivienda/processed"))

# Asegura existencia de carpetas
for d in (UNPROCESSED_DIR, PROCESSED_DIR):
    d.mkdir(parents=True, exist_ok=True)

def es_recalculado(p: Path) -> bool:
    return "recalculado" in str(p).lower()

# Lista de raw procesados (nombres sin prefijo)
processed_raw = {p.name for p in PROCESSED_DIR.glob("*.csv")}

# Coincidir archivos vivienda
vivienda_regex = re.compile(r'(vivienda|viv).*\.csv$', re.IGNORECASE)

# ─────────────────── FUNCIONES ───────────────────

def match_csv_vivienda(filename: str) -> bool:
    """
    Devuelve True si el CSV de vivienda debe copiarse:
      - Contiene 'vivienda' o 'viv'
      - NO contiene 'bdd'
      - NO contiene 'tics'
    """
    lower = filename.lower()
    if not vivienda_regex.search(lower):
        return False
    if 'bdd' in lower:
        return False
    if 'tics' in lower:
        return False
    return True


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
    """Extrae zip (y zips internos) en temp_dir; continúa si hay corrupción."""
    if not zipfile.is_zipfile(zip_path):
        print(f"⚠️  No es ZIP válido → {zip_path.name}")
        return

    try:
        with zipfile.ZipFile(zip_path, 'r') as zf:
            zf.extractall(temp_dir)
    except Exception as e:
        print(f"⚠️  Falló extracción de {zip_path.name}: {e}")
        return

    # Detectar y extraer zips anidados en cualquier subdirectorio
    for nested_zip in temp_dir.rglob('*.zip'):
        subdir = nested_zip.with_suffix('')
        subdir.mkdir(parents=True, exist_ok=True)
        extraer_zip_recursivo(nested_zip, subdir)


# ─────────────────── PROCESAMIENTO ───────────────────
for year_dir in sorted(BASE_DIR.iterdir()):
    if not year_dir.is_dir():
        continue
    year = year_dir.name

    for period_dir in sorted(year_dir.iterdir()):
        if not period_dir.is_dir():
            continue
        period = period_dir.name
        print(f"\n📂 Revisando {year}/{period}")

        # 1) CSV sueltos en cualquier subdirectorio
        for csv_file in period_dir.rglob('*.csv'):
            if match_csv_vivienda(csv_file.name):
                copiar_csv(csv_file, year, period)

        # 2) Procesar todos los zips en cualquier subdirectorio
        zip_files = sorted(period_dir.rglob("*.zip"), key=lambda p: (es_recalculado(p), p.name.lower()))
        for zip_file in zip_files:
            print(f"📦 Procesando ZIP → {zip_file.relative_to(period_dir)}")
            with tempfile.TemporaryDirectory() as tmp:
                tmp_path = Path(tmp)
                extraer_zip_recursivo(zip_file, tmp_path)
                # Copiar CSV extraídos que cumplan criterios
                for csv_ex in tmp_path.rglob('*.csv'):
                    if match_csv_vivienda(csv_ex.name):
                        copiar_csv(csv_ex, year, period)

print("\n✅ Proceso completado. Los CSV de VIVIENDA están en:", UNPROCESSED_DIR)