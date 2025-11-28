## Modelo de Datos en ClickHouse

La base de datos principal se llama **`indicadores`** e incluye tablas de detalle,
tablas agregadas (*sums*) y vistas de indicadores para:

* ENEMDU (persona y vivienda).
* IPM e indicadores de pobreza/NBI.
* Latinobarómetro.
* V-Dem.

Este documento resume la funcionalidad de las tablas y vistas más relevantes.

---

## 1. Tablas base ENEMDU

### 1.1 `enemdu_persona`

* **Propósito**: almacenar microdatos de personas de ENEMDU.
* **Tipo**: `MergeTree ORDER BY (periodo)`.
* **Campos principales** (ejemplos):

  * `periodo` (String): identificador del período (año + mes).
  * Variables de ubicación: `zona`, `sector`, `area`, `ciudad`, `provincia` (derivada en vistas).
  * Indicadores laborales y de pobreza:

    * `condact`, `desempleo`, `empleo`, `pobreza`, `epobreza`.
  * Ingreso y factores de expansión:

    * `fexp` (factor de expansión).
    * `ingpc` (ingreso per cápita).
    * `ingrl` (ingreso laboral).
  * Identificadores:

    * `hogar`, `id_hogar`, `id_persona`, `id_vivienda`, `vivienda`.
  * Gran número de variables `pXX` de cuestionario (edad, sexo, asistencia, horas trabajadas, etc.).

Esta tabla es la base para el cálculo de indicadores laborales, educativos y de pobreza por persona.

### 1.2 `enemdu_vivienda`

* **Propósito**: almacenar características de vivienda/hogar.
* **Tipo**: `MergeTree ORDER BY (periodo)`.
* **Campos principales**:

  * `periodo`, `area`, `ciudad`, `zona`, `conglomerado`, `estrato`.
  * Identificadores: `hogar`, `id_hogar`, `id_vivienda`, `vivienda`.
  * Condiciones de la vivienda:

    * Variables `viXX` sobre material de paredes, techos, pisos.
    * Servicios básicos (agua, alcantarillado, etc.).
    * Número de cuartos, hacinamiento, etc.

Se utiliza junto con `enemdu_persona` para construir indicadores de vivienda, NBI e IPM.

### 1.3 Tablas auxiliares

* **`poverty_lines`**

  * `periodo`, `linea_pobreza`, `linea_pobreza_extrema`.
  * Se usa para determinar pobreza por ingresos.

* **`sbu_hist`**

  * `periodo`: formato `YYYYMM`.
  * `sbu`: salario básico unificado del período.

---

## 2. Agregados de persona

### 2.1 Tabla `persona_sums`

* **Tipo**: `SummingMergeTree ORDER BY (level, anio, periodo, area, geo)`.
* **Llaves**:

  * `level`: nivel geográfico/temporal (ej. `nacional`, `provincia`, `canton`, `parroquia`, `nacional_sin_area`, `canton_anual`).
  * `anio`: año.
  * `periodo`: mes (0 = anual).
  * `area`: categoría de área (urbano/rural/total).
  * `geo`: código geográfico (vacío para nacional; códigos de provincia, cantón, parroquia).
* **Medidas almacenadas**:

  * Población:

    * `sw_pop`: población total (ponderada).
    * `sw_pet`: población en edad de trabajar.
    * `sw_pea`: población económicamente activa.
    * `sw_occ`: ocupados.
  * Empleo:

    * `s_emp_adecuado`, `s_subempleo`, `s_no_remu`, `s_otro_no_pleno`.
    * `s_formal_w`, `s_informal_w`.
  * Desagregaciones por sexo:

    * `pea_h`, `pea_m`, `ade_h`, `ade_m`.
    * `occ_inc_w_h`, `occ_w_h`, `occ_inc_w_m`, `occ_w_m`.
  * Juventud y ni-ni:

    * `s_youth`, `s_youth_nini`, `s_juv_pea`, `s_juv_des`.
  * Trabajo infantil:

    * `s_kids`, `s_ti`.
  * Otros:

    * `s_occ_manu`: empleo en manufactura.
    * `s_5_24`, `s_asist_5_24`: asistencia a clases.
    * `s_valid_lp`, `s_under_lp`, `s_under_lp_ext`: denominador y numeradores para pobreza y pobreza extrema por ingresos.

### 2.2 MV `mv_persona_all_levels`

* **Tipo**: *materialized view* que escribe en `persona_sums`.
* **Lógica**:

  * En la subconsulta `base` se:

    * Derivan variables como edad (`edad_i`), sexo, condición de actividad (`stat`), horas trabajadas (`horas`), rama de actividad (`rama`).
    * Se calcula el sector (`sector`) en base a variables `p42`, `p47a`, `p49`, `secemp`.
    * Se obtienen códigos geográficos (`prov2`, `cant4`, `parr6`) a partir de la variable `ciudad`.
    * Se determinan flags: `is_pet`, `is_pea`, `is_occ`, `no_est`, `no_trab`, asistencia escolar (`asiste`).
    * Se une con `poverty_lines` para obtener `lp` y `lpe`.
  * Se hace un `ARRAY JOIN` sobre distintos niveles (`nacional`, `provincia`, `canton`, `parroquia`, etc.).
  * Para cada combinación `(level, anio, periodo, area, geo)` se agregan las sumas condicionales que alimentan `persona_sums`.

---

## 3. Vistas de indicadores de persona

Las vistas siguientes consumen `persona_sums` y devuelven tasas en porcentaje.

### 3.1 `indicadores_persona_nacional`

* **Nivel**: nacional (con área).
* **Variables de salida**:

  * `anio`, `periodo`, `mes` (nombre del mes), `area`.
  * Tasas (%):

    * `tasa_participacion_global`, `tasa_participacion_bruta`.
    * `tasa_desempleo`, `empleo_total`.
    * `empleo_formal`, `empleo_informal`.
    * `empleo_adecuado`, `subempleo`, `no_remunerado`, `otro_no_pleno`.
    * `brecha_adecuado_HM`, `brecha_salarial_HM`.
    * `NiNi`, `desempleo_juvenil`.
    * `trabajo_infantil`, `tasa_asistencia_clases`.
    * `empleo_manufactura`.
    * `pobreza_ingresos`, `pobreza_extrema_ingresos`.

Vistas análogas existen para otros niveles:

* `indicadores_persona_provincia`
* `indicadores_persona_canton`
* `indicadores_persona_parroquia`
* `indicadores_persona_canton_anual`
* `indicadores_persona_nacional_por_periodo`
* `indicadores_persona_parroquia_por_periodo`

Cada una adapta la clave geográfica (`provincia`, `canton`, `ciudad`) y la agregación temporal (mensual vs anual).

---

## 4. IPM, NBI e indicadores de vivienda

### 4.1 Vista `enemdu_periodos_intersect`

* Lista los `periodo` que están presentes tanto en `enemdu_persona` como en `enemdu_vivienda`.
* Se usa como base para unir consistentemente ambas tablas.

### 4.2 Tabla `hh_ipm_nbi`

* **Propósito**: almacenar indicadores de IPM y NBI a nivel de hogar.
* **Campos principales**:

  * `periodo`, `id_hogar`.
  * Índice compuesto:

    * `ci`: índice de privación (0–1 aprox).
    * `TPM`: flag de pobre multidimensional.
    * `TPEM`: flag de pobreza extrema multidimensional.
    * `A`: intensidad de privación (solo para pobres TPM).
    * `IPM`: indicador de pobreza multidimensional.
  * Dimensiones de NBI:

    * `depec`: dependencia económica.
    * `ninastesc`: niños en edad escolar que no asisten.
    * `matviv_def`: materiales de vivienda deficientes.
    * `ser_viv`: servicios de vivienda inadecuados.
    * `hacm`: hacinamiento.
    * `NBI_hogar`: flag de hogar con al menos una NBI.

### 4.3 MV `mv_ipm_nbi_hogares`

* **Tipo**: materialized view que escribe en `hh_ipm_nbi`.
* **Resumen de lógica**:

  * Se construye una base de personas (`base`) unida a vivienda (`viv`).
  * Se calculan:

    * Años de escolaridad (`escol`) con una regla detallada sobre `p10a`/`p10b`.
    * Horas trabajadas (`horas`) usando `p20`, `p21`, `p22`, `p24`, `p51a/b/c`, etc.
  * Se definen indicadores por persona para distintas dimensiones (educación, empleo, protección social, vivienda).
  * Estos se agregan a nivel de hogar (`per_to_h`).
  * Se calculan materiales de vivienda (`materiales`) y tipología (`tipviv`).
  * Se derivan indicadores de hacinamiento, servicios, materiales, etc.
  * Se combinan en `hh_inds` y se aplican pesos (arreglo `pesos`) para obtener `ci`, `TPM`, `TPEM`, `A`, `IPM` y NBI.

### 4.4 Tabla `vivienda_sums`

* **Tipo**: `SummingMergeTree ORDER BY (level, anio, periodo, area, geo)`.
* **Contenido**:

  * Población de hogares (`sw_pop`).
  * Sumatorias ponderadas de:

    * `TPM` (`s_tpm`), `TPEM` (`s_tpem`).
    * `A` (`s_A`).
    * `ci` (`s_ipm`).
    * `NBI_hogar` (`s_nbi`).

Se alimenta mediante la MV `mv_vivienda_sums`, que utiliza `hh_ipm_nbi`, `enemdu_persona`, `enemdu_vivienda` y `enemdu_periodos_intersect`.

### 4.5 Vistas de indicadores de vivienda

Se definen vistas paralelas a las de persona:

* `indicadores_vivienda_nacional`
* `indicadores_vivienda_provincia`
* `indicadores_vivienda_canton`
* `indicadores_vivienda_parroquia`
* `indicadores_vivienda_canton_anual`
* `indicadores_vivienda_nacional_por_periodo`
* `indicadores_vivienda_parroquia_por_periodo`

Cada una expone:

* `tpm`, `tpem`: tasas de pobreza multidimensional y extrema.
* `A`: intensidad promedio de privación entre pobres multidimensionales.
* `ipm`: índice de pobreza multidimensional (en %).
* `nbi`: porcentaje de hogares con al menos una NBI.

---

## 5. Latinobarómetro

### 5.1 Tabla `latinobarometro`

* **Propósito**: almacenar microdatos de Latinobarómetro.
* **Campos relevantes**:

  * Identificadores:

    * `research_year`, `resp_country`, `country_name` (ALIAS), `iso3` (ALIAS).
    * `research_region`, `research_city`, `research_city_size`.
  * Percepción democrática:

    * `democ_supp` (apoyo a la democracia).
    * `democ_satis` (satisfacción con la democracia).
  * Posición ideológica:

    * `left_right_scale`.
  * Economía:

    * `job_concern`, `econ_situation`, `resp_economic_perception`.
  * Bienes del hogar:

    * `goods_wash_mach`, `goods_car`, `goods_sewage`, `goods_hot_water`.
  * Confianza institucional:

    * `confidence_congress`, `confidence_judiciary`, `confidence_church`,
      `confidence_police`, `confidence_army`, `confidence_political_parties`.
  * Demografía:

    * `resp_sex`, `resp_age`, `resp_chief`, `resp_education`, `resp_employment`, `resp_religion`.

### 5.2 Tabla `latinobarometro_sums`

* **Tipo**: `SummingMergeTree ORDER BY (level, anio, periodo, area, geo)`.
* **Estructura**:

  * `level`: `pais`, `region`, `ciudad`, `pais_total`.
  * `anio`: año de investigación.
  * `periodo`: siempre 0 (sin desagregación mensual).
  * `geo`: código compuesto según el nivel (país, país-región, país-región-ciudad).
* **Medidas**:

  * Denominadores válidos (`s_valid_*`) para distintas preguntas.
  * Numeradores de interés:

    * Apoyo a la democracia / autoritarismo.
    * Satisfacción con la democracia.
    * Orientación ideológica izq./der.
    * Percepción económica buena/mala.
    * Tenencia de bienes.
    * Confianza alta/baja en instituciones.

### 5.3 MV `mv_latinobarometro_all_levels`

* **Rol**:

  * A partir de cada registro de `latinobarometro`:

    * Define un peso `w` (actualmente igual a 1).
    * Determina flags de validez para cada indicador.
    * Construye claves geográficas:

      * `geo_country`: país.
      * `geo_region`: `pais-region`.
      * `geo_city`: `pais-region-ciudad`.
  * Con un `ARRAY JOIN` genera filas agregadas para:

    * `pais`, `region`, `ciudad`, `pais_total`.
  * Agrega sumas condicionales que alimentan `latinobarometro_sums`.

### 5.4 Vistas de indicadores Latinobarómetro

* **`indicadores_latino_pais`**

  * Se une con un `country_map` para obtener `pais_nombre` e `iso3`.
  * Variables de salida (en %):

    * `tasa_apoyo_democracia`, `tasa_apoyo_autoritarismo`.
    * `tasa_satisfechos_democracia`.
    * `tasa_derecha`, `tasa_izquierda`.
    * `percepcion_econ_buena`, `percepcion_econ_mala`.
    * `tasa_bien_lavadora`, `tasa_bien_auto`, `tasa_bien_alcantarillado`, `tasa_bien_agua_caliente`.
    * `confianza_*_mucha`, `confianza_*_poca_nada` para Congreso, sistema judicial, Iglesia, policía, FFAA, partidos.

* **`indicadores_latino_region`** y **`indicadores_latino_ciudad`**

  * Usan claves `pais-region` y `pais-region-ciudad`.
  * Exponen el mismo conjunto de tasas, desagregadas por región y ciudad dentro de cada país.

---

## 6. V-Dem

### 6.1 Tabla `vdem`

* **Propósito**: almacenar indicadores de democracia de la base V-Dem.
* **Campos principales**:

  * Identificadores:

    * `country_name`, `country_text_id`, `country_id`.
    * `year`, `historical_date`.
    * Códigos (`project`, `historical`, `COWcode`).
  * Rango de codificación y gaps:

    * `codingstart`, `codingend`, `codingstart_contemp`, `codingend_contemp`.
    * `codingstart_hist`, `codingend_hist`.
    * `gapstartX`, `gapendX`, `gap_index`.
  * Índices democráticos:

    * `v2x_polyarchy` (índice de poliarquía).
    * `v2x_libdem` (índice de democracia liberal).
    * `v2x_partipdem` (democracia participativa).
    * `v2x_delibdem` (democracia deliberativa).
    * `v2x_egaldem` (democracia igualitaria).
  * Derechos y libertades:

    * `v2x_freexp_altinf` (libertad de expresión y fuentes alternativas de información).
    * `v2xel_frefair` (elecciones libres y justas).
    * `v2xcl_rol` (rule of law).
    * `v2x_jucon` (independencia y poder judicial).
    * `v2xlg_legcon`, `v2xeg_eqprotec`, `v2xeg_eqaccess`, `v2xeg_eqdr`.
  * Distribución de poder:

    * `v2pepwrses`, `v2pepwrsoc`, `v2pepwrgen`, `v2pepwrort`, `v2pepwrgeo`.

Esta tabla se ingesta desde los CSV procesados por los scripts de automatización y puede ser utilizada directamente por Superset o combinada con otras fuentes (ENEMDU, Latinobarómetro) a nivel de dashboards.

---

## 7. Notas finales

* Todas las tablas y vistas descritas se crean automáticamente al iniciar `clickhouse_server` mediante el script `create_table.sql`.
* Para extender el modelo (nuevos indicadores o vistas):

  * Añadir nuevas columnas o vistas al SQL de inicialización.
  * Ajustar los scripts de ingesta si es necesario.
* Es recomendable documentar cualquier cambio en este archivo (`DATABASE.md`) para mantener alineados el código SQL y la documentación.
