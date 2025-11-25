# Esquema en ClickHouse

Este documento detalla la estructura de la base de datos, las tablas, las vistas materializadas y el particionado.

---

## 🗄️ Esquema

- Nombre: `indicadores`.

---

## 📊 Tablas

### `enemdu_persona`
- Variables individuales de la encuesta ENEMDU.
- Tipos de datos optimizados (Int32, Float64, String).
- Columnas clave:
  - `id_persona`, `id_hogar`, `periodo`, `edad`, `sexo`, `condact`, `ingrl`.

### `enemdu_vivienda`
- Características de la vivienda y servicios básicos.
- Columnas clave:
  - `id_vivienda`, `id_hogar`, `periodo`, `material_pared`, `material_piso`, `agua`, `higienico`.

### `mf_finanzas`
- Datos presupuestarios.
- Columnas clave:
  - `EJERCICIO`, `GRUPO_DESC`, `ITEM_DESC`, `PROVINCIA_DESC`, `CODIFICADO`.

---

## 📈 Vistas Materializadas

- `mv_indicadores_persona_canton`:
  - Agrega por **cantón, año, sexo y área**.
  - Métricas:
    - Tasa de Participación Global (TPG).
    - Tasa de Empleo (TPB).
    - Subempleo, informalidad, brechas de género.
    - Desempleo juvenil, trabajo infantil.

---

## 🧩 Particionado

- **Clave de partición**: `periodo` (`YYYYMM`).
- **Motor**: `MergeTree`.
- **Ordenamiento**: `ORDER BY (periodo)`.
- Granularidad: `8192`.

Esto asegura consultas rápidas por año, mes y región.

---
