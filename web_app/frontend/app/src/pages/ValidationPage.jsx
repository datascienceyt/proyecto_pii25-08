// src/pages/ValidationPage.jsx
import React from "react";

const VALIDATION_HTML_URL =
  process.env.PUBLIC_URL + "/validacion/indicadores_inec_altair_styled.html";

const ValidationPage = () => {
  return (
    <div className="page validation-page">
      {/* HERO */}
      <section className="validation-hero">
        <div className="validation-hero-content">
          <p className="project-tag">Validación INEC</p>
          <h1 className="project-title">
            Validación de indicadores ENEMDU / INEC
          </h1>
          <p className="project-hero-text">
            En esta sección se comparan los indicadores oficiales publicados por
            el INEC a partir de ENEMDU con los indicadores generados en el
            proyecto. El objetivo es verificar la consistencia de los cálculos y
            documentar posibles diferencias.
          </p>
        </div>

        <div className="validation-hero-box">
          <h3>Qué muestra el gráfico</h3>
          <ul>
            <li>
              Una <strong>serie de tiempo</strong> con la evolución del indicador
              seleccionado, medida en porcentaje.
            </li>
            <li>
              Dos líneas comparativas: la serie <strong>INEC</strong> (cálculos
              oficiales) y la serie <strong>Proyecto</strong> (cálculos
              reproducidos a partir de ENEMDU).
            </li>
            <li>
              Un panel de control a la derecha con filtros para cambiar el{" "}
              <strong>nivel geográfico</strong> y el{" "}
              <strong>tipo de indicador</strong>.
            </li>
          </ul>
        </div>
      </section>

      {/* CONTENIDO PRINCIPAL */}
      <section className="validation-section">
        <h2 className="project-section-title">Comparación gráfica</h2>
        <p className="project-section-text">
          El gráfico muestra, para cada período disponible, el valor del
          indicador según las estimaciones del INEC y las estimaciones
          realizadas en este proyecto. Cuando ambas líneas siguen trayectorias
          similares y los niveles son cercanos, se considera que la metodología
          del proyecto reproduce adecuadamente los resultados oficiales.
        </p>

        <div className="validation-details-grid">
          <article className="validation-details-card">
            <h3>Cómo usar el visualizador</h3>
            <ul>
              <li>
                En el panel derecho puedes elegir el{" "}
                <strong>nivel geográfico</strong> (por ejemplo, Nacional o
                ciudad) y el <strong>indicador</strong> que deseas analizar
                (empleo, subempleo, etc.).
              </li>
              <li>
                Puedes <strong>acercarte o alejarte</strong> en el tiempo usando
                la rueda del ratón o el gesto de zoom del trackpad sobre el
                gráfico.
              </li>
              <li>
                También es posible <strong>hacer zoom por selección</strong>:
                arrastra el cursor sobre un tramo del eje horizontal para
                enfocarte en un rango de años específico.
              </li>
              <li>
                Al colocar el cursor sobre cualquier punto de la serie aparecerá
                un <strong>tooltip</strong> con el valor exacto del indicador en
                ese año para cada serie (INEC y Proyecto).
              </li>
            </ul>
          </article>

          <article className="validation-details-card">
            <h3>Alcances y limitaciones</h3>
            <ul>
              <li>
                El visualizador oficial del INEC utilizado como referencia{" "}
                <strong>sólo publica series para las cinco ciudades auto-representadas</strong> y para
                el ámbito nacional. No dispone de desagregaciones a nivel
                provincial o cantonal.
              </li>
              <li>
                En el proyecto, en cambio, los indicadores se han calculado
                también a niveles <strong>provincial y cantonal</strong>, pero
                esas desagregaciones no pueden compararse directamente con el
                visualizador del INEC porque no están disponibles de forma
                pública.
              </li>
              <li>
                Algunas diferencias puntuales entre las dos series pueden
                reflejar cambios en los <strong>diseños muestrales</strong>,
                actualizaciones de factores de expansión o pequeñas variaciones
                en la definición de las variables originales.
              </li>
              <li>
                Todas las comparaciones se basan en los{" "}
                <strong>microdatos de ENEMDU</strong>. Cuando las diferencias son
                grandes y sistemáticas, se marcan como casos que requieren
                revisión metodológica adicional.
              </li>
            </ul>
          </article>
        </div>

        <div className="visualization-embed-wrapper validation-visualization-wrapper">
          <iframe
            src={VALIDATION_HTML_URL}
            title="Validación ENEMDU"
            className="visualization-iframe"
          />
        </div>
      </section>
    </div>
  );
};

export default ValidationPage;
