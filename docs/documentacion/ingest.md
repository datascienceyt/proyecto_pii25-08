# Procesos de Ingesta de Datos

Este documento describe los flujos de ingestión, la gestión de directorios, las políticas de idempotencia y los mecanismos de manejo de errores.

---

## 🔄 Flujo de Ingesta

1. **Descarga y Limpieza**
   - `enemdu_descarga` descarga CSV comprimidos y ejecuta limpieza.
   - Resultados guardados en `data/enemdu_*`.

2. **Ingesta Automática**
   - Scripts Python (`ingest_persona.py`, `ingest_vivienda.py`, `ingest_codigos.py`, `ingest_finanzas.py`).
   - Insertan datos en ClickHouse mediante **inserciones masivas**.

3. **Archivar Procesados**
   - Archivos movidos de `unprocessed/` a `processed/` tras carga exitosa.

---

## 📂 Directorios (Colas de Ingesta)

- `data/enemdu_persona/unprocessed/` → pendientes.
- `data/enemdu_persona/processed/` → cargados.
- `data/enemdu_vivienda/unprocessed/`.
- `data/mf_finanzas/unprocessed/`.

Estos directorios actúan como **colas naturales de procesamiento**.

---

## ✅ Idempotencia

- Política: *"Un archivo solo se procesa una vez"*.
- Estrategia:
  - Si la carga es exitosa o parcialmente exitosa, se mueve a `processed/`.
  - Parámetro `STOP_ON_ERROR` controla si detener ante primer fallo.

---

## 🛡️ Manejo de Errores

- Logs centralizados en `/ingest/logs`.
- Archivos problemáticos se mueven a `/ingest/errors`.
- Columnas inválidas opcionalmente reciben valores centinela:
  - Enteros: `-404`.
  - Flotantes: `-404.0`.
  - Strings: `"-404"`.

---
