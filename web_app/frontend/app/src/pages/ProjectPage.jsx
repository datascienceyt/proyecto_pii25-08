// src/pages/ProjectPage.jsx
import React from "react";

const teamMembers = [
  { name: "Erick Eduardo Cuenca Pauta", role: "Director" },
  { name: "Silvana Karina Escobar Córdova", role: "Codirectora" },
  { name: "María Gabriela Cajamarca Morquecho", role: "Profesora" },
  { name: "Tito Rolando Armas Andrade", role: "Profesor" },
  { name: "Alexandra Colaborador Jima González", role: "Colaboradora externa" },
  { name: "José Ángel Alcántara Lizárraga", role: "Colaborador externo" },
  { name: "Joseline Milagros García Paredes", role: "Estudiante de Pregrado" },
];

const ProjectPage = () => {
  return (
    <div className="page project-page">
      {/* HERO PRINCIPAL */}
      <section className="project-hero">
        <div className="project-hero-content">
          <p className="project-tag">
            Proyecto de democracia en Latinoamérica
          </p>
          <h1 className="project-title">
            Efectos de la desigualdad socioeconómica en la percepción de la
            democracia en Latinoamérica
          </h1>
          <p className="project-hero-text">
            El proyecto analiza cómo las brechas de ingreso, acceso a servicios
            y oportunidades se reflejan en el apoyo, la satisfacción y la
            confianza en la democracia en 19 países de la región entre 1995 y
            2023.
          </p>
          <div className="project-meta-row">
            <span className="project-meta-pill">1995 – 2023</span>
            <span className="project-meta-pill">19 países</span>
            <span className="project-meta-pill">V-Dem · Latinobarómetro · ENEMDU</span>
          </div>
        </div>

        <div className="project-hero-graphic">
          <div className="project-hero-circle project-hero-circle--primary" />
          <div className="project-hero-circle project-hero-circle--secondary" />
          <div className="project-hero-bars">
            <span />
            <span />
            <span />
            <span />
          </div>
          <p className="project-hero-quote">
            “Sin igualdad no hay una democracia plena; solo una promesa
            incompleta.”
          </p>
        </div>
      </section>

      {/* SOBRE EL PROYECTO */}
      <section className="project-section">
        <div className="project-section-header">
          <h2 className="project-section-title">Sobre el proyecto</h2>
          <p className="project-section-text">
            Este estudio integra múltiples fuentes de datos para construir
            indicadores comparables de desigualdad socioeconómica y percepción
            democrática. El análisis combina información de V-Dem, ENEMDU y
            Latinobarómetro para responder preguntas sobre apoyo a la
            democracia, confianza institucional y bienestar subjetivo.
          </p>
        </div>

        <div className="project-highlights">
          <div className="project-highlight-card">
            <h3>Preguntas clave</h3>
            <ul>
              <li>
                ¿Cómo se relaciona la desigualdad con el apoyo a la democracia?
              </li>
              <li>
                ¿Qué grupos sociales perciben con mayor fuerza el deterioro
                institucional?
              </li>
              <li>
                ¿Qué trayectorias siguen los países de la región a lo largo del
                tiempo?
              </li>
            </ul>
          </div>
          <div className="project-highlight-card">
            <h3>Enfoque metodológico</h3>
            <ul>
              <li>Integración de bases de datos internacionales y nacionales.</li>
              <li>Construcción de indicadores comparables en el tiempo.</li>
              <li>Visualización interactiva de resultados mediante dashboards.</li>
            </ul>
          </div>
        </div>
      </section>

      {/* OBJETIVOS */}
      <section className="project-section project-section-alt">
        <div className="project-section-header">
          <h2 className="project-section-title">Objetivos del proyecto</h2>
          <p className="project-section-text">
            Los siguientes objetivos pueden ajustarse a la redacción definitiva
            del proyecto. La estructura está pensada para resaltar cada objetivo
            como una tarjeta clara y legible.
          </p>
        </div>

        <div className="project-objectives-grid">
          <article className="project-objective-card">
            <span className="project-badge">01</span>
            <h3>Medir la desigualdad y la calidad democrática</h3>
            <p>
              Caracterizar la evolución de la desigualdad socioeconómica y de
              los indicadores de calidad democrática en los países analizados.
            </p>
          </article>
          <article className="project-objective-card">
            <span className="project-badge">02</span>
            <h3>Vincular desigualdad y percepción ciudadana</h3>
            <p>
              Analizar cómo las condiciones materiales y las brechas de acceso
              se reflejan en el apoyo, la satisfacción y la confianza en la
              democracia.
            </p>
          </article>
          <article className="project-objective-card">
            <span className="project-badge">03</span>
            <h3>Generar herramientas para la toma de decisiones</h3>
            <p>
              Producir indicadores y visualizaciones que faciliten el diseño de
              políticas públicas orientadas a fortalecer la democracia y reducir
              las desigualdades.
            </p>
          </article>
        </div>
      </section>

      {/* EQUIPO */}
      <section className="project-section">
        <div className="project-section-header">
          <h2 className="project-section-title">Equipo de trabajo</h2>
          <p className="project-section-text">
            El proyecto reúne a docentes, investigadores y estudiantes con experiencia en 
            ciencia política, economía, estadística y análisis de datos.
          </p>
        </div>

        <div className="team-grid">
          {teamMembers.map((member) => (
            <article key={member.name} className="team-card">
              <div className="team-avatar">
                <span>{member.name.charAt(0)}</span>
              </div>
              <div className="team-info">
                <h3 className="team-name">{member.name}</h3>
                <p className="team-role">{member.role}</p>
              </div>
            </article>
          ))}
        </div>
      </section>
    </div>
  );
};

export default ProjectPage;
