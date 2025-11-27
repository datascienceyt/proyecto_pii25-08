# Arquitectura del Sistema

Este documento describe la arquitectura lógica del proyecto **Indicadores**, detallando los contenedores, la red interna de Docker, los puertos expuestos y la interacción entre los componentes.

---

## 🏗️ Diseño Lógico

El sistema sigue una arquitectura de **pipeline de datos** desacoplada en cuatro componentes principales:

```
[Fuente ENEMDU] 
      ↓
[Scraper & Limpieza] (enemdu_descarga)
      ↓
[Ingestión CSV] (enemdu_ingest)
      ↓
[Base de Datos Analítica] (ClickHouse)
      ↓
[Visualización] (Apache Superset)
```

Cada etapa se ejecuta en su propio contenedor de Docker para asegurar **modularidad, reproducibilidad y escalabilidad**.

---

## 📦 Contenedores

1. **enemdu_descarga**
   - Descarga automáticamente archivos de la encuesta ENEMDU.
   - Ejecuta scripts de limpieza (`limpieza_persona.py`, `limpieza_vivienda.py`).
   - Expone volúmenes de datos en `data/raw` y `data/enemdu_*`.

2. **clickhouse**
   - Motor de base de datos analítica en columna.
   - Expone los puertos:
     - `8123`: interfaz HTTP.
     - `9000`: protocolo nativo TCP.
   - Monta volumen persistente `clickhouse_data`.

3. **enemdu_ingest**
   - Procesa CSVs de:
     - Diccionario de códigos.
     - ENEMDU persona y vivienda.
     - Finanzas (Ministerio).
   - Scripts idempotentes que archivan archivos ya procesados.

4. **superset**
   - Plataforma de visualización y BI.
   - Expone el puerto `8088` (UI web).
   - Se conecta directamente a ClickHouse mediante SQLAlchemy.

---

## 🌐 Red y Conectividad

- Los servicios están en la red interna de `docker-compose`.
- Comunicación directa:
  - `superset → clickhouse`
  - `enemdu_ingest → clickhouse`
- Acceso externo solo a:
  - `http://localhost:8088` (Superset)
  - `http://localhost:8123` (API HTTP ClickHouse)

---

## 🔒 Seguridad y Credenciales

- Variables de entorno configuradas en `.env` o `docker-compose.yml`.
- Ejemplo:
  ```bash
  CLICKHOUSE_USER=admin
  CLICKHOUSE_PASSWORD=secret_pw
  SUPERSET_PW=MiContrasenaSegura
  ```

---
