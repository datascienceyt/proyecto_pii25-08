// src/pages/MethodologyPage.jsx
import React from "react";
import { Link } from "react-router-dom"; 

const methodologyDocs = [
  // {
  //   title: "Bases del Proyecto",
  //   description:
  //     "Descripción completa del diseño del estudio, supuestos, alcances y limitaciones.",
  //   href: "/docs/metodologia_general.pdf",
  // },
  {
    title: "Ficha técnica V-Dem",
    description:
      "Descripción del proceso de selección de variables, reescalamiento de índices (-4 a 4 a 0–1) y construcción de la base de indicadores país–año a partir de V-Dem.",
    href: "/docs/Ficha_Metodologica_Vdem.pdf",
  },
  {
    title: "Ficha técnica Latinobarómetro",
    description:
      "Explica la integración de las encuestas anuales, normalización de nombres de variables, criterios de válidos y cálculo de indicadores agregados por país, región y ciudad.",
    href: "/docs/Ficha_Metodologica_Latinobarometro.pdf",
  },
  {
    title: "Ficha técnica ENEMDU",
    description:
      "Documenta la descarga, limpieza y homologación de códigos geográficos, así como la construcción de indicadores laborales, de pobreza por ingresos, IPM y NBI con desagregaciones territoriales.",
    href: "/docs/Ficha_Metodologica_ENEMDU.pdf",
  },
];

const MethodologyPage = () => {
  return (
    <div className="page methodology-page">
      {/* HERO */}
      <section className="methodology-hero">
        <div className="methodology-hero-content">
          <p className="project-tag">Metodología</p>
          <h1 className="project-title">Cómo se construyeron los indicadores</h1>
          <p className="project-hero-text">
            Esta sección documenta el proceso de integración de datos, normalización
            y cálculo de los indicadores que alimentan los dashboards del proyecto.
            El objetivo es que cualquier persona pueda comprender cómo se obtienen
            los resultados y replicar los cálculos.
          </p>
        </div>

        <div className="methodology-hero-box">
          <h3>En resumen</h3>

          <div className="methodology-hero-highlights">
            <article className="methodology-hero-highlight">
              <div className="methodology-hero-highlight-icon methodology-hero-highlight-icon--sources">
                <span role="img" aria-label="Integración de datos">
                  🧩
                </span>
              </div>
              <div className="methodology-hero-highlight-text">
                <h4>Integración de fuentes</h4>
                <p>
                  Unificación de V-Dem, Latinobarómetro y ENEMDU en una estructura
                  común de país–año.
                </p>
              </div>
            </article>

            <article className="methodology-hero-highlight">
              <div className="methodology-hero-highlight-icon methodology-hero-highlight-icon--scaling">
                <span role="img" aria-label="Escalamiento">
                  📊
                </span>
              </div>
              <div className="methodology-hero-highlight-text">
                <h4>Escalas comparables</h4>
                <p>
                  Normalización de indicadores en una escala 0–100 para facilitar la
                  comparación entre países y años.
                </p>
              </div>
            </article>

            <article className="methodology-hero-highlight">
              <div className="methodology-hero-highlight-icon methodology-hero-highlight-icon--series">
                <span role="img" aria-label="Series de tiempo">
                  🌎
                </span>
              </div>
              <div className="methodology-hero-highlight-text">
                <h4>Series temporales</h4>
                <p>
                  Construcción de series consistentes para 19 países entre 1995 y
                  2023, listas para análisis comparativo.
                </p>
              </div>
            </article>
          </div>
        </div>
      </section>


      {/* FLUJO GENERAL DE CÁLCULO */}
      <section className="methodology-section methodology-section-alt">
        <div className="project-section-header">
          <h2 className="project-section-title">
            Flujo general de cálculo de indicadores
          </h2>
          <p className="project-section-text">
            El proceso metodológico se puede resumir en las siguientes etapas.
            Cada una de ellas se detalla en los documentos técnicos disponibles
            para descarga.
          </p>
        </div>

        <div className="methodology-steps">
          <article className="methodology-step">
            <span className="methodology-step-number">1</span>
            <h3>Selección y depuración de variables</h3>
            <p>
              Selección de variables relevantes en V-Dem, Latinobarómetro y
              ENEMDU. Se aplican filtros de calidad, control de valores atípicos
              y unificación de codificaciones para países y años.
            </p>
          </article>
          <article className="methodology-step">
            <span className="methodology-step-number">2</span>
            <h3>Normalización y construcción de indicadores</h3>
            <p>
              Transformación de variables originales a escalas comparables,
              aplicación de ponderaciones (cuando corresponde) y cálculo de
              índices sintéticos a nivel de país y año.
            </p>
          </article>
          <article className="methodology-step">
            <span className="methodology-step-number">3</span>
            <h3>Validación y consistencia temporal</h3>
            <p>
              Verificación de la estabilidad de las series, comparación con
              fuentes oficiales y ajuste de posibles rupturas de serie o cambios
              metodológicos en las encuestas de origen.
            </p>
          </article>
        </div>
      </section>

      {/* METODOLOGÍA POR BASE DE DATOS */}
      <section className="methodology-section">
        <div className="project-section-header">
          <h2 className="project-section-title">
            Metodología por base de datos
          </h2>
          <p className="project-section-text">
            Cada fuente de información requiere decisiones específicas en
            términos de selección de variables, escalas y tratamiento de datos
            faltantes. A continuación se resume el enfoque utilizado para cada
            base.
          </p>
        </div>

        <div className="methodology-grid">
          <article className="methodology-card">
            <h3>V-Dem (Varieties of Democracy)</h3>
            <p>
              A partir de V-Dem se utilizan principalmente los índices de
              democracia electoral, liberal, participativa, deliberativa e
              igualitaria, además de indicadores complementarios sobre igualdad
              ante la ley, restricciones al ejecutivo y elecciones limpias.
            </p>
            <ul>
              <li>Escala original 0–1, interpretada como 0–100%.</li>
              <li>Promedios anuales por país sin ponderación adicional.</li>
              <li>
                Documentación detallada disponible en la ficha técnica V-Dem.
              </li>
            </ul>
          </article>

          <article className="methodology-card">
            <h3>Latinobarómetro</h3>
            <p>
              Se construyen tasas e índices agregados a partir de microdatos
              individuales: apoyo a la democracia, apoyo al autoritarismo,
              satisfacción con la democracia, autoubicación ideológica y
              confianza en instituciones.
            </p>
            <ul>
              <li>Uso de factores de expansión muestral provistos por el estudio.</li>
              <li>Cálculo de proporciones y medias por país y año.</li>
              <li>
                Agrupación de categorías de respuesta para facilitar la
                comparación entre países.
              </li>
            </ul>
          </article>

          <article className="methodology-card">
            <h3>ENEMDU (Ecuador)</h3>
            <p>
              Para Ecuador se emplean los microdatos de ENEMDU para construir
              indicadores de desigualdad, condiciones de vida y percepción
              económica, comparables con los indicadores regionales.
            </p>
            <ul>
              <li>
                Uso de ponderadores muestrales y diseño estratificado de la
                encuesta.
              </li>
              <li>Construcción de tasas y promedios por año.</li>
              <li>
                Comparación directa con indicadores de Latinobarómetro y V-Dem
                cuando es metodológicamente posible.
              </li>
            </ul>
            <div className="methodology-validation-callout">
              <p>
                Para ENEMDU se realizó, además, una{" "}
                <strong>validación comparativa</strong> con los indicadores
                oficiales publicados por el INEC.
              </p>
              <Link to="/validacion" className="methodology-validation-link">
                Ver validación de indicadores ENEMDU / INEC
              </Link>
            </div>
          </article>
        </div>
      </section>

      {/* DOCUMENTOS Y DESCARGAS */}
      <section className="methodology-section methodology-downloads">
        <div className="project-section-header">
          <h2 className="project-section-title">Documentos metodológicos</h2>
          <p className="project-section-text">
            Los documentos siguientes contienen información detallada sobre
            definiciones, fórmulas y procedimientos.
          </p>
        </div>

        <div className="methodology-docs-grid">
          {methodologyDocs.map((doc) => (
            <article key={doc.title} className="methodology-doc-card">
              <h3>{doc.title}</h3>
              <p>{doc.description}</p>
              <a
                href={doc.href}
                target="_blank"
                rel="noopener noreferrer"
                className="methodology-doc-link"
              >
                Ver documento
              </a>
            </article>
          ))}
        </div>
      </section>
    </div>
  );
};

export default MethodologyPage;
