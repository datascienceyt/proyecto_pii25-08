# Proyecto PII25-8 — Plataforma de Indicadores (ENEMDU, Latinobarómetro, V-Dem)

Sistema orquestado con **Docker Compose** para descargar, limpiar, **ingerir en ClickHouse** y visualizar con **Apache Superset**; con capa web (gateway Node/Express + frontend React) para embeber dashboards con guest tokens.

---

## 📦 Componentes

- **automatic_download**: descarga y limpieza inicial (ENEMDU, Latinobarómetro, V-Dem). Usa rutas de `data/*` y `.env`. Ejecuta `runner.sh`. 
- **clickhouse_server / clickhouse_client**: base y cliente CLI; expone `8123` (HTTP) y `9000` (nativo). Healthcheck `/ping`. 
- **automatic_ingest**: ingesta y derivados (diccionarios, ENEMDU, Latinobarómetro, V-Dem) + logs y errores montados en volúmenes. 
- **superset**: BI/visualización, configurado vía variables `.env`, `SUPERSET_HOME` y scripts de init.
- **gateway** (Node/Express): endpoint `/api/superset/guest-token` con **lista blanca de dashboards** (`ALLOWED_DASHBOARDS`). 
- **react_app** (frontend): embeber dashboards por `UUID`; mapea rutas/páginas a `supersetId`.{index=5}

---

## 📂 Estructura (resumen)

- `.env`, `docker-compose.yml`, `README.md`  
- `automatization/`  
  - `download_scripts/`: `enemdu_descarga.py`, `latinobarometro_descarga.py`, `vdem_descarga.py`, `limpieza_*`, `runner.sh`  
  - `ingest/`: `ingest_*` (persona, vivienda, latinobarómetro, vdem, codigos, geojson), `logs/`, `errors/`  
  - `init-scripts/` (clickhouse y superset)  
- `data/`: `diccionario/`, `enemdu_*`, `latinobarometro/*`, `raw/*` (INEC por año/mes)

> El README previo solo cubría ENEMDU; ahora el alcance incluye Latinobarómetro y V-Dem, más la capa web (gateway + React) y arranque por fases.

---

## ⚙️ Requisitos

- Linux (Ubuntu 20.04+ recomendado), Docker ≥ 20.10, Compose ≥ 1.29, internet, usuario con permisos docker.

---

## 🔐 Variables de entorno (`.env` ejemplo)

```bash
# ClickHouse
CH_USER=admin
CH_PASSWORD=ContrasenaSegura
CH_DATABASE=indicadores

# Superset
DATABASE_DIALECT=clickhouse
DATABASE_HOST=clickhouse_server
DATABASE_PORT=8123
DATABASE_DB=${CH_DATABASE}
DATABASE_USER=${CH_USER}
DATABASE_PASSWORD=${CH_PASSWORD}
SUPERSET_USER=admin
SUPERSET_PASS=CambiaEstaClave

# Web (gateway + frontend)
SUPERSET_URL=http://localhost:8088
ALLOWED_DASHBOARDS=UUID_GENERAL,UUID_VDEM,UUID_LATINO,UUID_ENEMDU
