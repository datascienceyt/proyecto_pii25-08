## Proyecto Democracia YACHAY – Plataforma de Indicadores

Plataforma analítica para estudiar los efectos de la desigualdad socioeconómica en la percepción de la democracia en Latinoamérica (1995–2023).

La solución integra:

* **Capa de datos**: descarga automática, limpieza e ingesta de:

  * ENEMDU (Ecuador, personas y viviendas/hogares).
  * Latinobarómetro.
  * V-Dem.
* **Base de datos analítica**: ClickHouse, con tablas normalizadas y vistas de indicadores para empleo, pobreza, NBI, IPM y democracia.
* **Capa de BI**: Apache Superset, conectado a ClickHouse y configurado con dashboards embebibles.
* **Capa Web**: backend Node/Express (gateway) para emisión de *guest tokens* de Superset y frontend React para la navegación del usuario final.

---

## 1. Arquitectura general

La plataforma está orquestada con **Docker Compose** y se organiza en tres capas:

### 1.1 Capa de Datos

* **automatic_download**

  * Imagen construida desde `./automatization/download_scripts/`.
  * Descarga ENEMDU, Latinobarómetro y V-Dem.
  * Ejecuta `runner.sh` que encadena:

    * Descarga de fuentes crudas.
    * Limpieza inicial / normalización de columnas.
    * Generación de CSV normalizados en `data/`.
  * Usa variables de entorno:

    * `ENEMDU_ROOT`, `PERSONA_UNPROC`, `PERSONA_PROCESSED`.
    * `VIVIENDA_UNPROC`, `VIVIENDA_PROCESSED`.
    * `LATINOBAROMETRO_ROOT`, `LATINOBAROMETRO_*`.
    * `VDEM_ROOT`, `VDEM_DATA`.

* **clickhouse_server**

  * Contenedor `clickhouse/clickhouse-server`.
  * Depende de `automatic_download` (solo arranca si la descarga termina correctamente).
  * Monta:

    * Volumen persistente de datos en `/var/lib/clickhouse`.
    * Scripts de inicialización en `/docker-entrypoint-initdb.d` (incluye `create_table.sql`).
  * Configuración por variables:

    * `CH_HOST`, `CH_PORT`, `CH_USER`, `CH_PASSWORD`, `CH_DATABASE`.
  * Expone:

    * `8123` (HTTP).
    * `9000` (protocolo nativo).
  * Healthcheck sobre `/ping`.

* **clickhouse_client**

  * Cliente interactivo `clickhouse/clickhouse-client`.
  * Espera a que `clickhouse_server` esté healthy.
  * Abre un cliente de línea de comandos (útil para diagnóstico y mantenimiento).

* **automatic_ingest**

  * Imagen construida desde `./automatization/ingest/`.
  * Depende de:

    * `automatic_download` (completado con éxito).
    * `clickhouse_server` (healthy).
  * Monta:

    * Diccionarios (`data/diccionario`).
    * ENEMDU persona/vivienda (`data/enemdu_*`).
    * V-Dem (`data/VDEM`).
    * Latinobarómetro (`data/latinobarometro/*`).
    * Logs y errores (`automatization/ingest/logs`, `automatization/ingest/errors`).
  * Ejecuta `runner.sh` que:

    * Ingresa diccionarios, ENEMDU, Latinobarómetro y V-Dem en ClickHouse.
    * Calcula indicadores y vistas agregadas.
    * Registra actividad en `LOG_DIR` y errores en `ERR_DIR`.

### 1.2 Capa de BI

* **superset**

  * Apache Superset con configuración personalizada.
  * Depende de `clickhouse_server`.
  * Usa variables:

    * `SUPERSET_LOAD_EXAMPLES`, `SUPERSET_SECRET_KEY`.
    * `DATABASE_DIALECT`, `DATABASE_HOST`, `DATABASE_PORT`,
      `DATABASE_DB`, `DATABASE_USER`, `DATABASE_PASSWORD`.
    * `MAPBOX_API_KEY`.
  * Monta:

    * `./volumes/superset/home` como `SUPERSET_HOME`.
    * Scripts de inicialización (`init_superset_db.py`, `superset_config.py`).
  * Expone el puerto `8088` para la interfaz web.
  * Healthcheck sobre `/health`.

### 1.3 Capa Web

* **gateway**

  * Backend Node/Express para gestionar *guest tokens* de Superset.
  * Código en `./web_app/backend/`.
  * Variables vía `.env`:

    * `SUPERSET_URL`, `SUPERSET_API`.
    * `SUPERSET_USER`, `SUPERSET_PASS`.
    * `ALLOWED_DASHBOARDS` (lista blanca de UUIDs de dashboards).
  * Depende de `superset`.
  * Expone el puerto `8080`.
  * Ruta principal:

    * `GET /api/superset/guest-token`

      * Inicia sesión en Superset (`/api/v1/security/login`).
      * Solicita guest token para un `dashboardId` permitido.

* **react_app**

  * Frontend en React en `./web_app/frontend/`.
  * Variables desde `.env`:

    * `SUPERSET_API_FRONT`, `ALLOWED_DASHBOARDS`, `GATEWAY`,
      `MAPBOX_API_KEY`.
  * Expone el puerto `3000`.
  * Funcionalidad:

    * Páginas de proyecto, metodología e indicadores.
    * Uso del componente `SupersetDashboard` para embeber dashboards de Superset.
    * Obtención de guest tokens a través del gateway.

---

## 2. Requisitos previos

Servidor dedicado recomendado:

* Sistema operativo tipo **Linux** (p.ej. Ubuntu Server 20.04+).
* **Docker ≥ 20.10**.
* **Docker Compose ≥ 1.29** (o plugin equivalente).
* Acceso a internet para:

  * Descargar imágenes de Docker.
  * Descargar datos de ENEMDU, Latinobarómetro y V-Dem.
* Usuario con permisos para ejecutar `docker` y `docker-compose`.

---

## 3. Obtención del código fuente

```bash
git clone https://github.com/datascienceyt/proyecto_pii25-08
cd proyecto_pii25-08

# (Opcional) Ver estructura a dos niveles
tree -L 2
```

Asegúrate de que existan al menos las carpetas:

* `data/`
* `automatization/`
* `web_app/`
* `docs/`
* `clickhouse/`
* `superset/`
* Archivos: `.env`, `docker-compose.yml`, `README.md`, etc.

Otorga permisos de ejecución a los *runners*:

```bash
chmod +x automatization/download_scripts/runner.sh
chmod +x automatization/ingest/runner.sh
```

---

## 4. Estructura de directorios

Esquema simplificado:

```text
. (raíz del proyecto)
├── .env                       # Variables de entorno
├── docker-compose.yml         # Orquestación de contenedores
├── README.md                  # Descripción general
├── automatization/            # Código de automatización (ETL)
│   ├── download_scripts/      # Descarga + limpieza inicial
│   │   ├── enemdu_descarga.py
│   │   ├── latinobarometro_descarga.py
│   │   ├── vdem_descarga.py
│   │   ├── limpieza_persona.py
│   │   ├── limpieza_vivienda.py
│   │   ├── limpieza_latinobarometro.py
│   │   ├── limpieza_vdem.py
│   │   └── runner.sh
│   ├── ingest/                # Ingesta a ClickHouse + indicadores
│   │   ├── ingest_persona.py
│   │   ├── ingest_vivienda.py
│   │   ├── ingest_latinobarometro.py
│   │   ├── ingest_vdem.py
│   │   ├── ingest_codigos.py
│   │   ├── ingest_geojson.py
│   │   ├── errors/            # Filas con errores de ingesta
│   │   └── logs/              # Registros de ejecución
│   └── init-scripts/
│       ├── clickhouse/        # SQL de creación de tablas y vistas
│       │   └── create_table.sql
│       └── superset/          # Imagen y config de Superset
│           ├── Dockerfile
│           ├── entrypoint.sh
│           ├── init_superset_db.py
│           └── superset_config.py
├── clickhouse/                # (según organización real)
├── superset/                  # (según organización real)
└── data/                      # Datos
    ├── diccionario/           # Códigos, pobreza, salarios, geojson
    ├── enemdu_persona/        # ENEMDU Personas (unprocessed/processed)
    ├── enemdu_vivienda/       # ENEMDU Vivienda (unprocessed/processed)
    ├── latinobarometro/       # DTA, CSV crudos y normalizados
    └── raw/
        └── ENEMDU/            # Zips originales del INEC
```

---

## 5. Variables de entorno principales

Las variables se definen en el archivo `.env` de la raíz del proyecto.
**No** se recomienda versionar `.env` con credenciales reales.

### 5.1 Configuración general

* `TZ`: zona horaria del contenedor (ej. `America/Bogota`).

### 5.2 ClickHouse

* `CH_HOST`: host de ClickHouse (en Compose suele ser `clickhouse_server`).
* `CH_PORT`: puerto nativo (9000).
* `CH_USER`: usuario de aplicación.
* `CH_PASSWORD`: contraseña de aplicación.
* `CH_DATABASE`: base de datos por defecto (ej. `indicadores`).

Estas credenciales deben coincidir con `DATABASE_USER` y `DATABASE_PASSWORD` usadas por Superset.

### 5.3 Rutas de datos y diccionarios

* ENEMDU:

  * `ENEMDU_ROOT`
  * `PERSONA_UNPROC`, `PERSONA_PROCESSED`
  * `VIVIENDA_UNPROC`, `VIVIENDA_PROCESSED`
* Latinobarómetro:

  * `LATINOBAROMETRO_ROOT`
  * `LATINOBAROMETRO_UNPROC_DTA`, `LATINOBAROMETRO_UNPROC_CSV`
  * `LATINOBAROMETRO_NORM_CSV`, `LATINOBAROMETRO_DICT_CSV`
  * `LATINOBAROMETRO_PROCESSED`
* V-Dem:

  * `VDEM_ROOT`, `VDEM_DATA`
* Diccionario:

  * `CODIGOS_FILE`
  * `POVERTY_FILE`
  * `SBU_FILE`
  * `GEOJSON_FILE`

### 5.4 Logs y control de ingesta

* `LOG_DIR`: directorio de logs de ingesta.
* `ERR_DIR`: directorio para filas con errores.
* `STOP_ON_ERROR`: indica si se detiene o no ante errores durante la ingesta.
* `USE_SENTINELS`: uso de archivos centinela (si aplica).
* `MAX_RETRIES`, `RETRY_DELAY`: reintentos ante fallos.

### 5.5 Superset

* `SUPERSET_LOAD_EXAMPLES`: cargar o no ejemplos.
* `SUPERSET_SECRET_KEY`: clave secreta de Superset.
* `DATABASE_DIALECT`: dialecto (p.ej. `clickhouse`).
* `DATABASE_HOST`, `DATABASE_PORT`, `DATABASE_DB`.
* `DATABASE_USER`, `DATABASE_PASSWORD`.
* `SUPERSET_USER`, `SUPERSET_PASS`: credenciales del usuario admin.
* `SUPERSET_ADMIN_FIRSTNAME`, `SUPERSET_ADMIN_LASTNAME`, `SUPERSET_ADMIN_EMAIL`.
* `MAPBOX_API_KEY`: API key para mapas.

### 5.6 Web App (Node + React)

* `PORT`: puerto interno del backend.
* `SUPERSET_URL`: URL interna de Superset (p.ej. `http://superset:8088`).
* `SUPERSET_API`: endpoint de seguridad de Superset.
* `SUPERSET_API_FRONT`: URL que usará el frontend para acceder a Superset.
* `ALLOWED_DASHBOARDS`: lista de UUIDs de dashboards permitidos, separados por comas.
* `GATEWAY`: URL pública del backend.
* `MAPBOX_API_KEY`: reutilizada en el frontend.

---

## 6. Puesta en marcha

### 6.1 Preparación de `.env`

1. Copiar el archivo `.env` de ejemplo (si existe) o crear uno siguiendo la estructura descrita.
2. Ajustar al menos:

   * `CH_USER`, `CH_PASSWORD`.
   * `DATABASE_USER`, `DATABASE_PASSWORD`.
   * `SUPERSET_USER`, `SUPERSET_PASS` (usar contraseñas seguras).
   * `SUPERSET_ADMIN_*` (datos del administrador).
   * Rutas de datos y diccionarios según el entorno real.

### 6.2 Primer arranque (capa de datos + BI)

Desde la raíz del proyecto:

```bash
docker-compose --env-file .env up --build \
  automatic_download \
  clickhouse_server \
  clickhouse_client \
  automatic_ingest \
  superset
```

#### Verificar logs de automatización

* Descarga/limpieza:

```bash
docker logs -f automatic_download
```

* Ingesta:

```bash
docker logs -f automatic_ingest
```

Ambos contenedores deben finalizar con código de salida `0` cuando `runner.sh` termine.

#### Validar ClickHouse y Superset

1. Estado general:

   ```bash
   docker-compose ps
   ```

2. Healthcheck de ClickHouse:

   ```bash
   curl http://localhost:8123/ping
   ```

   Debería devolver `Ok`.

3. Acceder a Superset en el navegador:

   ```text
   http://<IP-del-servidor>:8088
   ```

   Iniciar sesión con `SUPERSET_USER` / `SUPERSET_PASS`.

### 6.3 Configuración de dashboards en Superset

1. Ingresar a `http://<IP-del-servidor>:8088`.
2. Crear o importar dashboards, por ejemplo:

   * Dashboard general de indicadores.
   * Dashboard ENEMDU.
   * Dashboard Latinobarómetro.
   * Dashboard V-Dem.
3. Para cada dashboard:

   * Abrir el dashboard.
   * Ir al menú (tres puntos) → **Embed dashboard**.
   * En **Allowed Domains** agregar:

     * `http://<IP-del-servidor>:8080` (backend).
     * `http://<IP-del-servidor>:3000` (frontend).
   * Hacer clic en **Enable embedding**.
   * Copiar el **UUID** del dashboard (se usará en `ALLOWED_DASHBOARDS` y en el frontend).

### 6.4 Configurar `ALLOWED_DASHBOARDS` en el gateway

En el backend (`web_app/backend/server.js`) se parsea la lista de dashboards permitidos a partir de la variable de entorno:

```js
const ALLOWED_RAW = process.env.ALLOWED_DASHBOARDS || "";
const ALLOWED_DASHBOARDS = new Set(
  ALLOWED_RAW.split(",").map((s) => s.trim()).filter(Boolean)
);
```

Actualizar `.env` con los UUIDs (separados por comas):

```env
ALLOWED_DASHBOARDS=UUID_GENERAL,UUID_ENEMDU,UUID_LATINO,UUID_VDEM
```

Guardar el archivo antes de reconstruir el contenedor `gateway`.

### 6.5 Configurar supersetId en la aplicación React

En `web_app/frontend/app/src/pages/IndicatorsPage.jsx` se mapean las tarjetas de indicadores a los UUIDs de Superset:

```js
const GENERAL_DASHBOARD = {
  key: "general-overview",
  label: "Visión general de indicadores",
  supersetId: "UUID_GENERAL",
};

const BASES_DASHBOARDS = [
  {
    key: "base-vdem",
    label: "VDEM",
    description: "Indicadores comparativos construidos a partir de la base VDEM.",
    supersetId: "UUID_VDEM",
  },
  {
    key: "base-latinobarometro",
    label: "Latinobarómetro",
    description: "Indicadores comparativos construidos a partir de la base Latinobarómetro.",
    supersetId: "UUID_LATINO",
  },
  {
    key: "base-enemdu",
    label: "ENEMDU",
    description: "Indicadores comparativos construidos a partir de la base ENEMDU.",
    supersetId: "UUID_ENEMDU",
  },
];
```

1. Abrir `IndicatorsPage.jsx`.
2. Reemplazar `UUID_GENERAL`, `UUID_VDEM`, `UUID_LATINO`, `UUID_ENEMDU` por los UUIDs reales.
3. Guardar los cambios.

### 6.6 Entornos con máquina virtual (VM)

En `src/components/SupersetDashboard.jsx` suele haber referencias a `localhost`:

```js
const SUPERSET_DOMAIN = "http://localhost:8088";
const BACKEND_GATEWAY = "http://localhost:8080";
```

En entornos con VM, sustituir `localhost` por la IP de la VM:

```js
const SUPERSET_DOMAIN = "http://<IP-de-la-VM>:8088";
const BACKEND_GATEWAY = "http://<IP-de-la-VM>:8080";
```

No confundir la IP de la VM con la IP del host físico.

### 6.7 Arranque de gateway y react_app

1. Construir e iniciar el backend:

   ```bash
   docker-compose --env-file .env up --build --no-deps gateway
   ```

2. Probar healthcheck:

   ```bash
   curl http://localhost:8080/health
   ```

3. Construir e iniciar el frontend:

   ```bash
   docker-compose up --build --no-deps react_app
   ```

4. Ver estado global:

   ```bash
   docker-compose ps
   ```

5. Acceder a la app:

   ```text
   http://<IP-del-servidor>:3000
   ```

La sección de indicadores debería mostrar los dashboards embebidos.

---

## 7. Árbol de navegación de la aplicación web (alto nivel)

Estructura conceptual de la interfaz React:

* **Página de inicio / Proyecto**

  * Presentación del proyecto y objetivos generales.
* **Metodología**

  * Descripción de fuentes de datos (ENEMDU, Latinobarómetro, V-Dem).
  * Metodología de construcción de indicadores.
* **Indicadores**

  * **Visión general de indicadores**

    * Dashboard agregando indicadores clave.
  * **Indicadores por base**

    * VDEM: indicadores comparativos basados en V-Dem.
    * Latinobarómetro: indicadores de opinión pública y bienes del hogar.
    * ENEMDU: indicadores de empleo, pobreza, NBI, IPM.

Los nombres exactos de rutas (paths) dependen de la configuración del router en el código React.

---

## 8. Mantenimiento y operación

### 8.1 Backups

* **ClickHouse**

  * Respaldar el volumen que se monta en `/var/lib/clickhouse` (p.ej. `clickhouse_volume`).
  * Opcionalmente usar herramientas como `clickhouse-backup` para dumps incrementales.

* **Superset**

  * Respaldar `./volumes/superset/home` (SUPERSET_HOME).
  * Exportar dashboards y datasets vía CLI:

    ```bash
    superset export-dashboards -f backup_dashboards.zip
    ```

### 8.2 Logs

* Logs de ingesta: `automatization/ingest/logs/`.
* Errores de ingesta: `automatization/ingest/errors/`.

### 8.3 Troubleshooting básico

* Ver estado de contenedores:

  ```bash
  docker-compose ps
  ```

* Forzar descarga + limpieza completa por fuente (ejemplos):

  ```bash
  # ENEMDU
  docker-compose exec automatic_download python enemdu_descarga.py \
    && python limpieza_persona.py \
    && python limpieza_vivienda.py

  # Latinobarómetro
  docker-compose exec automatic_download python latinobarometro_descarga.py \
    && python limpieza_latinobarometro.py

  # V-Dem
  docker-compose exec automatic_download python vdem_descarga.py \
    && python limpieza_vdem.py
  ```

* Reprocesar solo descarga:

  ```bash
  docker-compose exec automatic_download python enemdu_descarga.py
  docker-compose exec automatic_download python latinobarometro_descarga.py
  docker-compose exec automatic_download python vdem_descarga.py
  ```

* Reprocesar solo limpieza:

  ```bash
  docker-compose exec automatic_download python limpieza_persona.py
  docker-compose exec automatic_download python limpieza_vivienda.py
  docker-compose exec automatic_download python limpieza_latinobarometro.py
  docker-compose exec automatic_download python limpieza_vdem.py
  ```

* Entrar al cliente de ClickHouse:

  ```bash
  docker-compose exec clickhouse_client sh

  clickhouse-client --host clickhouse_server \
    --port 9000 --user <USER> --password <PASSWORD>
  ```

* Eliminar contenedores y volúmenes (borra la BD):

  ```bash
  docker-compose down --volumes
  ```

  Tras esto, los CSV procesados deben volver a las carpetas `unprocessed` para que la ingesta se ejecute correctamente en el siguiente ciclo.

---

## 9. Créditos

* **Proyecto**: “Efectos de la desigualdad socioeconómica en la percepción de la democracia en Latinoamérica: periodo 1995–2023”.
* **Mantenimiento técnico**: repositorio y manual preparados por Patricio Mendoza.

---
