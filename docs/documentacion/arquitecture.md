## Arquitectura de la Plataforma

### 1. Visión general

La arquitectura sigue un esquema por capas, todas orquestadas mediante `docker-compose`:

* **Capa de Datos**: descarga, limpieza e ingesta.
* **Capa de BI**: motor analítico de dashboards (Apache Superset).
* **Capa Web**: backend gateway (Node/Express) + frontend React.

Diagrama lógico (simplificado):

```text
[Capa de Datos]
  automatic_download  -->  archivos CSV normalizados
        |
        v
  clickhouse_server (BD analítica) <------ automatic_ingest
        ^
        |
  clickhouse_client (uso interactivo)

[Capa BI]
  superset  <------>  clickhouse_server

[Capa Web]
  gateway (Node/Express)  <----->  superset (API security)
        ^
        |
  react_app (frontend)  <------>  gateway (guest tokens)
```

---

### 2. Capa de Datos

#### 2.1 automatic_download

* **Responsabilidad**:

  * Descarga y limpieza inicial de:

    * ENEMDU (persona/vivienda).
    * Latinobarómetro.
    * V-Dem.
* **Código fuente**:

  * `automatization/download_scripts/`.
* **Scripts principales**:

  * `enemdu_descarga.py`, `latinobarometro_descarga.py`, `vdem_descarga.py`.
  * `limpieza_persona.py`, `limpieza_vivienda.py`.
  * `limpieza_latinobarometro.py`, `limpieza_vdem.py`.
  * `runner.sh` (orquestación).
* **Volúmenes de datos** (según `.env`):

  * ENEMDU: `ENEMDU_ROOT`, `PERSONA_UNPROC`, `PERSONA_PROCESSED`,
    `VIVIENDA_UNPROC`, `VIVIENDA_PROCESSED`.
  * Latinobarómetro: `LATINOBAROMETRO_ROOT`, `LATINOBAROMETRO_*`.
  * V-Dem: `VDEM_ROOT`, `VDEM_DATA`.
* **Variables auxiliares**:

  * Directorios de logs y errores: `LOG_DIR`, `ERR_DIR`.
  * Control de ejecución: `STOP_ON_ERROR`, `USE_SENTINELS`, `MAX_RETRIES`, `RETRY_DELAY`.

#### 2.2 clickhouse_server

* **Imagen**: `clickhouse/clickhouse-server`.
* **Configuración**:

  * Zona horaria (`TZ`).
  * Credenciales y base: `CH_HOST`, `CH_PORT`, `CH_USER`, `CH_PASSWORD`, `CH_DATABASE`.
* **Volúmenes**:

  * Datos persistentes: volumen montado en `/var/lib/clickhouse`.
  * Scripts SQL de inicialización en `/docker-entrypoint-initdb.d`:

    * Incluye `create_table.sql`, que crea tablas, materialized views y vistas finales.
* **Puertos**:

  * `8123`: API HTTP (útil para healthchecks y consultas simples).
  * `9000`: protocolo nativo de ClickHouse (cliente CLI, Superset).
* **Dependencias**:

  * Declara `depends_on` respecto a `automatic_download` para empezar solo cuando la descarga terminó.

#### 2.3 clickhouse_client

* **Imagen**: `clickhouse/clickhouse-client`.
* **Uso**:

  * Cliente shell interactivo para:

    * Diagnóstico.
    * Ejecución de consultas ad-hoc.
    * Verificación de tablas y vistas.

#### 2.4 automatic_ingest

* **Responsabilidad**:

  * Cargar los CSV ya limpios en ClickHouse.
  * Aplicar diccionarios y cálculos de indicadores (por ejemplo, IPM, NBI, tasas laborales).
* **Código fuente**:

  * `automatization/ingest/`.
* **Scripts de ingesta**:

  * `ingest_persona.py`, `ingest_vivienda.py`.
  * `ingest_latinobarometro.py`, `ingest_vdem.py`.
  * `ingest_codigos.py`, `ingest_geojson.py`.
* **Volúmenes**:

  * Diccionarios (`data/diccionario`).
  * Directorios `unprocessed/processed` de ENEMDU.
  * Directorios normalizados de Latinobarómetro.
  * Directorios de V-Dem.
  * Logs (`automatization/ingest/logs`) y errores (`automatization/ingest/errors`).
* **Dependencias**:

  * `automatic_download` debe finalizar correctamente.
  * `clickhouse_server` debe estar healthy.

---

### 3. Capa de BI (Superset)

#### 3.1 superset

* **Imagen**:

  * Construida desde `automatization/init-scripts/superset/` (Dockerfile + entrypoint).
* **Configuración**:

  * Variables clave:

    * `SUPERSET_LOAD_EXAMPLES`.
    * `SUPERSET_SECRET_KEY`.
    * `MAPBOX_API_KEY`.
    * `DATABASE_DIALECT` (ClickHouse).
    * `DATABASE_HOST`, `DATABASE_PORT`, `DATABASE_DB`.
    * `DATABASE_USER`, `DATABASE_PASSWORD`.
  * Scripts de inicio:

    * `init_superset_db.py` (creación de usuario admin, conexión a ClickHouse, etc.).
    * `superset_config.py` (configuración general).
* **Almacenamiento**:

  * `./volumes/superset/home` montado como `SUPERSET_HOME` (BD interna de Superset, dashboards, etc.).
* **Servicios**:

  * Web UI en `:8088`.
  * Healthcheck en `/health`.
* **Seguridad y embed**:

  * Dashboards configurados en modo “Embed dashboard”.
  * Allowed Domains deben incluir las URLs de `gateway` y `react_app`.

---

### 4. Capa Web

#### 4.1 gateway (Node/Express)

* **Rol**:

  * Backend *fino* que se encarga de:

    * Autenticarse contra Superset (`/api/v1/security/login`).
    * Solicitar guest tokens para dashboards específicos.
    * Exponer una API para que el frontend obtenga el token sin conocer credenciales de Superset.
* **Variables de entorno**:

  * `SUPERSET_URL`: URL interna del servicio Superset en la red de Docker.
  * `SUPERSET_API`: endpoint de seguridad (normalmente `/api/v1/security`).
  * `SUPERSET_USER`, `SUPERSET_PASS`: credenciales del usuario admin de Superset.
  * `ALLOWED_DASHBOARDS`: lista de UUIDs permitidos.
  * `PORT`: puerto de escucha del backend.
* **Lógica de control de acceso**:

  * Los UUIDs permitidos se cargan así:

    ```js
    const ALLOWED_RAW = process.env.ALLOWED_DASHBOARDS || "";
    const ALLOWED_DASHBOARDS = new Set(
      ALLOWED_RAW.split(",").map((s) => s.trim()).filter(Boolean)
    );
    ```

  * Si el `dashboardId` solicitado no está en `ALLOWED_DASHBOARDS`, se rechaza la petición.

#### 4.2 react_app (Frontend React)

* **Rol**:

  * Proporcionar la interfaz de usuario del proyecto:

    * Páginas de descripción del proyecto.
    * Metodología de datos.
    * Selección y visualización de indicadores.
* **Integración con Superset**:

  * Componente `SupersetDashboard`:

    * Recibe un `supersetId` (UUID del dashboard).
    * Llama al `gateway` para obtener un guest token.
    * Embebe el dashboard con el Superset Embedded SDK.
* **Configuración específica**:

  * `SUPERSET_API_FRONT`: URL que el navegador usará para hablar con Superset (p.ej. `http://localhost:8088` o `http://<IP-de-la-VM>:8088`).
  * `GATEWAY`: URL pública del backend (p.ej. `http://localhost:8080`).
  * `ALLOWED_DASHBOARDS`: debe ser coherente con los UUIDs definidos en el backend.
* **En entornos de VM**:

  * Debe ajustarse `SUPERSET_DOMAIN` y `BACKEND_GATEWAY` en `SupersetDashboard.jsx` para usar la IP de la VM en lugar de `localhost`.

---

### 5. Consideraciones de despliegue

* La infraestructura asume un **servidor dedicado** (físico o virtual) con puertos `8088`, `8080`, `3000`, `8123`, `9000` disponibles.
* Si se expone públicamente:

  * Se recomienda poner un **reverse proxy** (Nginx, Caddy, etc.) delante de Superset, gateway y React.
  * Agregar HTTPS (certificados TLS).
  * Asegurar credenciales (`SUPERSET_SECRET_KEY`, `CH_PASSWORD`, `DATABASE_PASSWORD`, etc.).

---

### 6. Flujo de datos resumido

1. `automatic_download` descarga datos crudos en `data/raw/*` y genera CSV normalizados en `data/*/processed`.
2. `automatic_ingest` lee estos CSV y los inserta en ClickHouse (`indicadores.*`).
3. El script SQL `create_table.sql` crea tablas, materialized views y vistas de indicadores a distintos niveles geográficos y temporales.
4. Superset se conecta a ClickHouse, expone datasets y dashboards embebibles.
5. El gateway solicita guest tokens a Superset y los entrega al frontend.
6. El frontend React muestra los dashboards dentro de la interfaz del proyecto.

---