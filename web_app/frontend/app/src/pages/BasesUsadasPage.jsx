// src/pages/IndicatorsPage.jsx
import React from "react";

// ------------------------
// ENEMDU
// ------------------------

const enemduIndicators = [
  {
    name: "Tasa de participación global",
    survey: "Persona",
    description: "Es el porcentaje que resulta del cociente entre la Población Económicamente Activa (PEA) y la Población en Edad de Trabajar (PET). Esta tasa resulta más adecuada para medir la participación ya que aísla fenómenos de tipo demográfico.",
  },
  {
    name: "Tasa de participación bruta",
    survey: "Persona",
    description: "Es el porcentaje que resulta del cociente entre la Población Económicamente Activa (PEA) y la Población Total (PT).",
  },
  {
    name: "Tasa de desempleo",
    survey: "Persona",
    description: "Es el porcentaje de personas de 15 años y más en condición de desempleo, respecto a la PEA. Resulta del cociente entre el total de la población de 15 años y más en condición de Desempleo (DESEM) y la Población Económicamente Activa (PEA).",
  },
  {
    name: "Empleo",
    survey: "Persona",
    description: "Corresponde a la proporción de la PEA que se encuentra ocupada (cualquier tipo de empleo: adecuado, inadecuado, subempleo, no remunerado, etc.)",
  },
  {
    name: "Empleo formal",
    survey: "Persona",
    description: "Mide la proporción de personas ocupadas que se encuentran en empleos considerados formales (seguridad social, contrato formal, cumplimiento de normas laborales, etc., según la clasificación oficial empleada en ENEMDU).",
  },
  {
    name: "Empleo informal",
    survey: "Persona",
    description: "Corresponde a la proporción de personas ocupadas que trabajan en condiciones de informalidad (sin seguridad social, sin contrato, en unidades productivas informales, etc.)",
  },
  {
    name: "Empleo adecuado",
    survey: "Persona",
    description: "Es la proporción de la PEA que se encuentra ocupada en empleos que cumplen los criterios de adecuación laboral definidos por la ENEMDU (por ejemplo, horas trabajadas, ingresos iguales o superiores al salario de referencia, estabilidad, seguridad social, etc.).",
  },
  {
    name: "Subempleo",
    survey: "Persona",
    description: "Refleja la proporción de la PEA que se encuentra en una situación de subempleo, generalmente definida como personas ocupadas que trabajan menos horas de las deseadas y/o perciben ingresos inferiores a un umbral de referencia, y que están disponibles para trabajar más.",
  },
  {
    name: "Empleo no remunerado",
    survey: "Persona",
    description: "Mide la proporción de la PEA que realiza actividades económicas sin recibir un pago directo (por ejemplo, trabajo familiar no remunerado en negocios o actividades agrícolas del hogar).",
  },
  {
    name: "Otro empleo no pleno",
    survey: "Persona",
    description: "Mide el porcentaje de personas ocupadas que se encuentran en la categoría de otro empleo no pleno respecto del total de la Población Económicamente Activa (PEA), de acuerdo con la clasificación de condición de empleo utilizada en la ENEMDU. Ejemplo: descripción de Otro empleo no pleno (actualizar).",
  },
  {
    name: "Brecha salarial entre hombres y mujeres",
    survey: "Persona",
    description: "Mide la diferencia porcentual entre el ingreso laboral promedio de los hombres ocupados y el de las mujeres ocupadas",
  },
  {
    name: "Brecha de empleo adecuado (hombre/mujer)",
    survey: "Persona",
    description: "Mide la diferencia relativa en la tasa de empleo adecuado entre hombres y mujeres.",
  },
  {
    name: "Jóvenes que no estudian ni trabajan (NiNi)",
    survey: "Persona",
    description: "Corresponde a la proporción de jóvenes que no estudian ni participan en el mercado laboral (no están ocupados ni buscan empleo), sobre el total de jóvenes en la edad definida para este grupo (típicamente 15–24 años, según la clasificación utilizada en ENEMDU).",
  },
  {
    name: "Desempleo juvenil",
    survey: "Persona",
    description: "Mide la proporción de jóvenes que se encuentran desempleados (búsqueda activa y disponibilidad) sobre el total de jóvenes en la PEA juvenil.",
  },
  {
    name: "Trabajo infantil",
    survey: "Persona",
    description: "Mide la proporción de niñas, niños y adolescentes en el rango de edad definido para trabajo infantil (por ejemplo, 5–14 años, según la normativa vigente) que realizan actividades económicas clasificadas como trabajo infantil",
  },
  {
    name: "Tasa de asistencia a clases",
    survey: "Persona",
    description: "Mide la proporción de niñas, niños y jóvenes de 5 a 24 años que asisten a algún establecimiento educativo formal",
  },
  {
    name: "Empleo en manufactura",
    survey: "Persona",
    description: "Mide la proporción de personas ocupadas que trabajan en actividades de la industria manufacturera (por ejemplo, según la clasificación CIIU sección C o equivalente",
  },
  {
    name: "Pobreza por ingresos",
    survey: "Persona",
    description: "Mide la proporción de personas que viven en hogares cuyo ingreso per cápita se encuentra por debajo de la línea oficial de pobreza por ingresos.",
  },
  {
    name: "Pobreza extrema por ingresos",
    survey: "Persona",
    description: "Corresponde a la proporción de personas que viven en hogares cuyo ingreso per cápita se encuentra por debajo de la línea oficial de pobreza extrema por ingresos.",
  },
  {
    // Usa Persona + Vivienda (NBI)
    name: "Tasa de pobreza por necesidades básicas insatisfechas",
    survey: "Persona + Vivienda",
    description: "Mide la proporción de personas que pertenecen a un hogar que presenta carencias en la satisfacción de al menos una de sus necesidades básicas, definidas en cinco componentes: Calidad de la vivienda, Hacinamiento, Acceso a servicios básicos, Acceso a educación, Capacidad económica del hogar",
  },
  {
    // Usa Persona + Vivienda (MPI)
    name: "Tasa de pobreza multidimensional",
    survey: "Persona + Vivienda",
    description: "Mide el porcentaje de personas que se encuentran en situación de pobreza cuando se consideran simultáneamente múltiples dimensiones de bienestar (educación, trabajo y seguridad social, salud, vivienda, servicios básicos, entre otras)",
  },
  {
    // Usa Persona + Vivienda (MPI extrema)
    name: "Tasa de pobreza extrema multidimensional",
    survey: "Persona + Vivienda",
    description: "Mide el porcentaje de personas que presentan niveles muy altos de privación multidimensional, de acuerdo con un umbral de privación más exigente que el usado para pobreza multidimensional.",
  },
];

// ------------------------
// Latinobarómetro
// ------------------------

const latinobarometroIndicators = [
  {
    name: "Apoyo a la democracia",
    description: "Mide el porcentaje de personas que estan de acuerdo con la democracia como forma de gobierno princial.",
  },
  {
    name: "Indiferencia o apoyo a alternativas autoritarias",
    description: "Mide el procentaje de personas que les resulta indiferente y/o apoyarían a un gobierno autoritario.",
  },
  {
    name: "Satisfacción con la democracia",
    description: "Mide el porcentaje de personas que están satisfechas con la democracia.",
  },
  {
    name: "Ubicación ideológica izquierda-derecha",
    description: "Mide el procentaje de personas que apoyan a la izquierda ideológica y derecha ideológica.",
  },
  {
    name: "Evaluación de la situación económica del país",
    description: "Mide el porcentaje en cuanto a la percepción de la economía general del país.",
  },
  {
    name: "Evaluación de la situación económica personal",
    description: "Mide el porcentaje en cuanto a la percepción de la economía personal.",
  },
  {
    name: "Preocupación por perder el empleo",
    description: "Cuantifica la preocupación por perder el empleo en un futuro.",
  },
  {
    name: "Tenencia de bienes y servicios en el hogar",
    description: "Mide el procentaje de posesión de bienes personales como Autos, Lavadoras, Alcantarillado, Agua Caliente, etc.",
  },
  {
    name: "Confianza en instituciones",
    description: "Mide el porcentaje de confianza en diferentes instituciones como Gobierno, Partidos Políticos, Ejercito, Iglesia, etc.",
  },
];

// ------------------------
// V-Dem
// ------------------------

const vdemIndicators = [
  {
    name: "Índice de democracia electoral (v2x_polyarchy)",
    description: "Resume el grado en el que un país cumple con los principios de la “poliarquía” en el sentido de Dahl: elecciones libres y competitivas, sufragio amplio, libertad de expresión, libertad de asociación y acceso a fuentes alternativas de información.",
  },
  {
    name: "Índice de democracia liberal (v2x_libdem)",
    description: "Amplía el concepto de democracia electoral incorporando la limitación del poder ejecutivo mediante el estado de derecho, la independencia judicial y los controles legislativos y judiciales.",
  },
  {
    name: "Índice de democracia participativa (v2x_partipdem)",
    description: "Mide el grado en el que la ciudadanía participa en la vida política más allá del voto, incluyendo la fortaleza de la sociedad civil, la existencia de mecanismos de democracia directa y el involucramiento de organizaciones populares.",
  },
  {
    name: "Índice de democracia deliberativa (v2x_delibdem)",
    description: "Refleja hasta qué punto la toma de decisiones políticas está guiada por procesos de deliberación pública, argumentación razonada y consideración del bien común, en lugar de basarse en intereses particulares, coerción o intercambios clientelares",
  },
  {
    name: "Índice de democracia igualitaria (v2x_egaldem)",
    description: "Mide hasta qué punto los recursos políticos y las garantías democráticas se distribuyen de manera relativamente igualitaria entre diferentes grupos de la población (por ejemplo, grupos socioeconómicos, étnicos, territoriales y de género). Evalúa la dimensión igualitaria de la democracia.",
  },
  {
    name: "Libertad de expresión y fuentes alternativas de información (v2x_freexp_altinf)",
    description:
      "Sintetiza la medida en que los ciudadanos pueden expresar opiniones políticas sin temor, acceder a medios independientes y disponer de fuentes alternativas de información.",
  },
  {
    name: "Integridad de elecciones (índice de elecciones libres y justas, v2xel_frefair)",
    description:
      "Evalúa qué tan libres y justas son las elecciones, considerando aspectos como la ausencia de fraude, la competencia real entre opciones políticas, la imparcialidad de las autoridades electorales y el respeto a los resultados.",
  },
  {
    name: "Igualdad ante la ley y libertades individuales (v2xcl_rol)",
    description:
      "Mide la igualdad ante la ley y el respeto a las libertades civiles. Incluye dimensiones como la protección contra detenciones arbitrarias, el respeto al debido proceso, la libertad de movimiento y la ausencia de discriminación legal sistemática.",
  },
  {
    name: "Controles judiciales sobre el ejecutivo (v2x_jucon)",
    description: "Refleja el grado en que el poder judicial ejerce controles efectivos sobre el poder ejecutivo, incluyendo la independencia de jueces y tribunales, y la capacidad de revisar y limitar las decisiones del gobierno.",
  },
  {
    name: "Controles legislativos sobre el ejecutivo (v2xlg_legcon)",
    description: "Mide el grado en el que el poder legislativo puede supervisar, cuestionar y limitar al poder ejecutivo. Considera aspectos como la capacidad de investigar al gobierno, de destituir a autoridades y de modificar la agenda legislativa impulsada por el ejecutivo.",
  },
  {
    name: "Igual protección legal (v2xeg_eqprotec)",
    description: "Evalúa hasta qué punto todos los individuos reciben una protección legal similar, independientemente de su estatus socioeconómico, género, etnia, religión u otra característica. ",
  },
  {
    name: "Igual acceso a recursos públicos (v2xeg_eqaccess)",
    description: "Mide la igualdad en el acceso a servicios y recursos proporcionados por el Estado (por ejemplo, educación, salud, infraestructura), entre distintos grupos de la población. Captura si el Estado distribuye estos recursos de manera relativamente equitativa.",
  },
  {
    name: "Igual distribución de recursos (v2xeg_eqdr)",
    description: "Resume el grado en el que los recursos económicos y sociales se distribuyen de forma relativamente equitativa en la sociedad, más allá del acceso formal a servicios públicos.",
  },
  {
    name: "Distribución del poder por estatus socioeconómico (v2pepwrses)",
    description:
      "Mide en qué medida el poder político efectivo está concentrado en grupos de estatus socioeconómico alto (por ejemplo, élites económicas) o, por el contrario, distribuido de forma más equitativa entre clases sociales. ",
  },
  {
    name: "Distribución del poder por grupo social (v2pepwrsoc)",
    description: "Captura la medida en que el poder político está distribuido entre distintos grupos sociales (por ejemplo, étnicos o de casta), o concentrado en uno o pocos grupos dominantes.",
  },
  {
    name: "Distribución del poder por género (v2pepwrgen)",
    description: "Evalúa la distribución del poder político entre hombres y mujeres, incluyendo la presencia de mujeres en cargos electivos, posiciones de decisión y otros espacios de poder institucional.",
  },
  {
    name: "Distribución del poder por orientación religiosa (v2pepwrort)",
    description:
      "Mide hasta qué punto el poder político está sesgado hacia determinados grupos religiosos o si, por el contrario, se encuentra distribuido de forma más equitativa entre distintas orientaciones religiosas.",
  },
  {
    name: "Distribución del poder por región geográfica (v2pepwrgeo)",
    description:
      "Refleja en qué medida el poder político está concentrado en ciertas regiones del país (por ejemplo, capitales o zonas urbanas) o si existe una distribución más equilibrada entre las distintas regiones geográficas.",
  },
];

// ------------------------
// indicatorsTable final
// ------------------------

const indicatorsTable = [
  // ENEMDU
  ...enemduIndicators.map(({ name, survey, description }) => ({
    source: "ENEMDU",
    survey,
    name,
    description,
    geo: { nat: true, prov: true, cant: true, parr: true },
    temp: { annual: true, monthly: true },
    period: { from: "2007", to: "2025" },
    methodology: {
      label: `Ficha metodológica ENEMDU`,
      url: "https://www.ecuadorencifras.gob.ec/documentos/web-inec/EMPLEO/2018/Septiembre-2018/ENEMDU_Metodologia%20Encuesta%20Nacional%20de%20Empleo%20Desempleo%20y%20Subempleo.pdf",
    },
  })),

  // Latinobarómetro
  ...latinobarometroIndicators.map(({ name, description }) => ({
    source: "Latinobarómetro",
    name,
    description,
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1995", to: "2024" },
    methodology: {
      label: "Documentación y fichas técnicas de Latinobarómetro",
      url: "https://www.latinobarometro.org/documentacion-datos",
    },
  })),

  // V-Dem
  ...vdemIndicators.map(({ name, description }) => ({
    source: "V-Dem",
    name,
    description,
    geo: { nat: true, prov: false, cant: false, parr: false },
    temp: { annual: true, monthly: false },
    period: { from: "1789", to: "2024" },
    methodology: {
      label: "Metodología general de V-Dem",
      url: "https://v-dem.net/documents/56/methodology.pdf",
    },
  })),
];


const BasesUsadasPage = () => {
  // const yes = "✓";
  // const no = "—";

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
              <col className="col-description" />
              <col className="col-small" span="8" />
              <col className="col-methodology" />
            </colgroup>

            <thead>
              <tr>
                <th rowSpan={2}>Fuente</th>
                <th rowSpan={2}>Indicador</th>
                <th rowSpan={2}>Descripción</th>
                <th colSpan={4}>Desagregación geográfica</th>
                <th colSpan={2}>Desagregación temporal</th>
                <th colSpan={2}>Periodo</th>
                <th rowSpan={2}>Ficha metodológica</th>
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
                  <td>
                    {ind.source}
                    {ind.survey ? ` - ${ind.survey}` : ""}
                  </td>
                  <td>{ind.name}</td>
                  <td>{ind.description}</td>
                  <td>{ind.geo.nat ? "✓" : "—"}</td>
                  <td>{ind.geo.prov ? "✓" : "—"}</td>
                  <td>{ind.geo.cant ? "✓" : "—"}</td>
                  <td>{ind.geo.parr ? "✓" : "—"}</td>
                  <td>{ind.temp.annual ? "✓" : "—"}</td>
                  <td>{ind.temp.monthly ? "✓" : "—"}</td>
                  <td>{ind.period.from}</td>
                  <td>{ind.period.to}</td>
                  <td>
                    {ind.methodology ? (
                      <a
                        href={ind.methodology.url}
                        target="_blank"
                        rel="noopener noreferrer"
                      >
                        {ind.methodology.label}
                      </a>
                    ) : (
                      "—"
                    )}
                  </td>

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