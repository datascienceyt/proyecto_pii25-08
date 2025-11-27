// src/pages/BasesUsadasPage.jsx
import React from "react";

// const basesDocs = [
//   {
//     base: "V-Dem",
//     title: "Sitio Oficial - V-Dem",
//     description: "Contiene información sobre definiciones, escalas y fuentes.",
//     href: "https://www.v-dem.net/",
//   },
//   {
//     base: "Latinobarómetro",
//     title: "Sitio Oficial - Latinobarómetro",
//     description: "Contiene información sobre diseño muestral, ponderadores y series históricas.",
//     href: "https://www.latinobarometro.org/#",
//   },
//   {
//     base: "ENEMDU",
//     title: "Sitio Oficial - ENEMDU",
//     description: "Contiene información sobre el diseño de la encuesta, ponderación y manual de variables.",
//     href: "https://www.ecuadorencifras.gob.ec/enemdu-anual/",
//   },
// ];

const BasesUsadasPage = () => {
  return (
    <div className="page bases-page">
      {/* HERO */}
      <section className="bases-hero">
        <div className="bases-hero-content">
          <p className="project-tag">Bases de datos</p>
          <h1 className="project-title">Fuentes de información utilizadas</h1>
          <p className="project-hero-text">
            El proyecto combina información de tres fuentes principales: V-Dem,
            Latinobarómetro y ENEMDU (Ecuador). Cada una aporta una dimensión distinta
            para comprender la relación entre desigualdad y democracia en
            Latinoamérica.
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
          <h2 className="project-section-title">
            Panorama de las bases de datos
          </h2>
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
            <p></p>
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
            <p></p>
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
            <p></p>
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

      {/* DOCUMENTOS / ENLACES */}
      {/* <section className="bases-section bases-downloads">
        <div className="project-section-header">
          <h2 className="project-section-title">
            Documentación y enlaces de referencia
          </h2>
          <p className="project-section-text">
            Aquí puedes enlazar documentación oficial, fichas técnicas,
            cuestionarios y otros recursos útiles para profundizar en cada base
            de datos.
          </p>
        </div>

        <div className="bases-docs-grid">
          {basesDocs.map((doc) => (
            <article key={doc.title} className="bases-doc-card">
              <p className="bases-doc-base">{doc.base}</p>
              <h3>{doc.title}</h3>
              <p>{doc.description}</p>
              <a
                href={doc.href}
                target="_blank"
                rel="noopener noreferrer"
                className="methodology-doc-link"
              >
                Visitar Sitio
              </a>
            </article>
          ))}
        </div>
      </section> */}
    </div>
  );
};

export default BasesUsadasPage;
