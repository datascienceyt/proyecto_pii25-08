// src/pages/IndicatorsPage.jsx
import React, { useState, useMemo } from "react";
import SupersetDashboard from "../components/SupersetDashboard";

// ===== CONFIGURACIÓN DE DASHBOARDS =====

// 1) Dashboard general (único)
const GENERAL_DASHBOARD = {
  key: "general-overview",
  label: "Visión general de indicadores",
  supersetId: "60141dee-b2b0-44e6-b9cd-9f4d37bd4164",
};

// 2) Dashboards comparativos por base
const BASES_DASHBOARDS = [
  {
    key: "base-vdem",
    label: "VDEM",
    description: "Indicadores comparativos construidos a partir de la base VDEM.",
    supersetId: "01a76746-6cb1-4f80-ada7-0960d03eefc6",
  },
  {
    key: "base-latinobarometro",
    label: "Latinobarómetro",
    description:
      "Indicadores comparativos construidos a partir de la base Latinobarómetro.",
    supersetId: "2e8e24c5-148e-46dc-8dec-2c3046a5a81e",
  },
  {
    key: "base-enemdu",
    label: "ENEMDU",
    description: "Indicadores comparativos construidos a partir de la base ENEMDU.",
    supersetId: "04a0ed97-8f80-427c-9a99-ee35d9711c57",
  },
];

const IndicatorsPage = () => {
  // "general" | "bases"
  const [mode, setMode] = useState("general");
  const [selectedBaseKey, setSelectedBaseKey] = useState(
    BASES_DASHBOARDS[0]?.key || null
  );

  // Dashboard actual según lo seleccionado
  const currentDashboardId = useMemo(() => {
    if (mode === "general") {
      return GENERAL_DASHBOARD.supersetId;
    }
    if (mode === "bases" && selectedBaseKey) {
      const base = BASES_DASHBOARDS.find((b) => b.key === selectedBaseKey);
      return base?.supersetId || null;
    }
    return null;
  }, [mode, selectedBaseKey]);

  return (
    <div className="page indicators-page">
      {/* HERO / INTRO */}
      <section className="indicators-hero">
        <div className="indicators-hero-text">
          <p className="project-tag">Exploración interactiva</p>
          <h1 className="project-title">Indicadores del proyecto</h1>
          <p className="project-hero-text">
            En esta sección puedes explorar los indicadores construidos a partir
            de las distintas bases de datos. El modo{" "}
            <strong>General</strong> muestra una visión panorámica, mientras que{" "}
            <strong>Por bases</strong> permite profundizar en VDEM,
            Latinobarómetro y ENEMDU por separado.
          </p>
        </div>
        <div className="indicators-hero-box">
          <h3>Cómo navegar</h3>
          <ul>
            <li>
              Usa el menú lateral para alternar entre la vista general y las
              bases.
            </li>
            <li>
              En <strong>Por bases</strong>, selecciona la fuente que deseas
              analizar mediante las chips superiores.
            </li>
            <li>
              Los dashboards son interactivos: puedes filtrar, resaltar series y
              descargar gráficos según los permisos configurados.
            </li>
          </ul>
        </div>
      </section>

      <div className="indicators-layout">
        {/* Menú lateral */}
        <aside className="indicators-sidebar">
          <h3>INDICADORES</h3>

          <button
            className={
              mode === "general"
                ? "indicator-tab indicator-tab-active"
                : "indicator-tab"
            }
            onClick={() => setMode("general")}
          >
            GENERAL
          </button>

          <button
            className={
              mode === "bases"
                ? "indicator-tab indicator-tab-active"
                : "indicator-tab"
            }
            onClick={() => setMode("bases")}
          >
            POR BASES
          </button>
        </aside>

        {/* Contenido principal */}
        <section className="indicators-content">
          {mode === "general" ? (
            <>
              <h2 className="indicators-section-title">Indicadores generales</h2>
              <p className="indicators-section-text">
                El dashboard general resume la evolución de los indicadores
                clave de democracia y desigualdad para el conjunto de países y
                periodos analizados.
              </p>
            </>
          ) : (
            <>
              <h2 className="indicators-section-title">
                Indicadores comparativos por base
              </h2>
              <p className="indicators-section-text">
                Selecciona una base de datos para visualizar el dashboard
                comparativo construido a partir de sus indicadores.
              </p>

              <div className="indicator-chips">
                {BASES_DASHBOARDS.map((base) => (
                  <button
                    key={base.key}
                    className={
                      selectedBaseKey === base.key ? "chip chip-active" : "chip"
                    }
                    onClick={() => setSelectedBaseKey(base.key)}
                  >
                    {base.label}
                  </button>
                ))}
              </div>

              {/* Descripción breve de la base seleccionada */}
              {mode === "bases" && selectedBaseKey && (
                <div className="indicators-base-description">
                  {
                    BASES_DASHBOARDS.find((b) => b.key === selectedBaseKey)
                      ?.description
                  }
                </div>
              )}
            </>
          )}
        </section>
      </div>

      {/* Panel de dashboard embebido (full width) */}
      <div className="visualization-embed-wrapper indicators-visualization-wrapper">
        {currentDashboardId ? (
          <SupersetDashboard dashboardId={currentDashboardId} />
        ) : (
          <div className="indicators-empty">
            {mode === "general"
              ? "Configura el UUID del dashboard general para visualizarlo aquí."
              : "Selecciona una base para cargar el dashboard de Superset."}
          </div>
        )}
      </div>
    </div>
  );
};

export default IndicatorsPage;
