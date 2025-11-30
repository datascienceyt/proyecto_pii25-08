// src/pages/IndicatorsPage.jsx
import React from "react";

const Frac = ({ num, den }) => (
  <span className="bases-fraction">
    <span className="bases-fraction-num">{num}</span>
    <span className="bases-fraction-den">{den}</span>
  </span>
);

const indicatorsTable = [
  // =======================
  // ENEMDU (Ecuador)
  // =======================
  {
    source: "ENEMDU (Ecuador)",
    name: "Tasa de participación global",
    formula: (
      <>
        TPG = 100 ×{" "}
        <Frac
          num={
            <>
              Σ<sub>i∈PEA</sub> w<sub>i</sub>
            </>
          }
          den={
            <>
              Σ<sub>i∈PET</sub> w<sub>i</sub>
            </>
          }
        />
      </>
    ),
    geo: { nat: true, prov: true, cant: true, parr: true },
    temp: { annual: true, monthly: true },
    period: { from: "2007", to: "2025" },
  },
  {
    source: "ENEMDU (Ecuador)",
    name: "Tasa de participación bruta",
    formula: (
      <>
        TPB = 100 ×{" "}
        <Frac
          num={
            <>
              Σ<sub>i∈PEA</sub> w<sub>i</sub>
            </>
          }
          den={
            <>
              Σ<sub>i∈Población total</sub> w<sub>i</sub>
            </>
          }
        />
      </>
    ),
    geo: { nat: true, prov: true, cant: true, parr: true },
    temp: { annual: true, monthly: true },
    period: { from: "2007", to: "2025" },
  },
  {
    source: "ENEMDU (Ecuador)",
    name: "Tasa de desempleo",
    formula: (
      <>
        TD = 100 ×{" "}
        <Frac
          num={
            <>
              Σ<sub>i∈Desempleados</sub> w<sub>i</sub>
            </>
          }
          den={
            <>
              Σ<sub>i∈PEA</sub> w<sub>i</sub>
            </>
          }
        />
      </>
    ),
    geo: { nat: true, prov: true, cant: true, parr: true },
    temp: { annual: true, monthly: true },
    period: { from: "2007", to: "2025" },
  },
  {
    source: "ENEMDU (Ecuador)",
    name: "Empleo total",
    formula: (
      <>
        ET = 100 ×{" "}
        <Frac
          num={
            <>
              Σ<sub>i∈Ocupados</sub> w<sub>i</sub>
            </>
          }
          den={
            <>
              Σ<sub>i∈PEA</sub> w<sub>i</sub>
            </>
          }
        />
      </>
    ),
    geo: { nat: true, prov: true, cant: true, parr: true },
    temp: { annual: true, monthly: true },
    period: { from: "2007", to: "2025" },
  },
  {
    source: "ENEMDU (Ecuador)",
    name: "Empleo formal",
    formula: (
      <>
        EF = 100 ×{" "}
        <Frac
          num={
            <>
              Σ<sub>i∈Empleo formal</sub> w<sub>i</sub>
            </>
          }
          den={
            <>
              Σ<sub>i∈Ocupados</sub> w<sub>i</sub>
            </>
          }
        />
      </>
    ),
    geo: { nat: true, prov: true, cant: true, parr: true },
    temp: { annual: true, monthly: true },
    period: { from: "2007", to: "2025" },
  },
  {
    source: "ENEMDU (Ecuador)",
    name: "Empleo informal",
    formula: (
      <>
        EI = 100 ×{" "}
        <Frac
          num={
            <>
              Σ<sub>i∈Empleo informal</sub> w<sub>i</sub>
            </>
          }
          den={
            <>
              Σ<sub>i∈Ocupados</sub> w<sub>i</sub>
            </>
          }
        />
      </>
    ),
    geo: { nat: true, prov: true, cant: true, parr: true },
    temp: { annual: true, monthly: true },
    period: { from: "2007", to: "2025" },
  },
  {
    source: "ENEMDU (Ecuador)",
    name: "Empleo adecuado",
    formula: (
      <>
        EA = 100 ×{" "}
        <Frac
          num={
            <>
              Σ<sub>i∈Empleo adecuado</sub> w<sub>i</sub>
            </>
          }
          den={
            <>
              Σ<sub>i∈PEA</sub> w<sub>i</sub>
            </>
          }
        />
      </>
    ),
    geo: { nat: true, prov: true, cant: true, parr: true },
    temp: { annual: true, monthly: true },
    period: { from: "2007", to: "2025" },
  },
  {
    source: "ENEMDU (Ecuador)",
    name: "Subempleo",
    formula: (
      <>
        SUB = 100 ×{" "}
        <Frac
          num={
            <>
              Σ<sub>i∈Subempleados</sub> w<sub>i</sub>
            </>
          }
          den={
            <>
              Σ<sub>i∈PEA</sub> w<sub>i</sub>
            </>
          }
        />
      </>
    ),
    geo: { nat: true, prov: true, cant: true, parr: true },
    temp: { annual: true, monthly: true },
    period: { from: "2007", to: "2025" },
  },
  {
    source: "ENEMDU (Ecuador)",
    name: "Empleo no remunerado",
    formula: (
      <>
        ENR = 100 ×{" "}
        <Frac
          num={
            <>
              Σ<sub>i∈Empleo no remunerado</sub> w<sub>i</sub>
            </>
          }
          den={
            <>
              Σ<sub>i∈Ocupados</sub> w<sub>i</sub>
            </>
          }
        />
      </>
    ),
    geo: { nat: true, prov: true, cant: true, parr: true },
    temp: { annual: true, monthly: true },
    period: { from: "2007", to: "2025" },
  },
  {
    source: "ENEMDU (Ecuador)",
    name: "Otro empleo no pleno",
    formula: (
      <>
        OEP = 100 ×{" "}
        <Frac
          num={
            <>
              Σ<sub>i∈Otro empleo no pleno</sub> w<sub>i</sub>
            </>
          }
          den={
            <>
              Σ<sub>i∈PEA</sub> w<sub>i</sub>
            </>
          }
        />
      </>
    ),
    geo: { nat: true, prov: true, cant: true, parr: true },
    temp: { annual: true, monthly: true },
    period: { from: "2007", to: "2025" },
  },
  {
    source: "ENEMDU (Ecuador)",
    name: "Brecha salarial entre hombres y mujeres",
    formula: (
      <>
        Brecha<sub>HM</sub> = 100 ×{" "}
        <Frac
          num={
            <>
              ȳ<sub>h</sub> − ȳ<sub>m</sub>
            </>
          }
          den={
            <>
              ȳ<sub>h</sub>
            </>
          }
        />
      </>
    ),
    geo: { nat: true, prov: true, cant: true, parr: true },
    temp: { annual: true, monthly: true },
    period: { from: "2007", to: "2025" },
  },
  {
    source: "ENEMDU (Ecuador)",
    name: "Brecha de empleo adecuado (hombre/mujer)",
    formula: (
      <>
        BrechaEA<sub>HM</sub> = 100 ×{" "}
        <Frac
          num={
            <>
              EA<sub>h</sub> − EA<sub>m</sub>
            </>
          }
          den={
            <>
              EA<sub>h</sub>
            </>
          }
        />
      </>
    ),
    geo: { nat: true, prov: true, cant: true, parr: true },
    temp: { annual: true, monthly: true },
    period: { from: "2007", to: "2025" },
  },
  {
    source: "ENEMDU (Ecuador)",
    name: "Jóvenes que no estudian ni trabajan (NiNi)",
    formula: (
      <>
        NiNi = 100 ×{" "}
        <Frac
          num={
            <>
              Σ<sub>i∈NiNi</sub> w<sub>i</sub>
            </>
          }
          den={
            <>
              Σ<sub>i∈Población joven</sub> w<sub>i</sub>
            </>
          }
        />
      </>
    ),
    geo: { nat: true, prov: true, cant: true, parr: true },
    temp: { annual: true, monthly: true },
    period: { from: "2007", to: "2025" },
  },
  {
    source: "ENEMDU (Ecuador)",
    name: "Desempleo juvenil",
    formula: (
      <>
        TDJ = 100 ×{" "}
        <Frac
          num={
            <>
              Σ<sub>i∈Desempleados jóvenes</sub> w<sub>i</sub>
            </>
          }
          den={
            <>
              Σ<sub>i∈PEA juvenil</sub> w<sub>i</sub>
            </>
          }
        />
      </>
    ),
    geo: { nat: true, prov: true, cant: true, parr: true },
    temp: { annual: true, monthly: true },
    period: { from: "2007", to: "2025" },
  },
  {
    source: "ENEMDU (Ecuador)",
    name: "Trabajo infantil",
    formula: (
      <>
        TI = 100 ×{" "}
        <Frac
          num={
            <>
              Σ<sub>i∈Niños con trabajo infantil</sub> w<sub>i</sub>
            </>
          }
          den={
            <>
              Σ<sub>i∈Niños</sub> w<sub>i</sub>
            </>
          }
        />
      </>
    ),
    geo: { nat: true, prov: true, cant: true, parr: true },
    temp: { annual: true, monthly: true },
    period: { from: "2007", to: "2025" },
  },
  {
    source: "ENEMDU (Ecuador)",
    name: "Tasa de asistencia a clases",
    formula: (
      <>
        TAC = 100 ×{" "}
        <Frac
          num={
            <>
              Σ<sub>i∈Asisten a clases (5–24)</sub> w<sub>i</sub>
            </>
          }
          den={
            <>
              Σ<sub>i∈Población 5–24</sub> w<sub>i</sub>
            </>
          }
        />
      </>
    ),
    geo: { nat: true, prov: true, cant: true, parr: true },
    temp: { annual: true, monthly: true },
    period: { from: "2007", to: "2025" },
  },
  {
    source: "ENEMDU (Ecuador)",
    name: "Empleo en manufactura",
    formula: (
      <>
        EMM = 100 ×{" "}
        <Frac
          num={
            <>
              Σ<sub>i∈Ocupados en manufactura</sub> w<sub>i</sub>
            </>
          }
          den={
            <>
              Σ<sub>i∈Ocupados</sub> w<sub>i</sub>
            </>
          }
        />
      </>
    ),
    geo: { nat: true, prov: true, cant: true, parr: true },
    temp: { annual: true, monthly: true },
    period: { from: "2007", to: "2025" },
  },
  {
    source: "ENEMDU (Ecuador)",
    name: "Pobreza por ingresos",
    formula: (
      <>
        Pobreza = 100 ×{" "}
        <Frac
          num={
            <>
              Σ<sub>i∈Bajo línea de pobreza</sub> w<sub>i</sub>
            </>
          }
          den={
            <>
              Σ<sub>i∈Población con ingreso válido</sub> w<sub>i</sub>
            </>
          }
        />
      </>
    ),
    geo: { nat: true, prov: true, cant: true, parr: true },
    temp: { annual: true, monthly: true },
    period: { from: "2007", to: "2025" },
  },
  {
    source: "ENEMDU (Ecuador)",
    name: "Pobreza extrema por ingresos",
    formula: (
      <>
        PobrezaExt = 100 ×{" "}
        <Frac
          num={
            <>
              Σ<sub>i∈Bajo línea de pobreza extrema</sub> w<sub>i</sub>
            </>
          }
          den={
            <>
              Σ<sub>i∈Población con ingreso válido</sub> w<sub>i</sub>
            </>
          }
        />
      </>
    ),
    geo: { nat: true, prov: true, cant: true, parr: true },
    temp: { annual: true, monthly: true },
    period: { from: "2007", to: "2025" },
  },
  {
    source: "ENEMDU (Ecuador)",
    name: "Tasa de pobreza por necesidades básicas insatisfechas",
    formula: (
      <>
        NBI = 100 × (1/n) × Σ<sub>k=1</sub>
        <sup>n</sup> P<sub>k</sub>
        <sup>*</sup>
      </>
    ),
    geo: { nat: true, prov: true, cant: true, parr: true },
    temp: { annual: true, monthly: true },
    period: { from: "2007", to: "2025" },
  },
  {
    source: "ENEMDU (Ecuador)",
    name: "Tasa de pobreza multidimensional",
    formula: (
      <>
        TPM = 100 × (1/n) × Σ<sub>i=1</sub>
        <sup>n</sup> I(c<sub>i</sub> ≥ k)
      </>
    ),
    geo: { nat: true, prov: true, cant: true, parr: true },
    temp: { annual: true, monthly: true },
    period: { from: "2007", to: "2025" },
  },
  {
    source: "ENEMDU (Ecuador)",
    name: "Tasa de pobreza extrema multidimensional",
    formula: (
      <>
        TPEM = 100 × (1/n) × Σ<sub>i=1</sub>
        <sup>n</sup> I(c<sub>i</sub> ≥ k
        <sup>ext</sup>)
      </>
    ),
    geo: { nat: true, prov: true, cant: true, parr: true },
    temp: { annual: true, monthly: true },
    period: { from: "2007", to: "2025" },
  },

  // =======================
  // Latinobarómetro
  // =======================
  {
    source: "Latinobarómetro",
    name: "Apoyo a la democracia",
    formula: "Variable directa o recodificada de democ_supp",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1995", to: "2024" },
  },
  {
    source: "Latinobarómetro",
    name: "Indiferencia o apoyo a alternativas autoritarias",
    formula: "Recodificación de democ_supp",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1995", to: "2024" },
  },
  {
    source: "Latinobarómetro",
    name: "Satisfacción con la democracia",
    formula: "Variable directa o recodificada de democ_satis",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1995", to: "2024" },
  },
  {
    source: "Latinobarómetro",
    name: "Ubicación ideológica izquierda–centro–derecha",
    formula: "Variable directa o recodificada de left_right_scale",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1995", to: "2024" },
  },
  {
    source: "Latinobarómetro",
    name: "Evaluación de la situación económica del país",
    formula: "Variable directa o recodificada de econ_situation",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1995", to: "2024" },
  },
  {
    source: "Latinobarómetro",
    name: "Evaluación de la situación económica personal",
    formula:
      "Variable directa o recodificada de resp_economic_perception",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1995", to: "2024" },
  },
  {
    source: "Latinobarómetro",
    name: "Preocupación por perder el empleo",
    formula: "Variable directa o recodificada de job_concern",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1995", to: "2024" },
  },
  {
    source: "Latinobarómetro",
    name: "Tenencia de bienes y servicios en el hogar",
    formula: "Variable directa o recodificada de goods_car",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1995", to: "2024" },
  },
  {
    source: "Latinobarómetro",
    name: "Confianza en instituciones",
    formula: "Índices de confianza agregados (variables trust_*)",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1995", to: "2024" },
  },
  {
    source: "Latinobarómetro",
    name: "Otras variables normalizadas de contexto",
    formula:
      "Conjunto de variables normalizadas de contexto (sexo, edad, educación, etc.)",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1995", to: "2024" },
  },

  // =======================
  // V-Dem
  // =======================
  {
    source: "V-Dem",
    name: "Índice de democracia electoral (v2x_polyarchy)",
    formula: "Variable directa: v2x_polyarchy",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1789", to: "2024" },
  },
  {
    source: "V-Dem",
    name: "Índice de democracia liberal (v2x_libdem)",
    formula: "Variable directa: v2x_libdem",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1789", to: "2024" },
  },
  {
    source: "V-Dem",
    name: "Índice de democracia participativa (v2x_partipdem)",
    formula: "Variable directa: v2x_partipdem",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1789", to: "2024" },
  },
  {
    source: "V-Dem",
    name: "Índice de democracia deliberativa (v2x_delibdem)",
    formula: "Variable directa: v2x_delibdem",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1789", to: "2024" },
  },
  {
    source: "V-Dem",
    name: "Índice de democracia igualitaria (v2x_egaldem)",
    formula: "Variable directa: v2x_egaldem",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1789", to: "2024" },
  },
  {
    source: "V-Dem",
    name:
      "Libertad de expresión y fuentes alternativas de información (v2x_freexp_altinf)",
    formula: "Variable directa: v2x_freexp_altinf",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1789", to: "2024" },
  },
  {
    source: "V-Dem",
    name:
      "Integridad de elecciones (índice de elecciones libres y justas, v2xel_frefair)",
    formula: "Variable directa: v2xel_frefair",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1789", to: "2024" },
  },
  {
    source: "V-Dem",
    name:
      "Igualdad ante la ley y libertades individuales (v2xcl_rol)",
    formula: "Variable directa: v2xcl_rol",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1789", to: "2024" },
  },
  {
    source: "V-Dem",
    name:
      "Controles judiciales sobre el ejecutivo (v2x_jucon)",
    formula: "Variable directa: v2x_jucon",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1789", to: "2024" },
  },
  {
    source: "V-Dem",
    name:
      "Controles legislativos sobre el ejecutivo (v2xlg_legcon)",
    formula: "Variable directa: v2xlg_legcon",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1789", to: "2024" },
  },
  {
    source: "V-Dem",
    name: "Igual protección legal (v2xeg_eqprotec)",
    formula: "Variable directa: v2xeg_eqprotec",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1789", to: "2024" },
  },
  {
    source: "V-Dem",
    name: "Igual acceso a recursos públicos (v2xeg_eqaccess)",
    formula: "Variable directa: v2xeg_eqaccess",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1789", to: "2024" },
  },
  {
    source: "V-Dem",
    name: "Igual distribución de recursos (v2xeg_eqdr)",
    formula: "Variable directa: v2xeg_eqdr",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1789", to: "2024" },
  },
  {
    source: "V-Dem",
    name:
      "Distribución del poder por estatus socioeconómico (v2pepwrses)",
    formula: "Variable directa: v2pepwrses",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1789", to: "2024" },
  },
  {
    source: "V-Dem",
    name:
      "Distribución del poder por grupo social (v2pepwrsoc)",
    formula: "Variable directa: v2pepwrsoc",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1789", to: "2024" },
  },
  {
    source: "V-Dem",
    name: "Distribución del poder por género (v2pepwrgen)",
    formula: "Variable directa: v2pepwrgen",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1789", to: "2024" },
  },
  {
    source: "V-Dem",
    name:
      "Distribución del poder por orientación religiosa (v2pepwrort)",
    formula: "Variable directa: v2pepwrort",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1789", to: "2024" },
  },
  {
    source: "V-Dem",
    name:
      "Distribución del poder por región geográfica (v2pepwrgeo)",
    formula: "Variable directa: v2pepwrgeo",
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1789", to: "2024" },
  },
];


const BasesUsadasPage = () => {
  const yes = "✓";
  const no = "—";

  return (
    <div className="page bases-page">
      {/* HERO */}
      <section className="bases-hero">
        <div className="bases-hero-content">
          <p className="project-tag">Bases de datos</p>
          <h1 className="project-title">Fuentes de información utilizadas</h1>
          <p className="project-hero-text">
            El proyecto combina información de tres fuentes principales: V-Dem,
            Latinobarómetro y ENEMDU (Ecuador). Cada una aporta una dimensión
            distinta para comprender la relación entre desigualdad y democracia
            en Latinoamérica.
          </p>
        </div>

        <div className="bases-hero-summary">
          <h3>En una mirada</h3>

          <div className="bases-hero-highlights">
            <article className="bases-hero-highlight">
              <a
                href="https://www.v-dem.net/"
                target="_blank"
                rel="noopener noreferrer"
                className="bases-hero-highlight-link"
              >
                <div className="bases-hero-highlight-icon bases-hero-highlight-icon--vdem">
                  <span role="img" aria-label="Instituciones">
                    🏛️
                  </span>
                </div>
                <div className="bases-hero-highlight-text">
                  <h4>V-Dem</h4>
                  <p>Indicadores institucionales de calidad democrática.</p>
                </div>
              </a>
            </article>

            <article className="bases-hero-highlight">
              <a
                href="https://www.latinobarometro.org/"
                target="_blank"
                rel="noopener noreferrer"
                className="bases-hero-highlight-link"
              >
                <div className="bases-hero-highlight-icon bases-hero-highlight-icon--latino">
                  <span role="img" aria-label="Ciudadanía">
                    🧑‍🤝‍🧑
                  </span>
                </div>
                <div className="bases-hero-highlight-text">
                  <h4>Latinobarómetro</h4>
                  <p>Opinión pública y percepción ciudadana sobre la democracia.</p>
                </div>
              </a>
            </article>

            <article className="bases-hero-highlight">
              <a
                href="https://www.ecuadorencifras.gob.ec/enemdu-anual/"
                target="_blank"
                rel="noopener noreferrer"
                className="bases-hero-highlight-link"
              >
                <div className="bases-hero-highlight-icon bases-hero-highlight-icon--enemdu">
                  <span role="img" aria-label="Economía">
                    💼
                  </span>
                </div>
                <div className="bases-hero-highlight-text">
                  <h4>ENEMDU (Ecuador)</h4>
                  <p>Condiciones socioeconómicas y mercado laboral en Ecuador.</p>
                </div>
              </a>
            </article>
          </div>
        </div>
      </section>

      {/* CARDS PRINCIPALES */}
      <section className="bases-section bases-section-alt">
        <div className="project-section-header">
          <h2 className="project-section-title">Panorama de las bases de datos</h2>
          <p className="project-section-text">
            A continuación se resumen las características básicas de cada fuente
            de información, incluyendo años considerados, cobertura geográfica y
            tipo de variables utilizadas en los indicadores.
          </p>
        </div>

        <div className="bases-grid">
          <article className="bases-card bases-card--vdem">
            <h3>V-Dem (Varieties of Democracy)</h3>
            <p>
              Base internacional que ofrece índices detallados sobre distintas
              dimensiones de la democracia: electoral, liberal, participativa,
              deliberativa e igualitaria, entre otras.
            </p>
            <ul>
              <li>Unidad de análisis: país-año.</li>
              <li>Cobertura: 19 países de América Latina.</li>
              <li>Principales índices: democracia electoral, liberal, etc.</li>
            </ul>
            <a
              href="https://www.v-dem.net/"
              target="_blank"
              rel="noopener noreferrer"
              className="methodology-doc-link"
            >
              Visitar Sitio
            </a>
          </article>

          <article className="bases-card bases-card--latino">
            <h3>Latinobarómetro</h3>
            <p>
              Encuesta de opinión pública que recoge percepciones ciudadanas
              sobre democracia, economía, instituciones y valores políticos en
              la región.
            </p>
            <ul>
              <li>Unidad de análisis: individuo (agregado a país-año).</li>
              <li>
                Variables clave: apoyo a la democracia, satisfacción, confianza
                institucional, autoubicación ideológica, entre otras.
              </li>
              <li>Uso de ponderadores muestrales oficiales.</li>
            </ul>
            <a
              href="https://www.latinobarometro.org/#"
              target="_blank"
              rel="noopener noreferrer"
              className="methodology-doc-link"
            >
              Visitar Sitio
            </a>
          </article>

          <article className="bases-card bases-card--enemdu">
            <h3>ENEMDU (Ecuador)</h3>
            <p>
              Encuesta nacional de empleo, desempleo y subempleo de Ecuador,
              utilizada para construir indicadores de desigualdad y condiciones
              socioeconómicas comparables con el resto de la región.
            </p>
            <ul>
              <li>Unidad de análisis: hogar e individuo (agregado a año).</li>
              <li>
                Indicadores: empleo, ingresos, acceso a servicios y
                características del hogar.
              </li>
              <li>
                Permite comparar la situación de Ecuador con la evidencia
                regional.
              </li>
            </ul>
            <a
              href="https://www.ecuadorencifras.gob.ec/enemdu-anual/"
              target="_blank"
              rel="noopener noreferrer"
              className="methodology-doc-link"
            >
              Visitar Sitio
            </a>
          </article>
        </div>
      </section>

      {/* DETALLE COMPARATIVO RÁPIDO */}
      <section className="bases-section">
        <div className="project-section-header">
          <h2 className="project-section-title">
            Cobertura y estructura de las bases
          </h2>
          <p className="project-section-text">
            La siguiente síntesis puede ajustarse con los años exactos, número
            de observaciones y olas de encuesta que finalmente se utilicen en el
            proyecto.
          </p>
        </div>

        <div className="bases-table">
          <div className="bases-table-header">
            <span>Base</span>
            <span>Cobertura temporal</span>
            <span>Unidad principal</span>
            <span>Tipo de variables</span>
          </div>
          <div className="bases-table-row">
            <span>V-Dem</span>
            <span>1789 - 2024</span>
            <span>País - año</span>
            <span>Índices de democracia y componentes institucionales.</span>
          </div>
          <div className="bases-table-row">
            <span>Latinobarómetro</span>
            <span>1995 - 2024 (olas disponibles)</span>
            <span>Individuo (agregado a país - año)</span>
            <span>
              Percepción democrática, confianza, evaluación económica y valores
              políticos.
            </span>
          </div>
          <div className="bases-table-row">
            <span>ENEMDU</span>
            <span>2007 - 2025</span>
            <span>Hogar / individuo (Ecuador)</span>
            <span>
              Condiciones socioeconómicas, situación laboral y características
              del hogar.
            </span>
          </div>
        </div>
      </section>

      {/* TABLA CONJUNTA DE INDICADORES */}
      <section className="bases-section bases-section-alt bases-section-wide">
        <div className="project-section-header">
          <h2 className="project-section-title">
            Resumen conjunto de indicadores
          </h2>
          <p className="project-section-text">
            A continuación se presenta una tabla de referencia rápida con todos
            los indicadores utilizados en el proyecto, indicando su fuente,
            fórmula (en términos generales), nivel de desagregación geográfica,
            desagregación temporal y periodo de cobertura.
          </p>
        </div>

        <div className="bases-indicators-table-wrapper">
          <table className="bases-indicators-table">
            <colgroup>
              <col className="col-source" />
              <col className="col-indicator" />
              <col className="col-formula" />
              <col className="col-small" span="8" />
            </colgroup>
            <thead>
              <tr>
                <th rowSpan={2}>Fuente</th>
                <th rowSpan={2}>Indicador</th>
                <th rowSpan={2}>Fórmula</th>
                <th colSpan={4}>Desagregación geográfica</th>
                <th colSpan={2}>Desagregación temporal</th>
                <th colSpan={2}>Periodo</th>
              </tr>
              <tr>
                <th>Nacional</th>
                <th>Provincial</th>
                <th>Cantonal</th>
                <th>Parroquial</th>
                <th>Anual</th>
                <th>Mensual</th>
                <th>Desde</th>
                <th>Hasta</th>
              </tr>
            </thead>
            <tbody>
              {indicatorsTable.map((ind) => (
                <tr
                  key={`${ind.source}-${ind.name}`}
                  className={`bases-indicators-row bases-indicators-row--${ind.rowClass ||
                    ind.source
                      .toLowerCase()
                      .normalize("NFD")
                      .replace(/[\u0300-\u036f]/g, "")
                      .replace(/[^a-z0-9]/g, "")
                    }`}
                >
                  <td>{ind.source}</td>
                  <td>{ind.name}</td>
                  <td className="bases-indicators-formula">{ind.formula}</td>
                  <td>{ind.geo.nat ? "✓" : "—"}</td>
                  <td>{ind.geo.prov ? "✓" : "—"}</td>
                  <td>{ind.geo.cant ? "✓" : "—"}</td>
                  <td>{ind.geo.parr ? "✓" : "—"}</td>
                  <td>{ind.temp.annual ? "✓" : "—"}</td>
                  <td>{ind.temp.monthly ? "✓" : "—"}</td>
                  <td>{ind.period.from}</td>
                  <td>{ind.period.to}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

    </div>
  );
};

export default BasesUsadasPage;