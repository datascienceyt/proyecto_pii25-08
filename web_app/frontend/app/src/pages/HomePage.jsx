// src/pages/HomePage.jsx
import React from "react";
import { Link } from "react-router-dom";
import homeBg from "../assets/home-hero.jpg";

const HomePage = () => {
  return (
    <div className="home-page">
      <section
        className="home-hero"
        style={{ backgroundImage: `url(${homeBg})` }}
      >
        <div className="home-hero-overlay" />

        <div className="home-hero-content">
          <p className="home-tagline">
            Proyecto de democracia en Latinoamérica
          </p>

          <h1 className="home-title">
            Efectos de la desigualdad socioeconómica en la percepción
            de la democracia en Latinoamérica (1995–2023)
          </h1>

          <p className="home-subtitle">
            Un estudio comparativo basado en V-Dem, Latinobarómetro y ENEMDU
            para entender cómo la desigualdad condiciona la calidad y la
            percepción de la democracia en la región.
          </p>

          <div className="home-cta-group">
            <Link to="/sobre-el-proyecto" className="home-cta home-cta-primary">
              Sobre el Proyecto
            </Link>
            <Link to="/indicadores" className="home-cta home-cta-secondary">
              Ver Indicadores
            </Link>
          </div>
        </div>
      </section>
    </div>
  );
};

export default HomePage;
