# Diccionario de Datos y Fuentes

Este documento describe las fuentes de datos, la periodicidad de actualización y el diccionario de variables clave utilizadas en el proyecto.

---

## 📂 Fuentes de Datos

1. **ENEMDU (Encuesta Nacional de Empleo, Desempleo y Subempleo)**
   - Descargada automáticamente desde el portal oficial del INEC.
   - Guardada en `data/raw/ANUAL/{AÑO}`.
   - Cobertura: **2007–2025**.

2. **Diccionario de códigos**
   - Archivos de referencia para interpretación de variables.
   - Ubicación: `data/diccionario/`.

3. **Ministerio de Finanzas**
   - Información presupuestaria anual por provincia y cantón.
   - Ubicación: `data/mf_finanzas/`.

---

## ⏳ Periodicidad

- **ENEMDU**: mensual (cada mes se generan nuevas encuestas).
- **Finanzas**: anual (ejercicio fiscal).
- **Procesamiento interno**: bajo demanda o en batch según disponibilidad de datos.

---

## 📑 Diccionario de Variables

### ENEMDU Persona
- `p03`: Edad.
- `p02`: Sexo.
- `condact`: Condición de actividad (ocupado, desempleado, etc.).
- `ingrl`: Ingreso laboral.
- `ingpc`: Ingreso per cápita.
- `secemp`: Sector de empleo (formal/informal).
- `fexp`: Factor de expansión.

### ENEMDU Vivienda
- `vi04a/vi04b`: Material del piso.
- `vi05a/vi05b`: Material de la pared.
- `vi09`: Servicio higiénico.
- `vi10`: Fuente de agua.

### Finanzas
- `EJERCICIO`: Año fiscal.
- `GRUPO`, `ITEM`: Clasificación presupuestaria.
- `PROVINCIA`, `CANTON`: División política.
- `CODIFICADO`: Presupuesto asignado.

---
