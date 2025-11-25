// src/pages/PublicationsPage.jsx
import React from "react";

const scientificArticles = [
  {
    title: "Desigualdad y apoyo a la democracia en América Latina",
    authors: "Autor/a 1, Autor/a 2",
    year: "2024",
    outlet: "Revista X de Ciencia Política",
    href: "#", // TODO: replace with DOI or PDF
  },
  {
    title: "Trayectorias democráticas y brechas socioeconómicas",
    authors: "Autor/a 3, Autor/a 4",
    year: "2023",
    outlet: "Revista Y de Estudios Latinoamericanos",
    href: "#",
  },
];

const technicalReports = [
  {
    title: "Informe regional de indicadores de democracia y desigualdad",
    description:
      "Síntesis de resultados para los 19 países analizados, con énfasis en tendencias temporales.",
    year: "2024",
    href: "#",
  },
  {
    title: "Informe país: Ecuador",
    description:
      "Análisis detallado de los resultados para Ecuador, integrando ENEMDU con V-Dem y Latinobarómetro.",
    year: "2024",
    href: "#",
  },
];

const otherOutputs = [
  {
    title: "Presentación en congreso internacional",
    description:
      "Resultados preliminares presentados en el Congreso XYZ de Ciencia Política.",
    href: "#",
  },
  {
    title: "Poster académico",
    description:
      "Visualización sintética de indicadores clave para difusión académica.",
    href: "#",
  },
];

const PublicationsPage = () => {
  return (
    <div className="page publications-page">
      {/* HERO */}
      <section className="publications-hero">
        <div className="publications-hero-content">
          <p className="project-tag">Publicaciones</p>
          <h1 className="project-title">
            Resultados y productos académicos del proyecto
          </h1>
          <p className="project-hero-text">
            Esta sección recopila artículos científicos, informes técnicos y otros
            productos derivados del proyecto.
          </p>
        </div>

        <div className="publications-hero-box">
          <h3>Líneas de difusión</h3>

          <div className="publications-hero-highlights">
            <article className="publications-hero-highlight">
              <div className="publications-hero-highlight-icon publications-hero-highlight-icon--journals">
                <span role="img" aria-label="Revistas científicas">
                  📄
                </span>
              </div>
              <div className="publications-hero-highlight-text">
                <h4>Artículos científicos</h4>
                <p>
                  Manuscritos enviados o publicados en revistas indexadas en temas de
                  democracia, desigualdad y opinión pública.
                </p>
              </div>
            </article>

            <article className="publications-hero-highlight">
              <div className="publications-hero-highlight-icon publications-hero-highlight-icon--reports">
                <span role="img" aria-label="Informes técnicos">
                  📑
                </span>
              </div>
              <div className="publications-hero-highlight-text">
                <h4>Informes técnicos</h4>
                <p>
                  Documentos dirigidos a instituciones y tomadores de decisiones, con
                  énfasis en hallazgos aplicados.
                </p>
              </div>
            </article>

            <article className="publications-hero-highlight">
              <div className="publications-hero-highlight-icon publications-hero-highlight-icon--talks">
                <span role="img" aria-label="Presentaciones">
                  🎤
                </span>
              </div>
              <div className="publications-hero-highlight-text">
                <h4>Presentaciones y ponencias</h4>
                <p>
                  Participación en congresos, seminarios y espacios académicos donde
                  se discuten los resultados del proyecto.
                </p>
              </div>
            </article>
          </div>
        </div>
      </section>


      {/* ARTÍCULOS CIENTÍFICOS */}
      <section className="publications-section">
        <div className="project-section-header">
          <h2 className="project-section-title">Artículos científicos</h2>
          <p className="project-section-text">
            Artículos sometidos o publicados y enlace al texto completo o al DOI.
          </p>
        </div>

        <div className="publications-grid">
          {scientificArticles.map((art) => (
            <article key={art.title} className="publication-card">
              <p className="publication-year">{art.year}</p>
              <h3>{art.title}</h3>
              <p className="publication-authors">{art.authors}</p>
              <p className="publication-outlet">{art.outlet}</p>
              {art.href && art.href !== "#" && (
                <a
                  href={art.href}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="methodology-doc-link"
                >
                  Ver artículo
                </a>
              )}
            </article>
          ))}
        </div>
      </section>

      {/* INFORMES TÉCNICOS */}
      <section className="publications-section publications-section-alt">
        <div className="project-section-header">
          <h2 className="project-section-title">Informes técnicos</h2>
          <p className="project-section-text">
            Informes orientados a la síntesis de resultados para tomadores de
            decisiones, instituciones académicas y público general.
          </p>
        </div>

        <div className="publications-grid">
          {technicalReports.map((rep) => (
            <article key={rep.title} className="publication-card">
              <p className="publication-year">{rep.year}</p>
              <h3>{rep.title}</h3>
              <p>{rep.description}</p>
              {rep.href && rep.href !== "#" && (
                <a
                  href={rep.href}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="methodology-doc-link"
                >
                  Ver informe
                </a>
              )}
            </article>
          ))}
        </div>
      </section>

      {/* OTROS PRODUCTOS */}
      <section className="publications-section">
        <div className="project-section-header">
          <h2 className="project-section-title">Otros productos</h2>
          <p className="project-section-text">
            Presentaciones, posters, capítulos de libro y otros materiales de
            difusión asociados al proyecto.
          </p>
        </div>

        <div className="publications-grid">
          {otherOutputs.map((out) => (
            <article key={out.title} className="publication-card">
              <h3>{out.title}</h3>
              <p>{out.description}</p>
              {out.href && out.href !== "#" && (
                <a
                  href={out.href}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="methodology-doc-link"
                >
                  Ver material
                </a>
              )}
            </article>
          ))}
        </div>
      </section>
    </div>
  );
};

export default PublicationsPage;
