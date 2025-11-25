import os
import time
import re
import requests
from urllib.parse import urlparse


BASE = "https://www.latinobarometro.org/documents"
OUT_ROOT = os.getenv("LATINOBAROMETRO_ROOT", "/data/raw/LATINOBAROMETRO")
os.makedirs(OUT_ROOT, exist_ok=True)
COUNTRY_SLUG = "ecuador"  # cambia si necesitas otro país

# Plantillas base (según convención "normal")
# URL_TEMPLATES = [
#     f"{BASE}/LAT-{{year}}/latinobarometro-{{year}}-{COUNTRY_SLUG}-csv-esp-v1.zip",
#     f"{BASE}/LAT-{{year}}/latinobarometro-libro-de-codigos-{COUNTRY_SLUG}-{{year}}.pdf",
#     f"{BASE}/LAT-{{year}}/latinobarometro-{{year}}-resultados-por-sexo-y-edad-{COUNTRY_SLUG}-{{year}}.pdf",
# ]
URL_TEMPLATES = [
    # Data
    f"{BASE}/LAT-{{year}}/latinobarometro-{{year}}-dta.zip",
    # Codebook
    f"{BASE}/LAT-{{year}}/latinobarometro-{{year}}-codebook-v20190707.pdf",
]

# Overrides: a partir del 2018 se cambió de "dta" a "stata" usando diferentes nombres
# En 2024 ya no aparece el codebook, se descargan los resultados
YEAR_OVERRIDES = {
    2010: [
        # Data
        f"{BASE}/LAT-2010/latinobarometro-2010-dta.zip",
        # Codebook
        f"{BASE}/LAT-2010/latinobarometro-2010-codebook-10-07-2019.pdf",
    ],
    2016: [
        # Data
        f"{BASE}/LAT-2016/latinobarometro2016-dta.zip",
        # Codebook
        f"{BASE}/LAT-2016/latinobarometro-2016-codebook-v20190707.pdf",
    ],
    2017: [
        # Data
        f"{BASE}/LAT-2017/latinobarometro2017-dta.zip",
        # Codebook
        f"{BASE}/LAT-2017/latinobarometro-2017-codebook-v20190707.pdf",
    ],
    2018: [
        # Data
        f"{BASE}/LAT-2018/latinobarometro-2018-eng-stata-v20190303.zip",
        # Codebook
        f"{BASE}/LAT-2018/latinobarometro-2018-codebook-v20190707.pdf",
    ],
    2020: [
        # Data
        f"{BASE}/LAT-2020/latinobarometro-2020-esp-stata-v1-0.zip",
        # Codebook
        f"{BASE}/LAT-2020/latinobarometro-2020-codebook.pdf",
        
    ],
    2023: [
        # Data
        f"{BASE}/LAT-2023/latinobarometro-2023-stata-v1-0.zip",
        # Codebook
        f"{BASE}/LAT-2023/latinobarometro-2023-codebook.pdf",
    ],
    2024: [
        # Data
        f"{BASE}/LAT-2024/latinobarometro-2024-stata-v20250817.zip",
        # Results
        f"{BASE}/LAT-2024/latinobarometro-2024-results-by-country.pdf",
    ],
}

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://www.latinobarometro.org/",
    "Origin": "https://www.latinobarometro.org",
}

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def infer_filename(resp, url: str, fallback: str = None) -> str:
    """Intenta obtener el filename desde Content-Disposition; si no, usa el path."""
    cd = resp.headers.get("Content-Disposition", "")
    m = re.search(r'filename\*?=(?:UTF-8\'\')?"?([^";]+)"?', cd)
    if m:
        return m.group(1)
    name = os.path.basename(urlparse(resp.url).path)  # resp.url por si hubo redirects
    if not name and fallback:
        return fallback
    return name or "download.bin"

def download_if_exists(url: str, out_dir: str, timeout: int = 120) -> bool:
    """
    Intenta descargar 'url' a 'out_dir'.
    True si descargó algo (o ya existía); False si NO existe (404/HTML/error).
    """
    guessed_name = os.path.basename(urlparse(url).path) or None
    if guessed_name:
        guessed_path = os.path.join(out_dir, guessed_name)
        if os.path.exists(guessed_path) and os.path.getsize(guessed_path) > 0:
            print(f"  - Ya existe: {guessed_name}, omitiendo.")
            return True

    try:
        with requests.Session() as s:
            r = s.get(url, headers=HEADERS, stream=True, timeout=timeout, allow_redirects=True)
            if r.status_code == 404:
                print(f"  - 404: {url}")
                return False
            r.raise_for_status()

            ctype = (r.headers.get("Content-Type") or "").lower()
            if "text/html" in ctype:
                print(f"  - HTML en lugar de archivo: {url}")
                return False

            fname = infer_filename(r, url, fallback=guessed_name)
            if not fname:
                print(f"  - No se pudo inferir el nombre para: {url}")
                return False

            out_path = os.path.join(out_dir, fname)
            if os.path.exists(out_path) and os.path.getsize(out_path) > 0:
                print(f"  - Ya existe: {fname}, omitiendo.")
                return True

            chunk = 1 << 20  # 1 MB
            downloaded = 0
            with open(out_path, "wb") as f:
                for part in r.iter_content(chunk_size=chunk):
                    if part:
                        f.write(part)
                        downloaded += len(part)

            if os.path.getsize(out_path) == 0:
                print(f"  - Archivo vacío, borrando: {fname}")
                try:
                    os.remove(out_path)
                except Exception:
                    pass
                return False

            print(f"  - OK: {fname} ({downloaded} bytes)")
            return True

    except requests.RequestException as e:
        print(f"  - Error de red: {e}")
        return False
    except Exception as e:
        print(f"  - Error: {e}")
        return False

def build_urls_for_year(year: int):
    """
    Devuelve la lista de URLs a probar para ese año:
    1) Overrides específicos del año (si existen)
    2) Plantillas estándar
    Deduplica preservando el orden.
    """
    candidates = []
    seen = set()

    # 1) Overrides
    for u in YEAR_OVERRIDES.get(year, []):
        if u not in seen:
            candidates.append(u)
            seen.add(u)

    # 2) Plantillas estándar
    for tpl in URL_TEMPLATES:
        u = tpl.format(year=year)
        if u not in seen:
            candidates.append(u)
            seen.add(u)

    return candidates

def crawl_years(start_year: int = 1996, max_year: int = 2100, stop_after_consecutive_misses: int = 2, sleep_secs: float = 0.5):
    """
    Recorre años desde start_year a max_year. Se detiene
    cuando haya 'stop_after_consecutive_misses' años seguidos sin ningún archivo.
    """
    ensure_dir(OUT_ROOT)
    misses = 0

    for year in range(start_year, max_year + 1):
        year_dir = os.path.join(OUT_ROOT, str(year))
        ensure_dir(year_dir)
        print(f"\nAño {year}:")

        urls = build_urls_for_year(year)
        # Intentamos conseguir al menos uno de cada “tipo lógico”:
        # csv/zip, codebook pdf, resultados pdf (ordenados tal como los generamos)
        found_any = False

        # Descargamos todos los candidatos para ese año (así cubrimos overrides + plantillas)
        # Puedes cambiar a “parar al encontrar 1 por tipo” si lo prefieres.
        for u in urls:
            ok = download_if_exists(u, year_dir)
            time.sleep(sleep_secs)
            found_any = found_any or ok

        if found_any:
            print(f"✔ Descargas para {year} completadas.")
            misses = 0
        else:
            print(f"✖ No se encontró ningún archivo para {year}.")
            misses += 1
            if misses >= stop_after_consecutive_misses:
                print(f"\nNo se encontraron archivos en {misses} años consecutivos. Deteniendo el proceso.")
                break

if __name__ == "__main__":
    print("Iniciando descarga de Latinobarometro...")
    crawl_years(start_year=1995, max_year=2100, stop_after_consecutive_misses=4, sleep_secs=0.4)
