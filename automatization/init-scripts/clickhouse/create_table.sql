-- ===================================================
-- Base de datos
-- ===================================================
CREATE DATABASE IF NOT EXISTS indicadores;

-- ===================================================
-- Tabla ENEMDU Persona
-- ===================================================
-- DROP TABLE IF EXISTS indicadores.enemdu_persona;
CREATE TABLE IF NOT EXISTS indicadores.enemdu_persona (
  periodo String,
  zona Nullable(String),
  sector Nullable(String),
  condact Nullable(Int32),
  desempleo Nullable(Int32),
  empleo Nullable(Int32),
  estrato Nullable(Int32),
  nnivins Nullable(Int32),
  secemp Nullable(Int32),
  rama1 Nullable(Int32),
  upm Nullable(String),
  vivienda Nullable(Int32),
  pobreza Nullable(Int32),
  epobreza Nullable(Int32),
  fexp Nullable(Float64),
  ingpc Nullable(Float64),
  ingrl Nullable(Float64),
  grupo1 Nullable(String),
  hogar Nullable(String),
  id_hogar Nullable(String),
  id_persona Nullable(String),
  id_vivienda Nullable(String),
  area Nullable(String),
  ciudad Nullable(String),
  cod_inf Nullable(String),
  panelm Nullable(String),
  p01 Nullable(Int32),
  p02 Nullable(Int32),
  p03 Nullable(Int32),
  p04 Nullable(Int32),
  p05a Nullable(Int32),
  p05b Nullable(Int32),
  p06 Nullable(Int32),
  p07 Nullable(Int32),
  p09 Nullable(Int32),
  p10a Nullable(Int32),
  p10b Nullable(Int32),
  p15 Nullable(Int32),
  p20 Nullable(Int32),
  p21 Nullable(Int32),
  p22 Nullable(Int32),
  p23 Nullable(Int32),
  p24 Nullable(Int32),
  p25 Nullable(Int32),
  p26 Nullable(Int32),
  p27 Nullable(Int32),
  p28 Nullable(Int32),
  p29 Nullable(Int32),
  p32 Nullable(Int32),
  p33 Nullable(Int32),
  p34 Nullable(Int32),
  p35 Nullable(Int32),
  p36 Nullable(Int32),
  p37 Nullable(Int32),
  p38 Nullable(Int32),
  p39 Nullable(Int32),
  p40 Nullable(Int32),
  p41 Nullable(Int32),
  p42 Nullable(Int32),
  p44f Nullable(Int32),
  p46 Nullable(Int32),
  p47a Nullable(Int32),
  p47b Nullable(Int32),
  p49 Nullable(Int32),
  p50 Nullable(Int32),
  p51a Nullable(Int32),
  p51b Nullable(Int32),
  p51c Nullable(Int32),
  p55 Nullable(Int32),
  p56a Nullable(Int32),
  p56b Nullable(Int32),
  p58 Nullable(Int32),
  p63 Nullable(Int32),
  p64a Nullable(Int32),
  p64b Nullable(Int32),
  p65 Nullable(Int32),
  p66 Nullable(Int32),
  p67 Nullable(Int32),
  p68a Nullable(Int32),
  p68b Nullable(Int32),
  p69 Nullable(Int32),
  p70a Nullable(Int32),
  p70b Nullable(Int32),
  p71a Nullable(Int32),
  p71b Nullable(Int32),
  p72a Nullable(Int32),
  p72b Nullable(Int32),
  p73a Nullable(Int32),
  p73b Nullable(Int32),
  p74a Nullable(Int32),
  p74b Nullable(Int32),
  p75 Nullable(Int32),
  p76 Nullable(Int32),
  p77 Nullable(Int32)
) ENGINE = MergeTree
ORDER BY (periodo) SETTINGS index_granularity = 8192;

-- ===================================================
-- Tabla ENEMDU Vivienda
-- ===================================================
-- DROP TABLE IF EXISTS indicadores.enemdu_vivienda;
CREATE TABLE IF NOT EXISTS indicadores.enemdu_vivienda (
  periodo String,
  area Nullable(String),
  ciudad Nullable(String),
  zona Nullable(String),
  conglomerado Nullable(String),
  estrato Nullable(String),
  fexp Nullable(Float64),
  hogar Nullable(String),
  id_hogar Nullable(String),
  id_vivienda Nullable(String),
  vivienda Nullable(Int32),
  panelm Nullable(String),
  sector Nullable(String),
  upm Nullable(String),
  vi01 Nullable(Int32),
  vi02 Nullable(Int32),
  vi03a Nullable(Int32),
  vi03b Nullable(Int32),
  vi04a Nullable(Int32),
  vi04b Nullable(Int32),
  vi05a Nullable(Int32),
  vi05b Nullable(Int32),
  vi06 Nullable(Int32),
  vi07 Nullable(Int32),
  vi07a Nullable(Int32),
  vi07b Nullable(Int32),
  vi08 Nullable(Int32),
  vi09 Nullable(Int32),
  vi09a Nullable(Int32),
  vi09b Nullable(Int32),
  vi10 Nullable(Int32),
  vi101 Nullable(Int32),
  vi102 Nullable(Int32),
  vi10a Nullable(Int32),
  vi11 Nullable(Int32),
  vi12 Nullable(Int32),
  vi13 Nullable(Int32),
  vi14 Nullable(Int32),
  vi141 Nullable(Int32),
  vi142 Nullable(Int32),
  vi143 Nullable(Int32),
  vi144 Nullable(Int32),
  vi1511 Nullable(Int32),
  vi1512 Nullable(Int32),
  vi1521 Nullable(Int32),
  vi1522 Nullable(Int32),
  vi1531 Nullable(Int32),
  vi1532 Nullable(Int32),
  vi1533 Nullable(Int32),
  vi1534 Nullable(Int32),
  vi1541 Nullable(Int32),
  vi1542 Nullable(Int32),
  vi1543 Nullable(Int32),
  vi1544 Nullable(Int32),
  vi1551 Nullable(Int32),
  vi1552 Nullable(Int32),
  vi1553 Nullable(Int32),
  vi1554 Nullable(Int32),
  vi1561 Nullable(Int32),
  vi1562 Nullable(Int32),
  vi1563 Nullable(Int32),
  vi1564 Nullable(Int32),
  vi16 Nullable(Int32),
  vi161 Nullable(Int32),
  vi162 Nullable(Int32),
  vi163 Nullable(Int32),
  vi164 Nullable(Int32),
  vi165 Nullable(Int32),
  vi166 Nullable(Int32),
  vi167 Nullable(Int32),
  vi168 Nullable(Int32),
  vi169 Nullable(Int32),
  vi1610 Nullable(Int32),
  vi1611 Nullable(Int32),
  vi1612 Nullable(Int32),
  vi1613 Nullable(Int32),
  vi1614 Nullable(Int32),
  vi17 Nullable(Int32),
  vi171 Nullable(Int32),
  vi172 Nullable(Int32),
  vi173 Nullable(Int32),
  vi174 Nullable(Int32),
  vi175 Nullable(Int32),
  vi176 Nullable(Int32),
  vi177 Nullable(Int32),
  vi178 Nullable(Int32),
  vi179 Nullable(Int32),
  vi1710 Nullable(Int32),
  vi1711 Nullable(Int32),
  vi1712 Nullable(Int32),
  vi1713 Nullable(Int32),
  vi1714 Nullable(Int32),
  vi18 Nullable(Int32),
  vi181 Nullable(Int32),
  vi182 Nullable(Int32),
  vi183 Nullable(Int32),
  vi184 Nullable(Int32),
  vi185 Nullable(Int32),
  vi186 Nullable(Int32),
  vi187 Nullable(Int32),
  vi188 Nullable(Int32),
  vi189 Nullable(Int32),
  vi1810 Nullable(Int32),
  vi1811 Nullable(Int32),
  vi1812 Nullable(Int32),
  vi1813 Nullable(Int32),
  vi1814 Nullable(Int32)
) ENGINE = MergeTree()
ORDER BY (periodo);

-- ===================================================
-- Líneas de pobreza
-- ===================================================
CREATE TABLE IF NOT EXISTS indicadores.poverty_lines (
  periodo String,
  linea_pobreza Float64,
  linea_pobreza_extrema Float64
) ENGINE = MergeTree
ORDER BY (periodo);

-- DROP TABLE IF EXISTS indicadores.sbu_hist;
CREATE TABLE IF NOT EXISTS indicadores.sbu_hist (
  periodo String,  -- 'YYYYMM'
  sbu Float64 -- salario básico unificado del periodo
) ENGINE = MergeTree
ORDER BY (periodo);

-- ===================================================
-- Tabla de acumulados PERSONA (claves no nulas)
-- ===================================================
-- DROP TABLE IF EXISTS indicadores.persona_sums;
CREATE TABLE IF NOT EXISTS indicadores.persona_sums (
  level LowCardinality(String),
  anio UInt16,
  periodo UInt8,  -- 0 = anual
  area UInt8,     -- 0 = sin área
  geo String,     -- '' = nacional
  sw_pop Float64,
  sw_pet Float64,
  sw_pea Float64,
  sw_occ Float64,
  s_emp_adecuado Float64,
  s_subempleo Float64,
  s_no_remu Float64,
  s_otro_no_pleno Float64,
  s_formal_w Float64,
  s_informal_w Float64,
  pea_h Float64,
  pea_m Float64,
  ade_h Float64,
  ade_m Float64,
  occ_inc_w_h Float64,
  occ_w_h Float64,
  occ_inc_w_m Float64,
  occ_w_m Float64,
  s_youth Float64,
  s_youth_nini Float64,
  s_juv_pea Float64,
  s_juv_des Float64,
  s_kids Float64,
  s_ti Float64,
  s_occ_manu Float64,
  s_5_24 Float64,
  s_asist_5_24 Float64,
  s_valid_lp Float64,
  s_under_lp Float64,
  s_under_lp_ext Float64
) ENGINE = SummingMergeTree
ORDER BY (level, anio, periodo, area, geo);

-- ===================================================
-- MV PERSONA → persona_sums
-- ===================================================
DROP VIEW IF EXISTS indicadores.mv_persona_all_levels;
CREATE MATERIALIZED VIEW indicadores.mv_persona_all_levels TO indicadores.persona_sums AS
SELECT 
  tup.1 AS level,
  tup.2 AS anio,
  tup.3 AS periodo,
  tup.4 AS area,
  tup.5 AS geo,
  sum(w) AS sw_pop,
  sumIf(w, is_pet) AS sw_pet,
  sumIf(w, is_pea) AS sw_pea,
  sumIf(w, is_occ) AS sw_occ,
  sumIf(w, is_occ AND stat = 1) AS s_emp_adecuado,
  sumIf(w, is_occ AND stat IN (2, 3)) AS s_subempleo,
  sumIf(w, is_occ AND stat = 5) AS s_no_remu,
  sumIf(w, is_occ AND stat = 4) AS s_otro_no_pleno,
  sumIf(w, is_occ AND sector = 1) AS s_formal_w,
  sumIf(w, is_occ AND sector = 2) AS s_informal_w,
  sumIf(w, is_pea AND sexo = 1) AS pea_h,
  sumIf(w, is_pea AND sexo = 2) AS pea_m,
  sumIf(w, is_occ AND stat = 1  AND sexo = 1) AS ade_h,
  sumIf(w, is_occ AND stat = 1 AND sexo = 2) AS ade_m,
  sumIf(w * ingrl_v, is_occ AND sexo = 1 AND ingrl_v >= 0 AND ingrl_v < 999999) AS occ_inc_w_h,
  sumIf(w, is_occ AND sexo = 1 AND ingrl_v >= 0 AND ingrl_v < 999999) AS occ_w_h,
  sumIf(w * ingrl_v, is_occ AND sexo = 2 AND ingrl_v >= 0 AND ingrl_v < 999999) AS occ_inc_w_m,
  sumIf(w, is_occ AND sexo = 2 AND ingrl_v >= 0 AND ingrl_v < 999999) AS occ_w_m,
  sumIf(w, edad_i BETWEEN 15 AND 24) AS s_youth,
  sumIf(w, edad_i BETWEEN 15 AND 24 AND no_est AND no_trab) AS s_youth_nini,
  sumIf(w, edad_i BETWEEN 18 AND 29 AND is_pea) AS s_juv_pea,
  sumIf(w, edad_i BETWEEN 18 AND 29 AND stat IN (7, 8)) AS s_juv_des,
  sumIf(w, edad_i BETWEEN 5 AND 14) AS s_kids,
  sumIf(w, edad_i BETWEEN 5 AND 14 AND (stat BETWEEN 1 AND 6 OR horas > 0)) AS s_ti,
  sumIf(w, is_occ AND rama = 3) AS s_occ_manu,
  sumIf(w, edad_i BETWEEN 5 AND 24) AS s_5_24,
  sumIf(w, (edad_i BETWEEN 5 AND 24) AND asiste) AS s_asist_5_24,
  sumIf(w, lp_ok) AS s_valid_lp,
  sumIf(w, lp_ok AND ingpc_v < lp) AS s_under_lp,
  sumIf(w, lp_ok AND ingpc_v < lpe) AS s_under_lp_ext
FROM (
  SELECT p.*,
    ifNull(p.fexp, 0.0) AS w,
    ifNull(p.p03, 0) AS edad_i,
    ifNull(p.p02, 0) AS sexo,
    ifNull(p.condact, 0) AS stat,
    ifNull(p.p24, 0) AS horas,
    ifNull(p.rama1, 0) AS rama,
    ifNull(p.ingrl, -1.0) AS ingrl_v,
    ifNull(p.ingpc, 0.0) AS ingpc_v,
    (ifNull(p.p03, 0) >= 15 AND ifNull(p.fexp, 0.0) > 0) AS is_pet,
    (ifNull(p.p03, 0) >= 15 AND ifNull(p.fexp, 0.0) > 0 AND ifNull(p.condact, 0) BETWEEN 1 AND 8) AS is_pea,
    (ifNull(p.p03, 0) >= 15 AND ifNull(p.fexp, 0.0) > 0 AND ifNull(p.condact, 0) BETWEEN 1 AND 6) AS is_occ,
    -- (ifNull(p.empleo, 0) = 1)  AS has_empleo,
    multiIf(ifNull(p.p42, 0) = 10, 3, ifNull(p.p47a, 0) = 2, 1, (ifNull(p.p47a, 0) = 1 AND ifNull(p.p49, 0) = 1), 1, (ifNull(p.p47a, 0) = 1 AND ifNull(p.p49, 0) != 1), 2, 4) AS sec_calc,
    ifNull(p.secemp, sec_calc) AS sector,
    (ifNull(p.p07, 0) = 2) AS no_est,
    (ifNull(p.condact, 0) IN (7, 8, 9)) AS no_trab,
    (ifNull(p.p07, 0) = 1) AS asiste,
    replaceRegexpAll(toString(p.ciudad), '[^0-9]', '') AS geo_digits,
    substring(geo_digits, 1, 2) AS prov2,
    substring(geo_digits, 1, 4) AS cant4,
    substring(geo_digits, 1, 6) AS parr6,
    ifNull(
      toUInt8OrNull(p.area),
      multiIf(
        positionCaseInsensitive(p.area, 'urbano') > 0, toUInt8(1),
        positionCaseInsensitive(p.area, 'rural')  > 0, toUInt8(2),
        CAST(NULL, 'Nullable(UInt8)')
      )
    ) AS area_n,
    toUInt16(substring(p.periodo, 1, 4)) AS anio_i,
    toUInt8(substring(p.periodo, 5, 2))  AS per_i,
    pl.linea_pobreza AS lp,
    pl.linea_pobreza_extrema AS lpe,
    (pl.linea_pobreza IS NOT NULL AND pl.linea_pobreza_extrema IS NOT NULL AND ifNull(p.fexp, 0.0) > 0 AND ifNull(p.ingpc, 0.0) > 0) AS lp_ok
  FROM indicadores.enemdu_persona AS p
  LEFT JOIN indicadores.poverty_lines AS pl ON pl.periodo = p.periodo
) AS base
ARRAY JOIN [
  ('nacional',            anio_i, per_i, ifNull(area_n, toUInt8(0)), ''           ),
  ('provincia',           anio_i, per_i, ifNull(area_n, toUInt8(0)), ifNull(prov2,'') ),
  ('canton',              anio_i, per_i, ifNull(area_n, toUInt8(0)), ifNull(cant4,'') ),
  ('parroquia',           anio_i, per_i, ifNull(area_n, toUInt8(0)), ifNull(parr6,'') ),
  ('nacional_sin_area',   anio_i, per_i, toUInt8(0),                  ''           ),
  ('parroquial_sin_area', anio_i, per_i, toUInt8(0),                  ifNull(parr6,'') ),
  ('canton_anual',        anio_i, toUInt8(0), toUInt8(0),             ifNull(cant4,'') )
] AS tup
WHERE
      (tup.1 = 'nacional'             AND length(tup.5) = 0 AND tup.3 > 0 AND tup.4 IN (0,1,2))
  OR  (tup.1 = 'provincia'            AND length(tup.5) = 2 AND tup.3 > 0 AND tup.4 IN (0,1,2))
  OR  (tup.1 = 'canton'               AND length(tup.5) = 4 AND tup.3 > 0 AND tup.4 IN (0,1,2))
  OR  (tup.1 = 'parroquia'            AND length(tup.5) = 6 AND tup.3 > 0 AND tup.4 IN (0,1,2))
  OR  (tup.1 = 'nacional_sin_area'    AND length(tup.5) = 0 AND tup.3 > 0 AND tup.4 = 0)
  OR  (tup.1 = 'parroquial_sin_area'  AND length(tup.5) = 6 AND tup.3 > 0 AND tup.4 = 0)
  OR  (tup.1 = 'canton_anual'         AND length(tup.5) = 4 AND tup.3 = 0 AND tup.4 = 0)
GROUP BY level, anio, periodo, area, geo;

-- ===================================================
-- Vistas PERSONA (consumen persona_sums)
-- ===================================================
CREATE OR REPLACE VIEW indicadores.indicadores_persona_nacional AS
SELECT
  anio,
  periodo,
  multiIf(periodo=1,'Enero', periodo=2,'Febrero', periodo=3,'Marzo', periodo=4,'Abril',
          periodo=5,'Mayo',  periodo=6,'Junio',   periodo=7,'Julio', periodo=8,'Agosto',
          periodo=9,'Septiembre', periodo=10,'Octubre', periodo=11,'Noviembre','Diciembre') AS mes,
  area,
  round(100 * sum(sw_pea) / nullIf(sum(sw_pet), 0), 4) AS tasa_participacion_global,
  round(100 * sum(sw_pea) / nullIf(sum(sw_pop), 0), 4) AS tasa_participacion_bruta,
  round(100 * (sum(sw_pea) - sum(sw_occ)) / nullIf(sum(sw_pea), 0), 4) AS tasa_desempleo,
  round(100 * sum(sw_occ) / nullIf(sum(sw_pea), 0), 4) AS empleo_total,
  round(100 * sum(s_formal_w) / nullIf(sum(sw_occ), 0), 4) AS empleo_formal,
  round(100 * sum(s_informal_w) / nullIf(sum(sw_occ), 0), 4) AS empleo_informal,
  round(100 * sum(s_emp_adecuado) / nullIf(sum(sw_pea), 0), 4) AS empleo_adecuado,
  round(100 * sum(s_subempleo) / nullIf(sum(sw_pea), 0), 4) AS subempleo,
  round(100 * sum(s_no_remu) / nullIf(sum(sw_pea), 0), 4) AS no_remunerado,
  round(100 * sum(s_otro_no_pleno) / nullIf(sum(sw_pea), 0), 4) AS otro_no_pleno,
  round(
    100 * ((sum(ade_h) / nullIf(sum(pea_h), 0)) - (sum(ade_m) / nullIf(sum(pea_m), 0)))
        / nullIf(sum(ade_h) / nullIf(sum(pea_h), 0), 0), 4
  ) AS brecha_adecuado_HM,
  round(
    100 * ((sum(occ_inc_w_h) / nullIf(sum(occ_w_h), 0)) - (sum(occ_inc_w_m) / nullIf(sum(occ_w_m), 0)))
        / nullIf(sum(occ_inc_w_h) / nullIf(sum(occ_w_h), 0), 0), 4
  ) AS brecha_salarial_HM,
  round(100 * sum(s_youth_nini) / nullIf(sum(s_youth), 0), 4) AS NiNi,
  round(100 * sum(s_juv_des) / nullIf(sum(s_juv_pea), 0), 4) AS desempleo_juvenil,
  round(100 * sum(s_ti) / nullIf(sum(s_kids), 0), 4) AS trabajo_infantil,
  round(100 * sum(s_asist_5_24) / nullIf(sum(s_5_24), 0), 4) AS tasa_asistencia_clases,
  round(100 * sum(s_occ_manu) / nullIf(sum(sw_occ), 0), 4) AS empleo_manufactura,
  round(100 * sum(s_under_lp) / nullIf(sum(s_valid_lp), 0), 4) AS pobreza_ingresos,
  round(100 * sum(s_under_lp_ext) / nullIf(sum(s_valid_lp), 0), 4) AS pobreza_extrema_ingresos
FROM indicadores.persona_sums
WHERE level = 'nacional'
GROUP BY anio, periodo, area
ORDER BY anio, periodo, area;

CREATE OR REPLACE VIEW indicadores.indicadores_persona_provincia AS
SELECT
  anio, periodo,
  multiIf(periodo=1,'Enero', periodo=2,'Febrero', periodo=3,'Marzo', periodo=4,'Abril',
          periodo=5,'Mayo',  periodo=6,'Junio',   periodo=7,'Julio', periodo=8,'Agosto',
          periodo=9,'Septiembre', periodo=10,'Octubre', periodo=11,'Noviembre','Diciembre') AS mes,
  area,
  geo AS provincia,
  round(100 * sum(sw_pea) / nullIf(sum(sw_pet), 0), 4) AS tasa_participacion_global,
  round(100 * sum(sw_pea) / nullIf(sum(sw_pop), 0), 4) AS tasa_participacion_bruta,
  round(100 * (sum(sw_pea) - sum(sw_occ)) / nullIf(sum(sw_pea), 0), 4) AS tasa_desempleo,
  round(100 * sum(sw_occ) / nullIf(sum(sw_pea), 0), 4) AS empleo_total,
  round(100 * sum(s_formal_w) / nullIf(sum(sw_occ), 0), 4) AS empleo_formal,
  round(100 * sum(s_informal_w) / nullIf(sum(sw_occ), 0), 4) AS empleo_informal,
  round(100 * sum(s_emp_adecuado) / nullIf(sum(sw_pea), 0), 4) AS empleo_adecuado,
  round(100 * sum(s_subempleo) / nullIf(sum(sw_pea), 0), 4) AS subempleo,
  round(100 * sum(s_no_remu) / nullIf(sum(sw_pea), 0), 4) AS no_remunerado,
  round(100 * sum(s_otro_no_pleno) / nullIf(sum(sw_pea), 0), 4) AS otro_no_pleno,
  round(
    100 * ((sum(ade_h) / nullIf(sum(pea_h), 0)) - (sum(ade_m) / nullIf(sum(pea_m), 0)))
        / nullIf(sum(ade_h) / nullIf(sum(pea_h), 0), 0), 4
  ) AS brecha_adecuado_HM,
  round(
    100 * ((sum(occ_inc_w_h) / nullIf(sum(occ_w_h), 0)) - (sum(occ_inc_w_m) / nullIf(sum(occ_w_m), 0)))
        / nullIf(sum(occ_inc_w_h) / nullIf(sum(occ_w_h), 0), 0), 4
  ) AS brecha_salarial_HM,
  round(100 * sum(s_youth_nini) / nullIf(sum(s_youth), 0), 4) AS NiNi,
  round(100 * sum(s_juv_des) / nullIf(sum(s_juv_pea), 0), 4) AS desempleo_juvenil,
  round(100 * sum(s_ti) / nullIf(sum(s_kids), 0), 4) AS trabajo_infantil,
  round(100 * sum(s_occ_manu) / nullIf(sum(sw_occ), 0), 4) AS empleo_manufactura,
  round(100 * sum(s_asist_5_24) / nullIf(sum(s_5_24), 0), 4) AS tasa_asistencia_clases,
  round(100 * sum(s_under_lp) / nullIf(sum(s_valid_lp), 0), 4) AS pobreza_ingresos,
  round(100 * sum(s_under_lp_ext) / nullIf(sum(s_valid_lp), 0), 4) AS pobreza_extrema_ingresos
FROM indicadores.persona_sums
WHERE level = 'provincia'
GROUP BY anio, periodo, area, provincia
ORDER BY anio, periodo, area, provincia;

CREATE OR REPLACE VIEW indicadores.indicadores_persona_canton AS
SELECT
  anio, periodo,
  multiIf(periodo=1,'Enero', periodo=2,'Febrero', periodo=3,'Marzo', periodo=4,'Abril',
          periodo=5,'Mayo',  periodo=6,'Junio',   periodo=7,'Julio', periodo=8,'Agosto',
          periodo=9,'Septiembre', periodo=10,'Octubre', periodo=11,'Noviembre','Diciembre') AS mes,
  area,
  geo AS canton,
  round(100 * sum(sw_pea) / nullIf(sum(sw_pet), 0), 4) AS tasa_participacion_global,
  round(100 * sum(sw_pea) / nullIf(sum(sw_pop), 0), 4) AS tasa_participacion_bruta,
  round(100 * (sum(sw_pea) - sum(sw_occ)) / nullIf(sum(sw_pea), 0), 4) AS tasa_desempleo,
  round(100 * sum(sw_occ) / nullIf(sum(sw_pea), 0), 4) AS empleo_total,
  round(100 * sum(s_formal_w) / nullIf(sum(sw_occ), 0), 4) AS empleo_formal,
  round(100 * sum(s_informal_w) / nullIf(sum(sw_occ), 0), 4) AS empleo_informal,
  round(100 * sum(s_emp_adecuado) / nullIf(sum(sw_pea), 0), 4) AS empleo_adecuado,
  round(100 * sum(s_subempleo) / nullIf(sum(sw_pea), 0), 4) AS subempleo,
  round(100 * sum(s_no_remu) / nullIf(sum(sw_pea), 0), 4) AS no_remunerado,
  round(100 * sum(s_otro_no_pleno) / nullIf(sum(sw_pea), 0), 4) AS otro_no_pleno,
  round(
    100 * ((sum(ade_h) / nullIf(sum(pea_h), 0)) - (sum(ade_m) / nullIf(sum(pea_m), 0)))
        / nullIf(sum(ade_h) / nullIf(sum(pea_h), 0), 0), 4
  ) AS brecha_adecuado_HM,
  round(
    100 * ((sum(occ_inc_w_h) / nullIf(sum(occ_w_h), 0)) - (sum(occ_inc_w_m) / nullIf(sum(occ_w_m), 0)))
        / nullIf(sum(occ_inc_w_h) / nullIf(sum(occ_w_h), 0), 0), 4
  ) AS brecha_salarial_HM,
  round(100 * sum(s_youth_nini) / nullIf(sum(s_youth), 0), 4) AS NiNi,
  round(100 * sum(s_juv_des) / nullIf(sum(s_juv_pea), 0), 4) AS desempleo_juvenil,
  round(100 * sum(s_ti) / nullIf(sum(s_kids), 0), 4) AS trabajo_infantil,
  round(100 * sum(s_occ_manu) / nullIf(sum(sw_occ), 0), 4) AS empleo_manufactura,
  round(100 * sum(s_asist_5_24) / nullIf(sum(s_5_24), 0), 4) AS tasa_asistencia_clases,
  round(100 * sum(s_under_lp) / nullIf(sum(s_valid_lp), 0), 4) AS pobreza_ingresos,
  round(100 * sum(s_under_lp_ext) / nullIf(sum(s_valid_lp), 0), 4) AS pobreza_extrema_ingresos
FROM indicadores.persona_sums
WHERE level = 'canton'
GROUP BY anio, periodo, area, canton
ORDER BY anio, periodo, area, canton;

CREATE OR REPLACE VIEW indicadores.indicadores_persona_parroquia AS
SELECT
  anio, periodo,
  multiIf(periodo=1,'Enero', periodo=2,'Febrero', periodo=3,'Marzo', periodo=4,'Abril',
          periodo=5,'Mayo',  periodo=6,'Junio',   periodo=7,'Julio', periodo=8,'Agosto',
          periodo=9,'Septiembre', periodo=10,'Octubre', periodo=11,'Noviembre','Diciembre') AS mes,
  area,
  geo AS ciudad,
  round(100 * sum(sw_pea) / nullIf(sum(sw_pet), 0), 4) AS tasa_participacion_global,
  round(100 * sum(sw_pea) / nullIf(sum(sw_pop), 0), 4) AS tasa_participacion_bruta,
  round(100 * (sum(sw_pea) - sum(sw_occ)) / nullIf(sum(sw_pea), 0), 4) AS tasa_desempleo,
  round(100 * sum(sw_occ) / nullIf(sum(sw_pea), 0), 4) AS empleo_total,
  round(100 * sum(s_formal_w) / nullIf(sum(sw_occ), 0), 4) AS empleo_formal,
  round(100 * sum(s_informal_w) / nullIf(sum(sw_occ), 0), 4) AS empleo_informal,
  round(100 * sum(s_emp_adecuado) / nullIf(sum(sw_pea), 0), 4) AS empleo_adecuado,
  round(100 * sum(s_subempleo) / nullIf(sum(sw_pea), 0), 4) AS subempleo,
  round(100 * sum(s_no_remu) / nullIf(sum(sw_pea), 0), 4) AS no_remunerado,
  round(100 * sum(s_otro_no_pleno) / nullIf(sum(sw_pea), 0), 4) AS otro_no_pleno,
  round(
    100 * ((sum(ade_h) / nullIf(sum(pea_h), 0)) - (sum(ade_m) / nullIf(sum(pea_m), 0)))
        / nullIf(sum(ade_h) / nullIf(sum(pea_h), 0), 0), 4
  ) AS brecha_adecuado_HM,
  round(
    100 * ((sum(occ_inc_w_h) / nullIf(sum(occ_w_h), 0)) - (sum(occ_inc_w_m) / nullIf(sum(occ_w_m), 0)))
        / nullIf(sum(occ_inc_w_h) / nullIf(sum(occ_w_h), 0), 0), 4
  ) AS brecha_salarial_HM,
  round(100 * sum(s_youth_nini) / nullIf(sum(s_youth), 0), 4) AS NiNi,
  round(100 * sum(s_juv_des) / nullIf(sum(s_juv_pea), 0), 4) AS desempleo_juvenil,
  round(100 * sum(s_ti) / nullIf(sum(s_kids), 0), 4) AS trabajo_infantil,
  round(100 * sum(s_occ_manu) / nullIf(sum(sw_occ), 0), 4) AS empleo_manufactura,
  round(100 * sum(s_asist_5_24) / nullIf(sum(s_5_24), 0), 4) AS tasa_asistencia_clases,
  round(100 * sum(s_under_lp) / nullIf(sum(s_valid_lp), 0), 4) AS pobreza_ingresos,
  round(100 * sum(s_under_lp_ext) / nullIf(sum(s_valid_lp), 0), 4) AS pobreza_extrema_ingresos
FROM indicadores.persona_sums
WHERE level = 'parroquia'
GROUP BY anio, periodo, area, ciudad
ORDER BY anio, periodo, area, ciudad;

CREATE OR REPLACE VIEW indicadores.indicadores_persona_canton_anual AS
SELECT
  anio,
  geo AS canton,
  round(100 * sum(sw_pea) / nullIf(sum(sw_pet), 0), 4) AS tasa_participacion_global,
  round(100 * sum(sw_pea) / nullIf(sum(sw_pop), 0), 4) AS tasa_participacion_bruta,
  round(100 * (sum(sw_pea) - sum(sw_occ)) / nullIf(sum(sw_pea), 0), 4) AS tasa_desempleo,
  round(100 * sum(sw_occ) / nullIf(sum(sw_pea), 0), 4) AS empleo_total,
  round(100 * sum(s_formal_w) / nullIf(sum(sw_occ), 0), 4) AS empleo_formal,
  round(100 * sum(s_informal_w) / nullIf(sum(sw_occ), 0), 4) AS empleo_informal,
  round(100 * sum(s_emp_adecuado) / nullIf(sum(sw_pea), 0), 4) AS empleo_adecuado,
  round(100 * sum(s_subempleo) / nullIf(sum(sw_pea), 0), 4) AS subempleo,
  round(100 * sum(s_no_remu) / nullIf(sum(sw_pea), 0), 4) AS no_remunerado,
  round(100 * sum(s_otro_no_pleno) / nullIf(sum(sw_pea), 0), 4) AS otro_no_pleno,
  round(
    100 * ((sum(ade_h) / nullIf(sum(pea_h), 0)) - (sum(ade_m) / nullIf(sum(pea_m), 0)))
        / nullIf(sum(ade_h) / nullIf(sum(pea_h), 0), 0), 4
  ) AS brecha_adecuado_HM,
  round(
    100 * ((sum(occ_inc_w_h) / nullIf(sum(occ_w_h), 0)) - (sum(occ_inc_w_m) / nullIf(sum(occ_w_m), 0)))
        / nullIf(sum(occ_inc_w_h) / nullIf(sum(occ_w_h), 0), 0), 4
  ) AS brecha_salarial_HM,
  round(100 * sum(s_youth_nini) / nullIf(sum(s_youth), 0), 4) AS NiNi,
  round(100 * sum(s_juv_des) / nullIf(sum(s_juv_pea), 0), 4) AS desempleo_juvenil,
  round(100 * sum(s_ti) / nullIf(sum(s_kids), 0), 4) AS trabajo_infantil,
  round(100 * sum(s_occ_manu) / nullIf(sum(sw_occ), 0), 4) AS empleo_manufactura,
  round(100 * sum(s_asist_5_24) / nullIf(sum(s_5_24), 0), 4) AS tasa_asistencia_clases,
  round(100 * sum(s_under_lp) / nullIf(sum(s_valid_lp), 0), 4) AS pobreza_ingresos,
  round(100 * sum(s_under_lp_ext) / nullIf(sum(s_valid_lp), 0), 4) AS pobreza_extrema_ingresos
FROM indicadores.persona_sums
WHERE level = 'canton_anual'
GROUP BY anio, canton
ORDER BY anio, canton;

CREATE OR REPLACE VIEW indicadores.indicadores_persona_nacional_por_periodo AS
SELECT
  anio, periodo,
  multiIf(periodo=1,'Enero', periodo=2,'Febrero', periodo=3,'Marzo', periodo=4,'Abril',
          periodo=5,'Mayo',  periodo=6,'Junio',   periodo=7,'Julio', periodo=8,'Agosto',
          periodo=9,'Septiembre', periodo=10,'Octubre', periodo=11,'Noviembre','Diciembre') AS mes,
  round(100 * sum(sw_pea) / nullIf(sum(sw_pet), 0), 4) AS tasa_participacion_global,
  round(100 * sum(sw_pea) / nullIf(sum(sw_pop), 0), 4) AS tasa_participacion_bruta,
  round(100 * (sum(sw_pea) - sum(sw_occ)) / nullIf(sum(sw_pea), 0), 4) AS tasa_desempleo,
  round(100 * sum(sw_occ) / nullIf(sum(sw_pea), 0), 4) AS empleo_total,
  round(100 * sum(s_formal_w) / nullIf(sum(sw_occ), 0), 4) AS empleo_formal,
  round(100 * sum(s_informal_w) / nullIf(sum(sw_occ), 0), 4) AS empleo_informal,
  round(100 * sum(s_emp_adecuado) / nullIf(sum(sw_pea), 0), 4) AS empleo_adecuado,
  round(100 * sum(s_subempleo) / nullIf(sum(sw_pea), 0), 4) AS subempleo,
  round(100 * sum(s_no_remu) / nullIf(sum(sw_pea), 0), 4) AS no_remunerado,
  round(100 * sum(s_otro_no_pleno) / nullIf(sum(sw_pea), 0), 4) AS otro_no_pleno,
  round(
    100 * ((sum(ade_h) / nullIf(sum(pea_h), 0)) - (sum(ade_m) / nullIf(sum(pea_m), 0)))
        / nullIf(sum(ade_h) / nullIf(sum(pea_h), 0), 0), 4
  ) AS brecha_adecuado_HM,
  round(
    100 * ((sum(occ_inc_w_h) / nullIf(sum(occ_w_h), 0)) - (sum(occ_inc_w_m) / nullIf(sum(occ_w_m), 0)))
        / nullIf(sum(occ_inc_w_h) / nullIf(sum(occ_w_h), 0), 0), 4
  ) AS brecha_salarial_HM,
  round(100 * sum(s_youth_nini) / nullIf(sum(s_youth), 0), 4) AS NiNi,
  round(100 * sum(s_juv_des) / nullIf(sum(s_juv_pea), 0), 4) AS desempleo_juvenil,
  round(100 * sum(s_ti) / nullIf(sum(s_kids), 0), 4) AS trabajo_infantil,
  round(100 * sum(s_occ_manu) / nullIf(sum(sw_occ), 0), 4) AS empleo_manufactura,
  round(100 * sum(s_asist_5_24) / nullIf(sum(s_5_24), 0), 4) AS tasa_asistencia_clases,
  round(100 * sum(s_under_lp) / nullIf(sum(s_valid_lp), 0), 4) AS pobreza_ingresos,
  round(100 * sum(s_under_lp_ext) / nullIf(sum(s_valid_lp), 0), 4) AS pobreza_extrema_ingresos
FROM indicadores.persona_sums
WHERE level = 'nacional_sin_area'
GROUP BY anio, periodo
ORDER BY anio, periodo;


CREATE OR REPLACE VIEW indicadores.indicadores_persona_parroquia_por_periodo AS
SELECT
  anio, periodo,
  multiIf(periodo=1,'Enero', periodo=2,'Febrero', periodo=3,'Marzo', periodo=4,'Abril',
          periodo=5,'Mayo',  periodo=6,'Junio',   periodo=7,'Julio', periodo=8,'Agosto',
          periodo=9,'Septiembre', periodo=10,'Octubre', periodo=11,'Noviembre','Diciembre') AS mes,
  geo AS ciudad,
  round(100 * sum(sw_pea) / nullIf(sum(sw_pet), 0), 4) AS tasa_participacion_global,
  round(100 * sum(sw_pea) / nullIf(sum(sw_pop), 0), 4) AS tasa_participacion_bruta,
  round(100 * (sum(sw_pea) - sum(sw_occ)) / nullIf(sum(sw_pea), 0), 4) AS tasa_desempleo,
  round(100 * sum(sw_occ) / nullIf(sum(sw_pea), 0), 4) AS empleo_total,
  round(100 * sum(s_formal_w) / nullIf(sum(sw_occ), 0), 4) AS empleo_formal,
  round(100 * sum(s_informal_w) / nullIf(sum(sw_occ), 0), 4) AS empleo_informal,
  round(100 * sum(s_emp_adecuado) / nullIf(sum(sw_pea), 0), 4) AS empleo_adecuado,
  round(100 * sum(s_subempleo) / nullIf(sum(sw_pea), 0), 4) AS subempleo,
  round(100 * sum(s_no_remu) / nullIf(sum(sw_pea), 0), 4) AS no_remunerado,
  round(100 * sum(s_otro_no_pleno) / nullIf(sum(sw_pea), 0), 4) AS otro_no_pleno,
  round(
    100 * ((sum(ade_h) / nullIf(sum(pea_h), 0)) - (sum(ade_m) / nullIf(sum(pea_m), 0)))
        / nullIf(sum(ade_h) / nullIf(sum(pea_h), 0), 0), 4
  ) AS brecha_adecuado_HM,
  round(
    100 * ((sum(occ_inc_w_h) / nullIf(sum(occ_w_h), 0)) - (sum(occ_inc_w_m) / nullIf(sum(occ_w_m), 0)))
        / nullIf(sum(occ_inc_w_h) / nullIf(sum(occ_w_h), 0), 0), 4
  ) AS brecha_salarial_HM,
  round(100 * sum(s_youth_nini) / nullIf(sum(s_youth), 0), 4) AS NiNi,
  round(100 * sum(s_juv_des) / nullIf(sum(s_juv_pea), 0), 4) AS desempleo_juvenil,
  round(100 * sum(s_ti) / nullIf(sum(s_kids), 0), 4) AS trabajo_infantil,
  round(100 * sum(s_occ_manu) / nullIf(sum(sw_occ), 0), 4) AS empleo_manufactura,
  round(100 * sum(s_asist_5_24) / nullIf(sum(s_5_24), 0), 4) AS tasa_asistencia_clases,
  round(100 * sum(s_under_lp) / nullIf(sum(s_valid_lp), 0), 4) AS pobreza_ingresos,
  round(100 * sum(s_under_lp_ext) / nullIf(sum(s_valid_lp), 0), 4) AS pobreza_extrema_ingresos
FROM indicadores.persona_sums
WHERE level = 'parroquial_sin_area'
GROUP BY anio, periodo, ciudad
ORDER BY anio, periodo, ciudad;

/* ======================================================================
   MV PERSONA+VIVIENDA
   ====================================================================== */
CREATE OR REPLACE VIEW indicadores.enemdu_periodos_intersect AS
SELECT periodo
FROM (
  SELECT periodo FROM indicadores.enemdu_persona   GROUP BY periodo
) p
INNER JOIN (
  SELECT periodo FROM indicadores.enemdu_vivienda  GROUP BY periodo
) v USING (periodo);

DROP TABLE IF EXISTS indicadores.hh_ipm_nbi;
CREATE TABLE indicadores.hh_ipm_nbi
(
  periodo String,
  id_hogar String,
  ci Nullable(Float64),
  TPM Nullable(UInt8),
  TPEM Nullable(UInt8),
  A Nullable(Float64),
  IPM Nullable(Float64),
  depec Nullable(UInt8),
  ninastesc Nullable(UInt8),
  matviv_def Nullable(UInt8),
  ser_viv Nullable(UInt8),
  hacm Nullable(UInt8),
  NBI_hogar Nullable(UInt8)
)
ENGINE = MergeTree
ORDER BY (periodo, id_hogar);

DROP VIEW IF EXISTS indicadores.mv_ipm_nbi_hogares;
CREATE MATERIALIZED VIEW indicadores.mv_ipm_nbi_hogares
TO indicadores.hh_ipm_nbi
AS
WITH
  base AS
  (
    SELECT
      p.periodo, p.id_persona, p.id_hogar,
      toInt32OrNull(toString(p.p03))  AS p03,
      toInt32OrNull(toString(p.p07))  AS p07,
      toInt32OrNull(toString(p.p09))  AS p09,
      toInt32OrNull(toString(p.p10a)) AS p10a,
      toInt32OrNull(toString(p.p10b)) AS p10b,
      toInt32OrNull(toString(p.p05a)) AS p05a,
      toInt32OrNull(toString(p.p05b)) AS p05b,
      toInt32OrNull(toString(p.p20))  AS p20,
      toInt32OrNull(toString(p.p21))  AS p21,
      toInt32OrNull(toString(p.p22))  AS p22,
      toInt32OrNull(toString(p.p24))  AS p24,
      toInt32OrNull(toString(p.condact))   AS condact,
      toInt32OrNull(toString(p.empleo))    AS empleo,
      toInt32OrNull(toString(p.desempleo)) AS desempleo,
      toInt32OrNull(toString(p.p72a))      AS p72a,
      toInt32OrNull(toString(p.p75))       AS p75,
      toInt32OrNull(toString(p.p77))       AS p77,
      toInt32OrNull(toString(p.p51a))      AS p51a,
      toInt32OrNull(toString(p.p51b))      AS p51b,
      toInt32OrNull(toString(p.p51c))      AS p51c,
      toFloat64OrZero(toString(p.fexp))    AS fexp,
      toInt32OrNull(toString(p.epobreza))  AS epobreza,
      (p03 >= 15 AND fexp > 0)                               AS pet,
      (p03 >= 15 AND fexp > 0 AND condact BETWEEN 1 AND 8)   AS pea,
      (p03 >= 15 AND fexp > 0 AND (condact NOT BETWEEN 1 AND 8)) AS pei
    FROM indicadores.enemdu_persona p
    INNER JOIN indicadores.enemdu_periodos_intersect pi ON pi.periodo = p.periodo
  ),
  viv AS
  (
    SELECT
      v.periodo, v.id_hogar,
      any(toInt32OrNull(toString(v.area)))  AS area,
      any(toInt32OrNull(toString(v.vi07)))  AS vi07,
      any(toInt32OrNull(toString(v.vi09)))  AS vi09,
      any(toInt32OrNull(toString(v.vi10)))  AS vi10,
      any(toInt32OrNull(toString(v.vi13)))  AS vi13,
      any(toInt32OrNull(toString(v.vi03a))) AS vi03a,
      any(toInt32OrNull(toString(v.vi03b))) AS vi03b,
      any(toInt32OrNull(toString(v.vi04a))) AS vi04a,
      any(toInt32OrNull(toString(v.vi04b))) AS vi04b,
      any(toInt32OrNull(toString(v.vi05a))) AS vi05a,
      any(toInt32OrNull(toString(v.vi05b))) AS vi05b
    FROM indicadores.enemdu_vivienda v
    INNER JOIN indicadores.enemdu_periodos_intersect pi ON pi.periodo = v.periodo
    GROUP BY v.periodo, v.id_hogar
  ),
  joined AS
  (
    SELECT b.*, vv.area, vv.vi07, vv.vi09, vv.vi10, vv.vi13, vv.vi03a, vv.vi03b, vv.vi04a, vv.vi04b, vv.vi05a, vv.vi05b
    FROM base b
    LEFT JOIN viv vv ON vv.periodo = b.periodo AND vv.id_hogar = b.id_hogar
  ),
  escol_calc AS
  (
    SELECT
      *,
      multiIf(
        p10a=1 AND p10b=0, 0, p10a=2 AND p10b=0, 0, p10a=2 AND p10b=1, 2, p10a=2 AND p10b=2, 4,
        p10a=2 AND p10b=3, 6, p10a=2 AND p10b=4, 7, p10a=3, 1, p10a=4, 1+p10b, p10a=5, p10b,
        p10a=6, 7+p10b, p10a=7, 10+p10b, p10a=8, 13+p10b, p10a=9, 13+p10b, p10a=10, 18+p10b, 0
      ) AS escol
    FROM joined
  ),
  horas_calc AS
  (
    SELECT
      *,
      if(p51a=999, CAST(NULL AS Nullable(Float64)), CAST(p51a AS Nullable(Float64))) AS p51a_f,
      if(p51b=999, CAST(NULL AS Nullable(Float64)), CAST(p51b AS Nullable(Float64))) AS p51b_f,
      if(p51c=999, CAST(NULL AS Nullable(Float64)), CAST(p51c AS Nullable(Float64))) AS p51c_f,
      (nullIf(p51a_f,0.0)+nullIf(p51b_f,0.0)+nullIf(p51c_f,0.0)) AS hh_sum,
      multiIf(
        empleo=1, CAST(0.0 AS Nullable(Float64)),
        (pea=1) AND (p20=1), CAST(p24 AS Nullable(Float64)),
        (pea=1) AND (p20=2) AND (p21<=11), CAST(p24 AS Nullable(Float64)),
        (pea=1) AND (p20=2) AND (p21=12) AND (p22=1), hh_sum,
        CAST(NULL AS Nullable(Float64))
      ) AS horas
    FROM escol_calc
  ),
  per AS
  (
    SELECT
      *,
      if((p03 BETWEEN 5 AND 17) AND (p10a<8),
         if(
           ((p03 BETWEEN 5 AND 14) AND p07=1 AND (p10a IN (1,3) OR (p10a=4 AND p10b BETWEEN 0 AND 6) OR (p10a=5 AND p10b BETWEEN 0 AND 9) OR (p10a=6 AND p10b BETWEEN 0 AND 2)))
           OR ((p03 BETWEEN 15 AND 17) AND p07=1 AND ((p10a=5 AND p10b=10) OR (p10a=7 AND p10b BETWEEN 0 AND 2) OR (p10a=6 AND p10b BETWEEN 3 AND 5)))
           OR (p10a>=8),
           0, 1),
         NULL) AS dim1_ind1_p,
      if((p03 BETWEEN 18 AND 29),
         if((p07=2) AND (((p10a=7 AND p10b>=3) OR (p10a=6 AND p10b>=6) OR (p10a IN (8,9)))) AND (p09=3), 1, 0),
         NULL) AS dim1_ind2_p,
      if((p03 BETWEEN 18 AND 64), if((escol<10 AND p07=2),1,0), NULL) AS dim1_ind3_p,
      if((p03 BETWEEN 5 AND 17),
         if((condact BETWEEN 2 AND 6) OR (condact=1 AND (p07=2 OR horas>30)) OR ((p03 BETWEEN 5 AND 14) AND (p20=1 OR (p20=2 AND p21 BETWEEN 1 AND 11) OR p22=1)), 1, 0),
         NULL) AS dim2_ind1_p,
      if((p03 BETWEEN 18 AND 98), if(condact BETWEEN 2 AND 8, 1, 0), NULL) AS dim2_ind2_p,
      if((p03>=15 AND pet=1),
         multiIf(
           (p03>=65 AND p72a=2 AND (desempleo=1 OR pei=1)), 1.0,
           (p03>=65 AND p72a=2 AND p75=1), 0.0,
           (empleo=1 AND p05a BETWEEN 5 AND 10 AND p05b BETWEEN 5 AND 10), 1.0,
           (p77=1), 0.0,
           0.0
         ),
         NULL) AS dim2_ind3_p,
      ifNull(toFloat64(epobreza), NULL) AS dim3_ind1_p,
      ifNull(if(vi10 IS NULL, NULL, toFloat64(vi10 != 1)), NULL) AS dim3_ind2_p,
      -- if(vi10 IN (0, 9, 99), CAST(NULL AS Nullable(Float64)), toFloat64(vi10 != 1)) AS dim3_ind2_p,
      1 AS _per_marker
    FROM horas_calc
  ),
  per_to_h AS
  (
    SELECT
      periodo, id_hogar,
      max(dim1_ind1_p) AS dim1_ind1_h,
      max(dim1_ind2_p) AS dim1_ind2_h,
      max(dim1_ind3_p) AS dim1_ind3_h,
      max(dim2_ind1_p) AS dim2_ind1_h,
      max(dim2_ind2_p) AS dim2_ind2_h,
      max(dim2_ind3_p) AS dim2_ind3_h,
      max(dim3_ind1_p) AS dim3_ind1_h,
      max(dim3_ind2_p) AS dim3_ind2_h,
      countIf(_per_marker=1) AS hsize_calc
    FROM per
    GROUP BY periodo, id_hogar
  ),
  materiales AS
  (
    SELECT
      j.periodo, j.id_hogar,
      ifNull(nullIf(vv.vi07,0),1) AS vi07_adj,
      multiIf(((vv.vi03a=1 AND vv.vi03b IN (1,2)) OR (vv.vi03b=1 AND vv.vi03a IN (2,3,4))),1,
              ((vv.vi03a=1 AND vv.vi03b=3) OR (vv.vi03b=2 AND vv.vi03a IN (2,3,4))),2,
              ((vv.vi03b=3 AND vv.vi03a IN (2,3,4)) OR vv.vi03a IN (5,6)),3, NULL) AS techo,
      multiIf(((vv.vi05a=1 AND vv.vi05b IN (1,2)) OR (vv.vi05a=2 AND vv.vi05b=1)),1,
              ((vv.vi05a=1 AND vv.vi05b=3) OR (vv.vi05a=2 AND vv.vi05b=2) OR (vv.vi05a IN (3,4,5) AND vv.vi05b IN (1,2))),2,
              ((vv.vi05b=3 AND vv.vi05a IN (2,3,4,5)) OR vv.vi05a IN (6,7)),3, NULL) AS pared,
      multiIf((((vv.vi04a<=3) AND vv.vi04b IN (1,2)) OR (vv.vi04b=1 AND vv.vi04a IN (4,5))),1,
              (((vv.vi04a<=3) AND vv.vi04b=3) OR (vv.vi04b=2 AND vv.vi04a IN (4,5)) OR (vv.vi04a=6 AND vv.vi04b=1)),2,
              (((vv.vi04b=3) AND vv.vi04a IN (4,5,6)) OR (vv.vi04a=6 AND vv.vi04b=2) OR vv.vi04a IN (7,8)),3, NULL) AS piso
    FROM per j
    LEFT JOIN viv vv ON vv.periodo = j.periodo AND vv.id_hogar = j.id_hogar
    GROUP BY j.periodo, j.id_hogar, vv.vi07, vv.vi03a, vv.vi03b, vv.vi05a, vv.vi05b, vv.vi04a, vv.vi04b
  ),
  tipviv AS
  (
    SELECT
      m.periodo, m.id_hogar, m.vi07_adj,
      multiIf( ((m.techo=1 AND m.pared=1 AND m.piso IN (1,2,3)) OR (m.techo=1 AND m.pared=2 AND m.piso=1)), 1,
               ((m.techo=1 AND m.pared=2 AND m.piso IN (2,3)) OR (m.techo=1 AND m.pared=3 AND m.piso IN (1,2)) OR
                (m.techo=2 AND m.pared IN (1,2) AND m.piso IN (1,2)) OR (m.techo=3 AND m.pared=1 AND m.piso IN (1,2)) OR
                (m.techo=3 AND m.pared=2 AND m.piso=1)), 2,
               ((m.techo=1 AND m.pared=3 AND m.piso=3) OR (m.techo=2 AND m.pared IN (1,2) AND m.piso=3) OR
                (m.techo=2 AND m.pared=3 AND m.piso IN (1,2,3)) OR (m.techo=3 AND m.pared=1 AND m.piso=3) OR
                (m.techo=3 AND m.pared=2 AND m.piso IN (1,2,3)) OR (m.techo=3 AND m.pared=3 AND m.piso IN (1,2,3))), 3,
               NULL) AS tipviv
    FROM materiales m
  ),
  dim4_h AS
  (
    SELECT
      t.periodo, t.id_hogar,
      if((h.hsize_calc / t.vi07_adj) > 3, 1.0, 0.0) AS dim4_ind1_h,
      if(t.tipviv IN (2,3), 1.0, if(t.tipviv=1, 0.0, NULL)) AS dim4_ind2_h
    FROM tipviv t
    INNER JOIN per_to_h h ON h.periodo = t.periodo AND h.id_hogar = t.id_hogar
  ),
  dim4_h_2 AS
  (
    SELECT
      j.periodo, j.id_hogar,
      max(if(vv.area=1, if(vv.vi09 BETWEEN 2 AND 5, 1.0, 0.0),
             if(vv.area=2, if(vv.vi09 BETWEEN 3 AND 5, 1.0, 0.0), NULL))) AS dim4_ind3_h,
      max(if(vv.vi13 IN (1,3,4,5), 1.0, 0.0)) AS dim4_ind4_h
    FROM per j
    LEFT JOIN viv vv ON vv.periodo = j.periodo AND vv.id_hogar = j.id_hogar
    GROUP BY j.periodo, j.id_hogar
  ),
  hh_inds AS
  (
    SELECT
      h.periodo AS periodo, h.id_hogar AS id_hogar,
      h.dim1_ind1_h, h.dim1_ind2_h, h.dim1_ind3_h,
      h.dim2_ind1_h, h.dim2_ind2_h, h.dim2_ind3_h,
      h.dim3_ind1_h, h.dim3_ind2_h,
      d4.dim4_ind1_h, d4.dim4_ind2_h, d42.dim4_ind3_h, d42.dim4_ind4_h
    FROM per_to_h h
    LEFT JOIN dim4_h   d4  ON d4.periodo  = h.periodo AND d4.id_hogar  = h.id_hogar
    LEFT JOIN dim4_h_2 d42 ON d42.periodo = h.periodo AND d42.id_hogar = h.id_hogar
  ),
  pesos AS (SELECT array(1.0/4/3,1.0/4/3,1.0/4/3, 1.0/4/3,1.0/4/3,1.0/4/3, 1.0/4/2,1.0/4/2, 1.0/4/4,1.0/4/4,1.0/4/4,1.0/4/4) AS w),
  nbi_dep AS
  (
    WITH pers AS (
      SELECT periodo, id_hogar,
             maxIf(multiIf(
               p10a=1 AND p10b=0,0, p10a=2 AND p10b=0,0, p10a=2 AND p10b=1,2, p10a=2 AND p10b=2,4,
               p10a=2 AND p10b=3,6, p10a=2 AND p10b=4,7, p10a=3,1, p10a=4,1+p10b, p10a=5,p10b,
               p10a=6,7+p10b, p10a=7,10+p10b, p10a=8,13+p10b, p10a=9,13+p10b, p10a=10,18+p10b, 0
             ) < 3, p04=1) AS escjefe_lt3,
             sumIf((p03>=15) AND (condact BETWEEN 1 AND 6), 1) AS numper_ocu,
             count() AS numper
      FROM indicadores.enemdu_persona
      INNER JOIN indicadores.enemdu_periodos_intersect pi ON pi.periodo = periodo
      GROUP BY periodo, id_hogar
    )
    SELECT periodo, id_hogar,
           toUInt8((escjefe_lt3=1 AND numper_ocu>0 AND (numper / nullIf(numper_ocu,0)) > 3) OR (escjefe_lt3=1 AND numper_ocu=0)) AS depec,
           numper
    FROM pers
  ),
  nbi_ninos AS
  (
    SELECT periodo, id_hogar,
           toUInt8(maxIf(1, (toInt32OrNull(toString(p03)) BETWEEN 6 AND 12) AND toInt32OrNull(toString(p07))=2)) AS ninastesc
    FROM indicadores.enemdu_persona
    INNER JOIN indicadores.enemdu_periodos_intersect pi ON pi.periodo = periodo
    GROUP BY periodo, id_hogar
  ),
  nbi_mat AS (SELECT vv.periodo, vv.id_hogar, toUInt8((vv.vi04a BETWEEN 7 AND 8) OR (vv.vi05a BETWEEN 6 AND 7)) AS matviv_def FROM viv AS vv),
  nbi_ser AS (SELECT vv.periodo, vv.id_hogar, toUInt8((vv.vi09 >= 3) OR (vv.vi10 = 2) OR (vv.vi10 >= 4)) AS ser_viv FROM viv AS vv),
  nbi_hac AS
  (
    SELECT m.periodo, m.id_hogar, toUInt8((d.numper / nullIf(m.vi07_adj,0)) > 3) AS hacm
    FROM materiales m
    INNER JOIN nbi_dep d ON d.periodo = m.periodo AND d.id_hogar = m.id_hogar
  )
SELECT
  hi.periodo AS periodo,
  hi.id_hogar AS id_hogar,
  (
    (ifNull(hi.dim1_ind1_h,0)*w[1]) + (ifNull(hi.dim1_ind2_h,0)*w[2]) + (ifNull(hi.dim1_ind3_h,0)*w[3]) +
    (ifNull(hi.dim2_ind1_h,0)*w[4]) + (ifNull(hi.dim2_ind2_h,0)*w[5]) + (ifNull(hi.dim2_ind3_h,0)*w[6]) +
    (ifNull(hi.dim3_ind1_h,0)*w[7]) + (ifNull(hi.dim3_ind2_h,0)*w[8]) +
    (ifNull(hi.dim4_ind1_h,0)*w[9]) + (ifNull(hi.dim4_ind2_h,0)*w[10]) + (ifNull(hi.dim4_ind3_h,0)*w[11]) + (ifNull(hi.dim4_ind4_h,0)*w[12])
  ) AS ci,
  toUInt8(ci >= (4.0/12.0)) AS TPM,
  toUInt8(ci >= (6.0/12.0)) AS TPEM,
  if(TPM=1, ci, CAST(NULL AS Nullable(Float64))) AS A,
  if(TPM=1, ci, 0.0) AS IPM,
  nd.depec, nn.ninastesc, nm.matviv_def, ns.ser_viv, nh.hacm,
  toUInt8((nd.depec + nn.ninastesc + nm.matviv_def + ns.ser_viv + nh.hacm) >= 1) AS NBI_hogar
FROM (SELECT periodo, id_hogar, dim1_ind1_h, dim1_ind2_h, dim1_ind3_h, dim2_ind1_h, dim2_ind2_h, dim2_ind3_h, dim3_ind1_h, dim3_ind2_h, dim4_ind1_h, dim4_ind2_h, dim4_ind3_h, dim4_ind4_h FROM hh_inds) AS hi
CROSS JOIN pesos
LEFT JOIN nbi_dep   AS nd ON nd.periodo = hi.periodo AND nd.id_hogar = hi.id_hogar
LEFT JOIN nbi_ninos AS nn ON nn.periodo = hi.periodo AND nn.id_hogar = hi.id_hogar
LEFT JOIN nbi_mat   AS nm ON nm.periodo = hi.periodo AND nm.id_hogar = hi.id_hogar
LEFT JOIN nbi_ser   AS ns ON ns.periodo = hi.periodo AND ns.id_hogar = hi.id_hogar
LEFT JOIN nbi_hac   AS nh ON nh.periodo = hi.periodo AND nh.id_hogar = hi.id_hogar;

DROP TABLE IF EXISTS indicadores.vivienda_sums;
CREATE TABLE indicadores.vivienda_sums
(
  level   LowCardinality(String),
  anio    Int32,
  periodo Int32,
  area    Int32,
  geo     LowCardinality(String),
  sw_pop  Nullable(Float64),
  s_tpm   Nullable(Float64),
  s_tpem  Nullable(Float64),
  s_A     Nullable(Float64),
  s_ipm   Nullable(Float64),
  s_nbi   Nullable(Float64)
)
ENGINE = SummingMergeTree
ORDER BY (level, anio, periodo, area, geo);

DROP VIEW IF EXISTS indicadores.mv_vivienda_sums;
CREATE MATERIALIZED VIEW indicadores.mv_vivienda_sums
TO indicadores.vivienda_sums
AS
WITH base_b AS
(
  SELECT
    p.periodo,
    p.id_persona,
    p.id_hogar,
    -- CAST(p.fexp AS Float64) AS fexp,
    toFloat64OrZero(toString(p.fexp)) AS fexp,

    /* GEO desde ciudad (XXYYZZ) */
    replaceRegexpAll(toString(p.ciudad), '[^0-9]', '') AS geo_digits,
    substring(geo_digits, 1, 2) AS prov2,
    substring(geo_digits, 1, 4) AS cant4,
    substring(geo_digits, 1, 6) AS parr6,

    /* Año/Periodo (ajusta si tu formato difiere) */
    toInt32OrNull(substring(toString(p.periodo), 1, 4)) AS anio_i,
    toInt32OrNull(right(toString(p.periodo), 2))        AS per_i,

    /* Área del hogar (directo desde vivienda) */
    toInt32OrNull(toString(v.area)) AS area_n,

    /* Flags y valores del hogar */
    h.TPM, h.TPEM, h.A, h.ci, h.NBI_hogar

  FROM indicadores.hh_ipm_nbi AS h
  /* unir personas para fexp y ciudad */
  INNER JOIN indicadores.enemdu_persona AS p
    ON p.periodo = h.periodo AND p.id_hogar = h.id_hogar
  /* área del hogar sin vista intermedia */
  INNER JOIN indicadores.enemdu_vivienda AS v
    ON v.periodo = h.periodo AND v.id_hogar = h.id_hogar
  /* sólo periodos válidos */
  INNER JOIN indicadores.enemdu_periodos_intersect AS pi
    ON pi.periodo = h.periodo
  WHERE fexp > 0 
)

SELECT
  tup.1 AS level,
  tup.2 AS anio,
  tup.3 AS periodo,
  tup.4 AS area,
  tup.5 AS geo,

  sum(fexp)                                AS sw_pop,
  sum(fexp * (TPM  = 1))                   AS s_tpm,
  sum(fexp * (TPEM = 1))                   AS s_tpem,
  sum(if(TPM=1, fexp * A,  0.0))           AS s_A,
  sum(fexp * if(TPM=1, ci, 0.0))           AS s_ipm,
  sum(fexp * (NBI_hogar = 1))              AS s_nbi

FROM base_b

ARRAY JOIN
[
  ('nacional',            anio_i, per_i, ifNull(area_n, toInt32(0)), ''               ),
  ('provincia',           anio_i, per_i, ifNull(area_n, toInt32(0)), ifNull(prov2,'') ),
  ('canton',              anio_i, per_i, ifNull(area_n, toInt32(0)), ifNull(cant4,'') ),
  ('parroquia',           anio_i, per_i, ifNull(area_n, toInt32(0)), ifNull(parr6,'') ),
  ('nacional_sin_area',   anio_i, per_i, toInt32(0),                  ''               ),
  ('parroquial_sin_area', anio_i, per_i, toInt32(0),                  ifNull(parr6,'') ),
  ('canton_anual',        anio_i, toInt32(0), toInt32(0),             ifNull(cant4,'') )
] AS tup

WHERE
      (tup.1 = 'nacional'             AND length(tup.5) = 0 AND tup.3 > 0 AND tup.4 IN (0,1,2))
  OR  (tup.1 = 'provincia'            AND length(tup.5) = 2 AND tup.3 > 0 AND tup.4 IN (0,1,2))
  OR  (tup.1 = 'canton'               AND length(tup.5) = 4 AND tup.3 > 0 AND tup.4 IN (0,1,2))
  OR  (tup.1 = 'parroquia'            AND length(tup.5) = 6 AND tup.3 > 0 AND tup.4 IN (0,1,2))
  OR  (tup.1 = 'nacional_sin_area'    AND length(tup.5) = 0 AND tup.3 > 0 AND tup.4 = 0)
  OR  (tup.1 = 'parroquial_sin_area'  AND length(tup.5) = 6 AND tup.3 > 0 AND tup.4 = 0)
  OR  (tup.1 = 'canton_anual'         AND length(tup.5) = 4 AND tup.3 = 0 AND tup.4 = 0)

GROUP BY level, anio, periodo, area, geo;

-- Nacional (con área)
CREATE OR REPLACE VIEW indicadores.indicadores_vivienda_nacional AS
SELECT
  anio, periodo,
  multiIf(periodo=1,'Enero', periodo=2,'Febrero', periodo=3,'Marzo', periodo=4,'Abril',
          periodo=5,'Mayo',  periodo=6,'Junio',   periodo=7,'Julio', periodo=8,'Agosto',
          periodo=9,'Septiembre', periodo=10,'Octubre', periodo=11,'Noviembre','Diciembre') AS mes,
  area,
  round(100 * sum(s_tpm)  / nullIf(sum(sw_pop), 0), 4) AS tpm,
  round(100 * sum(s_tpem) / nullIf(sum(sw_pop), 0), 4) AS tpem,
  round(      sum(s_A)    / nullIf(sum(s_tpm),  0), 4) AS A,
  round(100 * sum(s_ipm)  / nullIf(sum(sw_pop), 0), 4) AS ipm,
  round(100 * sum(s_nbi)  / nullIf(sum(sw_pop), 0), 4) AS nbi
FROM indicadores.vivienda_sums
WHERE level = 'nacional'
GROUP BY anio, periodo, area
ORDER BY anio, periodo, area;

-- Provincia
CREATE OR REPLACE VIEW indicadores.indicadores_vivienda_provincia AS
SELECT
  anio, periodo,
  multiIf(periodo=1,'Enero', periodo=2,'Febrero', periodo=3,'Marzo', periodo=4,'Abril',
          periodo=5,'Mayo',  periodo=6,'Junio',   periodo=7,'Julio', periodo=8,'Agosto',
          periodo=9,'Septiembre', periodo=10,'Octubre', periodo=11,'Noviembre','Diciembre') AS mes,
  area,
  geo AS provincia,
  round(100 * sum(s_tpm)  / nullIf(sum(sw_pop), 0), 4) AS tpm,
  round(100 * sum(s_tpem) / nullIf(sum(sw_pop), 0), 4) AS tpem,
  round(      sum(s_A)    / nullIf(sum(s_tpm),  0), 4) AS A,
  round(100 * sum(s_ipm)  / nullIf(sum(sw_pop), 0), 4) AS ipm,
  round(100 * sum(s_nbi)  / nullIf(sum(sw_pop), 0), 4) AS nbi
FROM indicadores.vivienda_sums
WHERE level = 'provincia'
GROUP BY anio, periodo, area, provincia
ORDER BY anio, periodo, area, provincia;

-- Cantón
CREATE OR REPLACE VIEW indicadores.indicadores_vivienda_canton AS
SELECT
  anio, periodo,
  multiIf(periodo=1,'Enero', periodo=2,'Febrero', periodo=3,'Marzo', periodo=4,'Abril',
          periodo=5,'Mayo',  periodo=6,'Junio',   periodo=7,'Julio', periodo=8,'Agosto',
          periodo=9,'Septiembre', periodo=10,'Octubre', periodo=11,'Noviembre','Diciembre') AS mes,
  area,
  geo AS canton,
  round(100 * sum(s_tpm)  / nullIf(sum(sw_pop), 0), 4) AS tpm,
  round(100 * sum(s_tpem) / nullIf(sum(sw_pop), 0), 4) AS tpem,
  round(      sum(s_A)    / nullIf(sum(s_tpm),  0), 4) AS A,
  round(100 * sum(s_ipm)  / nullIf(sum(sw_pop), 0), 4) AS ipm,
  round(100 * sum(s_nbi)  / nullIf(sum(sw_pop), 0), 4) AS nbi
FROM indicadores.vivienda_sums
WHERE level = 'canton'
GROUP BY anio, periodo, area, canton
ORDER BY anio, periodo, area, canton;

-- Parroquia
CREATE OR REPLACE VIEW indicadores.indicadores_vivienda_parroquia AS
SELECT
  anio, periodo,
  multiIf(periodo=1,'Enero', periodo=2,'Febrero', periodo=3,'Marzo', periodo=4,'Abril',
          periodo=5,'Mayo',  periodo=6,'Junio',   periodo=7,'Julio', periodo=8,'Agosto',
          periodo=9,'Septiembre', periodo=10,'Octubre', periodo=11,'Noviembre','Diciembre') AS mes,
  area,
  geo AS ciudad,
  round(100 * sum(s_tpm)  / nullIf(sum(sw_pop), 0), 4) AS tpm,
  round(100 * sum(s_tpem) / nullIf(sum(sw_pop), 0), 4) AS tpem,
  round(      sum(s_A)    / nullIf(sum(s_tpm),  0), 4) AS A,
  round(100 * sum(s_ipm)  / nullIf(sum(sw_pop), 0), 4) AS ipm,
  round(100 * sum(s_nbi)  / nullIf(sum(sw_pop), 0), 4) AS nbi
FROM indicadores.vivienda_sums
WHERE level = 'parroquia'
GROUP BY anio, periodo, area, ciudad
ORDER BY anio, periodo, area, ciudad;

-- Cantón (anual, sin área)
CREATE OR REPLACE VIEW indicadores.indicadores_vivienda_canton_anual AS
SELECT
  anio,
  geo AS canton,
  round(100 * sum(s_tpm)  / nullIf(sum(sw_pop), 0), 4) AS tpm,
  round(100 * sum(s_tpem) / nullIf(sum(sw_pop), 0), 4) AS tpem,
  round(      sum(s_A)    / nullIf(sum(s_tpm),  0), 4) AS A,
  round(100 * sum(s_ipm)  / nullIf(sum(sw_pop), 0), 4) AS ipm,
  round(100 * sum(s_nbi)  / nullIf(sum(sw_pop), 0), 4) AS nbi
FROM indicadores.vivienda_sums
WHERE level = 'canton_anual'
GROUP BY anio, canton
ORDER BY anio, canton;

-- Nacional por periodo (sin área)
CREATE OR REPLACE VIEW indicadores.indicadores_vivienda_nacional_por_periodo AS
SELECT
  anio, periodo,
  multiIf(periodo=1,'Enero', periodo=2,'Febrero', periodo=3,'Marzo', periodo=4,'Abril',
          periodo=5,'Mayo',  periodo=6,'Junio',   periodo=7,'Julio', periodo=8,'Agosto',
          periodo=9,'Septiembre', periodo=10,'Octubre', periodo=11,'Noviembre','Diciembre') AS mes,
  round(100 * sum(s_tpm)  / nullIf(sum(sw_pop), 0), 4) AS tpm,
  round(100 * sum(s_tpem) / nullIf(sum(sw_pop), 0), 4) AS tpem,
  round(      sum(s_A)    / nullIf(sum(s_tpm),  0), 4) AS A,
  round(100 * sum(s_ipm)  / nullIf(sum(sw_pop), 0), 4) AS ipm,
  round(100 * sum(s_nbi)  / nullIf(sum(sw_pop), 0), 4) AS nbi
FROM indicadores.vivienda_sums
WHERE level = 'nacional'
GROUP BY anio, periodo
ORDER BY anio, periodo;

-- Parroquia por periodo (sin área)
CREATE OR REPLACE VIEW indicadores.indicadores_vivienda_parroquia_por_periodo AS
SELECT
  anio, periodo,
  multiIf(periodo=1,'Enero', periodo=2,'Febrero', periodo=3,'Marzo', periodo=4,'Abril',
          periodo=5,'Mayo',  periodo=6,'Junio',   periodo=7,'Julio', periodo=8,'Agosto',
          periodo=9,'Septiembre', periodo=10,'Octubre', periodo=11,'Noviembre','Diciembre') AS mes,
  geo AS ciudad,
  round(100 * sum(s_tpm)  / nullIf(sum(sw_pop), 0), 4) AS tpm,
  round(100 * sum(s_tpem) / nullIf(sum(sw_pop), 0), 4) AS tpem,
  round(      sum(s_A)    / nullIf(sum(s_tpm),  0), 4) AS A,
  round(100 * sum(s_ipm)  / nullIf(sum(sw_pop), 0), 4) AS ipm,
  round(100 * sum(s_nbi)  / nullIf(sum(sw_pop), 0), 4) AS nbi
FROM indicadores.vivienda_sums
WHERE level = 'parroquia'
GROUP BY anio, periodo, ciudad
ORDER BY anio, periodo, ciudad;

-- ===================================================
-- Tabla Latinobarometro
-- ===================================================
-- DROP TABLE indicadores.latinobarometro;
CREATE TABLE IF NOT EXISTS indicadores.latinobarometro (
    research_year         Int16,
    resp_country          Int32,
    country_name ALIAS transform(
      resp_country,
      [32, 68, 76, 152, 170, 188, 218, 222, 724, 320, 340, 484, 558, -3, -2, -4, -1, -5, 591, 600, 604, 214, 858, 862],
      ['Argentina','Bolivia','Brazil','Chile','Colombia','Costa Rica','Ecuador','El Salvador','Spain','Guatemala','Honduras','Mexico','Nicaragua','No aplicable','No contesta','No preguntada','No sabe','No sabe / No contesta','Panama','Paraguay','Peru','Dominican Republic','Uruguay','Venezuela'],
      'Desconocido'
    ),
    iso3 ALIAS transform(
      resp_country,
      [32, 68, 76, 152, 170, 188, 218, 222, 724, 320, 340, 484, 558, -3, -2, -4, -1, -5, 591, 600, 604, 214, 858, 862],
      ['ARG','BOL','BRA','CHL','COL','CRI','ECU','SLV','ESP','GTM','HND','MEX','NIC','UNK','UNK','UNK','UNK','UNK','PAN','PRY','PER','DOM','URY','VEN'],
      'UNK'
    ),
    research_region Int32,
    research_city Int32,
    research_city_size    Nullable(Int32),
    democ_supp            Nullable(Int16),
    democ_satis           Nullable(Int16),
    left_right_scale      Nullable(Int16),
    elections_vote        Nullable(Int16),
    job_concern           Nullable(Int16),
    econ_situation        Nullable(Int16),
    goods_wash_mach       Nullable(Int16),
    goods_car             Nullable(Int16),
    goods_sewage          Nullable(Int16),
    goods_hot_water       Nullable(Int16),
    confidence_congress   Nullable(Int16),
    confidence_judiciary  Nullable(Int16),
    confidence_church     Nullable(Int16),
    confidence_police     Nullable(Int16),
    confidence_army       Nullable(Int16),
    confidence_political_parties  Nullable(Int16),
    resp_sex              Nullable(Int16),
    resp_age              Nullable(Int16),
    resp_chief            Nullable(Int16),
    resp_education        Nullable(Int16),
    resp_employment       Nullable(Int16),
    resp_economic_perception  Nullable(Int16),
    resp_religion         Nullable(Int16)
)
ENGINE = MergeTree
ORDER BY (research_year, resp_country, research_region, research_city);

/* ===================================================
   Sums para Latinobarometro
   =================================================== */
-- DROP TABLE IF EXISTS indicadores.latinobarometro_sums;
CREATE TABLE IF NOT EXISTS indicadores.latinobarometro_sums
(
  level LowCardinality(String),
  anio  UInt16,
  periodo UInt8,         -- 0 = sin período mensual
  area  UInt8,           -- 0 = sin área (placeholder para compatibilidad)
  geo   String,

  /* Denominador general y válidos por indicador */
  sw_resp Float64,

  s_valid_democ_supp Float64,
  s_valid_democ_satis Float64,
  s_valid_lr Float64,
  s_valid_econ_sit Float64,

  s_valid_conf_congress Float64,
  s_valid_conf_judiciary Float64,
  s_valid_conf_church Float64,
  s_valid_conf_police Float64,
  s_valid_conf_army Float64,
  s_valid_conf_parties Float64,

  s_valid_goods_wash_mach Float64,
  s_valid_goods_car Float64,
  s_valid_goods_sewage Float64,
  s_valid_goods_hot_water Float64,

  /* Indicadores solicitados (numeradores) */
  s_democ_support_dem  Float64,  -- democ_supp = 1
  s_democ_support_auth Float64,  -- democ_supp = 2
  s_democ_satis        Float64,  -- democ_satis = 1

  s_left_lean  Float64,          -- left_right_scale 0-4
  s_right_lean Float64,          -- left_right_scale 5-10

  s_econ_good Float64,           -- econ_situation 1-2
  s_econ_bad  Float64,           -- econ_situation 4-5

  s_goods_wash_mach Float64,     -- goods_wash_mach = 1
  s_goods_car       Float64,     -- goods_car = 1
  s_goods_sewage    Float64,     -- goods_sewage = 1
  s_goods_hot_water Float64,     -- goods_hot_water = 1

  s_conf_congress_high Float64,  -- confidence_congress IN (1,2)
  s_conf_congress_low  Float64,  -- confidence_congress IN (3,4)

  s_conf_judiciary_high Float64,
  s_conf_judiciary_low  Float64,

  s_conf_church_high Float64,
  s_conf_church_low  Float64,

  s_conf_police_high Float64,
  s_conf_police_low  Float64,

  s_conf_army_high Float64,
  s_conf_army_low  Float64,

  s_conf_parties_high Float64,
  s_conf_parties_low  Float64
)
ENGINE = SummingMergeTree
ORDER BY (level, anio, periodo, area, geo);

/* ===================================================
   MV Latinobarometro → latinobarometro_sums
   =================================================== */

DROP VIEW IF EXISTS indicadores.mv_latinobarometro_all_levels;
CREATE MATERIALIZED VIEW indicadores.mv_latinobarometro_all_levels
TO indicadores.latinobarometro_sums
AS
SELECT
  tup.1 AS level,
  tup.2 AS anio,
  toUInt8(0) AS periodo,
  toUInt8(0) AS area,
  tup.5 AS geo,
  sum(w) AS sw_resp,

  /* válidos */
  sumIf(w, democ_supp_v)  AS s_valid_democ_supp,
  sumIf(w, democ_satis_v) AS s_valid_democ_satis,
  sumIf(w, lr_v)          AS s_valid_lr,
  sumIf(w, econ_v)        AS s_valid_econ_sit,
  sumIf(w, conf_congress_v)  AS s_valid_conf_congress,
  sumIf(w, conf_judiciary_v) AS s_valid_conf_judiciary,
  sumIf(w, conf_church_v)    AS s_valid_conf_church,
  sumIf(w, conf_police_v)    AS s_valid_conf_police,
  sumIf(w, conf_army_v)      AS s_valid_conf_army,
  sumIf(w, conf_parties_v)   AS s_valid_conf_parties,
  sumIf(w, goods_wash_mach_v) AS s_valid_goods_wash_mach,
  sumIf(w, goods_car_v)       AS s_valid_goods_car,
  sumIf(w, goods_sewage_v)    AS s_valid_goods_sewage,
  sumIf(w, goods_hot_water_v) AS s_valid_goods_hot_water,

  /* numeradores */
  sumIf(w, democ_supp = 1)                    AS s_democ_support_dem,
  sumIf(w, democ_supp = 2)                    AS s_democ_support_auth,
  sumIf(w, democ_satis = 1)                   AS s_democ_satis,
  sumIf(w, left_right_scale BETWEEN 0 AND 4)  AS s_left_lean,
  sumIf(w, left_right_scale BETWEEN 5 AND 10) AS s_right_lean,
  sumIf(w, econ_situation BETWEEN 1 AND 2)    AS s_econ_good,
  sumIf(w, econ_situation BETWEEN 4 AND 5)    AS s_econ_bad,
  sumIf(w, goods_wash_mach = 1)               AS s_goods_wash_mach,
  sumIf(w, goods_car = 1)                     AS s_goods_car,
  sumIf(w, goods_sewage = 1)                  AS s_goods_sewage,
  sumIf(w, goods_hot_water = 1)               AS s_goods_hot_water,
  sumIf(w, confidence_congress IN (1,2))      AS s_conf_congress_high,
  sumIf(w, confidence_congress IN (3,4))      AS s_conf_congress_low,
  sumIf(w, confidence_judiciary IN (1,2))     AS s_conf_judiciary_high,
  sumIf(w, confidence_judiciary IN (3,4))     AS s_conf_judiciary_low,
  sumIf(w, confidence_church IN (1,2))        AS s_conf_church_high,
  sumIf(w, confidence_church IN (3,4))        AS s_conf_church_low,
  sumIf(w, confidence_police IN (1,2))        AS s_conf_police_high,
  sumIf(w, confidence_police IN (3,4))        AS s_conf_police_low,
  sumIf(w, confidence_army IN (1,2))          AS s_conf_army_high,
  sumIf(w, confidence_army IN (3,4))          AS s_conf_army_low,
  sumIf(w, confidence_political_parties IN (1,2)) AS s_conf_parties_high,
  sumIf(w, confidence_political_parties IN (3,4)) AS s_conf_parties_low

FROM
(
  SELECT
    l.*,
    toFloat64(1) AS w,
    toUInt16(research_year) AS anio_i,
    (democ_supp IN (1,2,3))             AS democ_supp_v,
    (democ_satis > 0)                   AS democ_satis_v,
    (left_right_scale BETWEEN 0 AND 10) AS lr_v,
    (econ_situation BETWEEN 1 AND 5)    AS econ_v,
    (confidence_congress IN (1,2,3,4))            AS conf_congress_v,
    (confidence_judiciary IN (1,2,3,4))           AS conf_judiciary_v,
    (confidence_church IN (1,2,3,4))              AS conf_church_v,
    (confidence_police IN (1,2,3,4))              AS conf_police_v,
    (confidence_army IN (1,2,3,4))                AS conf_army_v,
    (confidence_political_parties IN (1,2,3,4))   AS conf_parties_v,
    (goods_wash_mach > 0) AS goods_wash_mach_v,
    (goods_car > 0)       AS goods_car_v,
    (goods_sewage > 0)    AS goods_sewage_v,
    (goods_hot_water > 0) AS goods_hot_water_v,

    /* claves geo */
    toString(resp_country) AS geo_country,
    concat(toString(resp_country), '-', toString(research_region)) AS geo_region,
    concat(toString(resp_country), '-', toString(research_region), '-', toString(research_city)) AS geo_city
  FROM indicadores.latinobarometro AS l
) base
ARRAY JOIN
[
  ('pais',       anio_i, toUInt8(0), toUInt8(0), geo_country),
  ('region',     anio_i, toUInt8(0), toUInt8(0), geo_region),
  ('ciudad',     anio_i, toUInt8(0), toUInt8(0), geo_city),
  ('pais_total', anio_i, toUInt8(0), toUInt8(0), geo_country)
] AS tup
WHERE length(tup.5) > 0
GROUP BY level, anio, periodo, area, geo;


/* ===================================================
   Vistas de indicadores (tasas en %)
   =================================================== */

/* País */
CREATE OR REPLACE VIEW indicadores.indicadores_latino_pais AS
WITH country_map AS
(
  SELECT
    toUInt16(research_year) AS year,
    toString(resp_country)  AS pais_code,
    anyHeavy(country_name)  AS pais_nombre,
    anyHeavy(iso3)          AS pais_iso3
  FROM indicadores.latinobarometro
  GROUP BY year, pais_code
)
SELECT
  s.anio AS year,
  s.geo AS pais_code,
  m.pais_nombre,
  m.pais_iso3,
  round(100 * sum(s.s_democ_support_dem)  / nullIf(sum(s.s_valid_democ_supp), 0), 4) AS tasa_apoyo_democracia,
  round(100 * sum(s.s_democ_support_auth) / nullIf(sum(s.s_valid_democ_supp), 0), 4) AS tasa_apoyo_autoritarismo,
  round(100 * sum(s.s_democ_satis)        / nullIf(sum(s.s_valid_democ_satis), 0), 4) AS tasa_satisfechos_democracia,
  round(100 * sum(s.s_right_lean) / nullIf(sum(s.s_valid_lr), 0), 4) AS tasa_derecha,
  round(100 * sum(s.s_left_lean)  / nullIf(sum(s.s_valid_lr), 0), 4) AS tasa_izquierda,
  round(100 * sum(s.s_econ_good) / nullIf(sum(s.s_valid_econ_sit), 0), 4) AS percepcion_econ_buena,
  round(100 * sum(s.s_econ_bad)  / nullIf(sum(s.s_valid_econ_sit), 0), 4) AS percepcion_econ_mala,
  round(100 * sum(s.s_goods_wash_mach) / nullIf(sum(s.s_valid_goods_wash_mach), 0), 4) AS tasa_bien_lavadora,
  round(100 * sum(s.s_goods_car)       / nullIf(sum(s.s_valid_goods_car), 0), 4)       AS tasa_bien_auto,
  round(100 * sum(s.s_goods_sewage)    / nullIf(sum(s.s_valid_goods_sewage), 0), 4)    AS tasa_bien_alcantarillado,
  round(100 * sum(s.s_goods_hot_water) / nullIf(sum(s.s_valid_goods_hot_water), 0), 4) AS tasa_bien_agua_caliente,
  round(100 * sum(s.s_conf_congress_high) / nullIf(sum(s.s_valid_conf_congress), 0), 4) AS confianza_congreso_mucha,
  round(100 * sum(s.s_conf_congress_low)  / nullIf(sum(s.s_valid_conf_congress), 0), 4) AS confianza_congreso_poca_nada,
  round(100 * sum(s.s_conf_judiciary_high) / nullIf(sum(s.s_valid_conf_judiciary), 0), 4) AS confianza_judicial_mucha,
  round(100 * sum(s.s_conf_judiciary_low)  / nullIf(sum(s.s_valid_conf_judiciary), 0), 4) AS confianza_judicial_poca_nada,
  round(100 * sum(s.s_conf_church_high) / nullIf(sum(s.s_valid_conf_church), 0), 4) AS confianza_iglesia_mucha,
  round(100 * sum(s.s_conf_church_low)  / nullIf(sum(s.s_valid_conf_church), 0), 4) AS confianza_iglesia_poca_nada,
  round(100 * sum(s.s_conf_police_high) / nullIf(sum(s.s_valid_conf_police), 0), 4) AS confianza_policia_mucha,
  round(100 * sum(s.s_conf_police_low)  / nullIf(sum(s.s_valid_conf_police), 0), 4) AS confianza_policia_poca_nada,
  round(100 * sum(s.s_conf_army_high) / nullIf(sum(s.s_valid_conf_army), 0), 4) AS confianza_ffaa_mucha,
  round(100 * sum(s.s_conf_army_low)  / nullIf(sum(s.s_valid_conf_army), 0), 4) AS confianza_ffaa_poca_nada,
  round(100 * sum(s.s_conf_parties_high) / nullIf(sum(s.s_valid_conf_parties), 0), 4) AS confianza_partidos_mucha,
  round(100 * sum(s.s_conf_parties_low)  / nullIf(sum(s.s_valid_conf_parties), 0), 4) AS confianza_partidos_poca_nada
FROM indicadores.latinobarometro_sums s
LEFT JOIN country_map m
  ON m.year = s.anio AND m.pais_code = s.geo
WHERE s.level = 'pais'
GROUP BY s.anio, s.geo, m.pais_nombre, m.pais_iso3
ORDER BY year, pais_nombre, pais_code;



/* Región */
CREATE OR REPLACE VIEW indicadores.indicadores_latino_region AS
WITH country_map AS
(
  SELECT
    toUInt16(research_year) AS year,
    toString(resp_country)  AS pais_code,
    anyHeavy(country_name)  AS pais_nombre,
    anyHeavy(iso3)          AS pais_iso3
  FROM indicadores.latinobarometro
  GROUP BY year, pais_code
),
with_country AS
(
  /* Solo filas de nivel región y con al menos 1 guión en geo: "pais-region" */
  SELECT
    s.*,
    splitByChar('-', s.geo) AS parts,
    splitByChar('-', s.geo)[1] AS pais_code_only
  FROM indicadores.latinobarometro_sums s
  WHERE s.level = 'region'
    AND countSubstrings(s.geo, '-') >= 1
)
SELECT
  w.anio AS year,
  /* extracción segura */
  toString(arrayElement(w.parts, 1))                         AS pais_code,
  toInt32OrNull(arrayElement(w.parts, 2))                    AS region_code,
  cm.pais_nombre,
  cm.pais_iso3,

  round(100 * sum(w.s_democ_support_dem)  / nullIf(sum(w.s_valid_democ_supp), 0), 4) AS tasa_apoyo_democracia,
  round(100 * sum(w.s_democ_support_auth) / nullIf(sum(w.s_valid_democ_supp), 0), 4) AS tasa_apoyo_autoritarismo,
  round(100 * sum(w.s_democ_satis)        / nullIf(sum(w.s_valid_democ_satis), 0), 4) AS tasa_satisfechos_democracia,
  round(100 * sum(w.s_right_lean) / nullIf(sum(w.s_valid_lr), 0), 4) AS tasa_derecha,
  round(100 * sum(w.s_left_lean)  / nullIf(sum(w.s_valid_lr), 0), 4) AS tasa_izquierda,
  round(100 * sum(w.s_econ_good) / nullIf(sum(w.s_valid_econ_sit), 0), 4) AS percepcion_econ_buena,
  round(100 * sum(w.s_econ_bad)  / nullIf(sum(w.s_valid_econ_sit), 0), 4) AS percepcion_econ_mala,
  round(100 * sum(w.s_goods_wash_mach) / nullIf(sum(w.s_valid_goods_wash_mach), 0), 4) AS tasa_bien_lavadora,
  round(100 * sum(w.s_goods_car)       / nullIf(sum(w.s_valid_goods_car), 0), 4)       AS tasa_bien_auto,
  round(100 * sum(w.s_goods_sewage)    / nullIf(sum(w.s_valid_goods_sewage), 0), 4)    AS tasa_bien_alcantarillado,
  round(100 * sum(w.s_goods_hot_water) / nullIf(sum(w.s_valid_goods_hot_water), 0), 4) AS tasa_bien_agua_caliente,
  round(100 * sum(w.s_conf_congress_high) / nullIf(sum(w.s_valid_conf_congress), 0), 4) AS confianza_congreso_mucha,
  round(100 * sum(w.s_conf_congress_low)  / nullIf(sum(w.s_valid_conf_congress), 0), 4) AS confianza_congreso_poca_nada,
  round(100 * sum(w.s_conf_judiciary_high) / nullIf(sum(w.s_valid_conf_judiciary), 0), 4) AS confianza_judicial_mucha,
  round(100 * sum(w.s_conf_judiciary_low)  / nullIf(sum(w.s_valid_conf_judiciary), 0), 4) AS confianza_judicial_poca_nada,
  round(100 * sum(w.s_conf_church_high) / nullIf(sum(w.s_valid_conf_church), 0), 4) AS confianza_iglesia_mucha,
  round(100 * sum(w.s_conf_church_low)  / nullIf(sum(w.s_valid_conf_church), 0), 4) AS confianza_iglesia_poca_nada,
  round(100 * sum(w.s_conf_police_high) / nullIf(sum(w.s_valid_conf_police), 0), 4) AS confianza_policia_mucha,
  round(100 * sum(w.s_conf_police_low)  / nullIf(sum(w.s_valid_conf_police), 0), 4) AS confianza_policia_poca_nada,
  round(100 * sum(w.s_conf_army_high) / nullIf(sum(w.s_valid_conf_army), 0), 4) AS confianza_ffaa_mucha,
  round(100 * sum(w.s_conf_army_low)  / nullIf(sum(w.s_valid_conf_army), 0), 4) AS confianza_ffaa_poca_nada,
  round(100 * sum(w.s_conf_parties_high) / nullIf(sum(w.s_valid_conf_parties), 0), 4) AS confianza_partidos_mucha,
  round(100 * sum(w.s_conf_parties_low)  / nullIf(sum(w.s_valid_conf_parties), 0), 4) AS confianza_partidos_poca_nada
FROM with_country w
LEFT JOIN country_map cm
  ON cm.year = w.anio AND cm.pais_code = w.pais_code_only
/* Opcional: asegura que la región sea válida numéricamente */
/* WHERE region_code IS NOT NULL */
GROUP BY w.anio, pais_code, region_code, cm.pais_nombre, cm.pais_iso3
ORDER BY year, pais_nombre, pais_code, region_code;


/* Ciudad */
CREATE OR REPLACE VIEW indicadores.indicadores_latino_ciudad AS
WITH country_map AS
(
  SELECT
    toUInt16(research_year) AS year,
    toString(resp_country)  AS pais_code,
    anyHeavy(country_name)  AS pais_nombre,
    anyHeavy(iso3)          AS pais_iso3
  FROM indicadores.latinobarometro
  GROUP BY year, pais_code
),
with_country AS
(
  /* Solo filas de nivel ciudad y con al menos 2 guiones en geo: "pais-region-ciudad" */
  SELECT
    s.*,
    splitByChar('-', s.geo) AS parts,
    splitByChar('-', s.geo)[1] AS pais_code_only
  FROM indicadores.latinobarometro_sums s
  WHERE s.level = 'ciudad'
    AND countSubstrings(s.geo, '-') >= 2
)
SELECT
  w.anio AS year,
  /* extracción segura */
  toString(arrayElement(w.parts, 1))          AS pais_code,
  toInt32OrNull(arrayElement(w.parts, 2))     AS region_code,
  toInt32OrNull(arrayElement(w.parts, 3))     AS city_code,
  cm.pais_nombre,
  cm.pais_iso3,

  round(100 * sum(w.s_democ_support_dem)  / nullIf(sum(w.s_valid_democ_supp), 0), 4) AS tasa_apoyo_democracia,
  round(100 * sum(w.s_democ_support_auth) / nullIf(sum(w.s_valid_democ_supp), 0), 4) AS tasa_apoyo_autoritarismo,
  round(100 * sum(w.s_democ_satis)        / nullIf(sum(w.s_valid_democ_satis), 0), 4) AS tasa_satisfechos_democracia,
  round(100 * sum(w.s_right_lean) / nullIf(sum(w.s_valid_lr), 0), 4) AS tasa_derecha,
  round(100 * sum(w.s_left_lean)  / nullIf(sum(w.s_valid_lr), 0), 4) AS tasa_izquierda,
  round(100 * sum(w.s_econ_good) / nullIf(sum(w.s_valid_econ_sit), 0), 4) AS percepcion_econ_buena,
  round(100 * sum(w.s_econ_bad)  / nullIf(sum(w.s_valid_econ_sit), 0), 4) AS percepcion_econ_mala,
  round(100 * sum(w.s_goods_wash_mach) / nullIf(sum(w.s_valid_goods_wash_mach), 0), 4) AS tasa_bien_lavadora,
  round(100 * sum(w.s_goods_car)       / nullIf(sum(w.s_valid_goods_car), 0), 4)       AS tasa_bien_auto,
  round(100 * sum(w.s_goods_sewage)    / nullIf(sum(w.s_valid_goods_sewage), 0), 4)    AS tasa_bien_alcantarillado,
  round(100 * sum(w.s_goods_hot_water) / nullIf(sum(w.s_valid_goods_hot_water), 0), 4) AS tasa_bien_agua_caliente,
  round(100 * sum(w.s_conf_congress_high) / nullIf(sum(w.s_valid_conf_congress), 0), 4) AS confianza_congreso_mucha,
  round(100 * sum(w.s_conf_congress_low)  / nullIf(sum(w.s_valid_conf_congress), 0), 4) AS confianza_congreso_poca_nada,
  round(100 * sum(w.s_conf_judiciary_high) / nullIf(sum(w.s_valid_conf_judiciary), 0), 4) AS confianza_judicial_mucha,
  round(100 * sum(w.s_conf_judiciary_low)  / nullIf(sum(w.s_valid_conf_judiciary), 0), 4) AS confianza_judicial_poca_nada,
  round(100 * sum(w.s_conf_church_high) / nullIf(sum(w.s_valid_conf_church), 0), 4) AS confianza_iglesia_mucha,
  round(100 * sum(w.s_conf_church_low)  / nullIf(sum(w.s_valid_conf_church), 0), 4) AS confianza_iglesia_poca_nada,
  round(100 * sum(w.s_conf_police_high) / nullIf(sum(w.s_valid_conf_police), 0), 4) AS confianza_policia_mucha,
  round(100 * sum(w.s_conf_police_low)  / nullIf(sum(w.s_valid_conf_police), 0), 4) AS confianza_policia_poca_nada,
  round(100 * sum(w.s_conf_army_high) / nullIf(sum(w.s_valid_conf_army), 0), 4) AS confianza_ffaa_mucha,
  round(100 * sum(w.s_conf_army_low)  / nullIf(sum(w.s_valid_conf_army), 0), 4) AS confianza_ffaa_poca_nada,
  round(100 * sum(w.s_conf_parties_high) / nullIf(sum(w.s_valid_conf_parties), 0), 4) AS confianza_partidos_mucha,
  round(100 * sum(w.s_conf_parties_low)  / nullIf(sum(w.s_valid_conf_parties), 0), 4) AS confianza_partidos_poca_nada
FROM with_country w
LEFT JOIN country_map cm
  ON cm.year = w.anio AND cm.pais_code = w.pais_code_only
/* Opcional: asegura validez numérica */
/* WHERE region_code IS NOT NULL AND city_code IS NOT NULL */
GROUP BY w.anio, pais_code, region_code, city_code, cm.pais_nombre, cm.pais_iso3
ORDER BY year, pais_nombre, pais_code, region_code, city_code;


-- ===================================================
-- Tabla VDEM
-- ===================================================
CREATE TABLE IF NOT EXISTS indicadores.vdem (
    country_name  String,
    country_text_id  String,
    country_id  Int32,
    year  Int32,
    historical_date  Date,
    project  Int32,
    historical  Int32,
    histname  String,
    codingstart  Int32,
    codingend  Int32,
    codingstart_contemp  Int32,
    codingend_contemp  Int32,
    codingstart_hist  Nullable(Int32),
    codingend_hist  Nullable(Int32),
    gapstart1  Nullable(String),
    gapstart2  Nullable(String),
    gapstart3  Nullable(String),
    gapend1  Nullable(String),
    gapend2  Nullable(String),
    gapend3  Nullable(String),
    gap_index  Int32,
    COWcode  Int32,
    v2x_polyarchy  Float64,
    v2x_libdem  Float64,
    v2x_partipdem  Float64,
    v2x_delibdem  Nullable(Float64),
    v2x_egaldem  Nullable(Float64),
    -- v2x_api  Float64,
    -- v2x_mpi  Float64,
    v2x_freexp_altinf  Float64,
    v2xel_frefair  Float64,
    -- v2x_liberal  Float64,
    v2xcl_rol  Float64,
    v2x_jucon  Float64,
    v2xlg_legcon  Nullable(Float64),
    -- v2x_partip  Float64,
    v2xeg_eqprotec  Float64,
    v2xeg_eqaccess  Float64,
    v2xeg_eqdr  Nullable(Float64),
    -- Distribución de poder
    v2pepwrses Float64,
    v2pepwrsoc Float64,
    v2pepwrgen Float64,
    v2pepwrort Float64,
    v2pepwrgeo Float64
)
ENGINE = MergeTree
ORDER BY (country_id, year);