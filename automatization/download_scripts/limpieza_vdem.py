import os
import shutil
import zipfile
from pathlib import Path

def main():
    raw_dir = Path(os.getenv("VDEM_ROOT", "data/raw/VDEM"))
    out_dir = Path(os.getenv("VDEM_DATA", "data/VDEM"))
    out_dir.mkdir(parents=True, exist_ok=True)

    if not raw_dir.exists():
        print(f"[WARN] Directorio de entrada no existe: {raw_dir}")
        return

    zips = list(raw_dir.glob("*.zip"))
    if not zips:
        print(f"[INFO] No se encontraron ZIPs en {raw_dir}")
        return

    for zip_path in zips:
        print(f"[INFO] Procesando ZIP: {zip_path}")
        if not zipfile.is_zipfile(zip_path):
            print(f"[WARN] No es un ZIP válido, se omite: {zip_path}")
            continue

        with zipfile.ZipFile(zip_path, "r") as zf:
            members = [m for m in zf.namelist() if m.lower().endswith(".csv")]
            if not members:
                print(f"[INFO] ZIP sin CSVs: {zip_path.name}")
                continue

            for member in members:
                target_name = Path(member).name  # conserva el nombre original del CSV
                target_path = out_dir / target_name
                print(f"  - Extrayendo {member} → {target_path}")
                with zf.open(member) as src, open(target_path, "wb") as dst:
                    shutil.copyfileobj(src, dst)

    print("[DONE] Extracción de VDEM completada.")

if __name__ == "__main__":
    main()
