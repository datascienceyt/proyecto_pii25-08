import os
import re
import requests
from urllib.parse import urlparse

DIRECT_URL = "https://v-dem.net/media/datasets/V-Dem-CY-FullOthers-v15_csv.zip"
OUT_DIR = os.getenv("VDEM_ROOT", "/data/raw/VDEM")
os.makedirs(OUT_DIR, exist_ok=True)

def download_vdem_csv(url=DIRECT_URL, out_dir=OUT_DIR, filename=None, timeout=300):
    os.makedirs(out_dir, exist_ok=True)

    # Si no se provee filename, intenta inferirlo del header o de la URL
    def infer_filename(resp, url):
        cd = resp.headers.get("Content-Disposition", "")
        m = re.search(r'filename\*?=(?:UTF-8\'\')?"?([^";]+)"?', cd)
        if m:
            return m.group(1)
        # fallback: usar el path de la URL
        path = urlparse(resp.url).path  # resp.url por si hubo redirecciones
        base = os.path.basename(path) or "vdem_country_year_v15.zip"
        return base

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.v-dem.net/",
        "Origin": "https://www.v-dem.net",
    }
    with requests.Session() as s:
        r = s.get(url, headers=headers, stream=True, timeout=timeout, allow_redirects=True)
        r.raise_for_status()

        ctype = (r.headers.get("Content-Type") or "").lower()
        if "text/html" in ctype:
            raise RuntimeError("El servidor devolvió HTML en lugar del archivo (Content-Type text/html). ¿Cambió el enlace?")

        fname = filename or infer_filename(r, url)
        out_path = os.path.join(out_dir, fname)

        total = int(r.headers.get("Content-Length", 0))
        chunk = 1 << 20  # 1 MB
        downloaded = 0

        with open(out_path, "wb") as f:
            for part in r.iter_content(chunk_size=chunk):
                if part:
                    f.write(part)
                    downloaded += len(part)
                    if total:
                        pct = downloaded * 100 // total
                        print(f"\rDescargando {fname}: {pct}% ({downloaded}/{total} bytes)", end="")
        if total:
            print()  # salto de línea al terminar

        print("Descarga completa:", out_path)
        return out_path

if __name__ == "__main__":
    print("Iniciando descarga de VDEM...")
    download_vdem_csv()
