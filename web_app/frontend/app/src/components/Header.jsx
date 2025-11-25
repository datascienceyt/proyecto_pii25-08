// src/components/Header.jsx
import React from "react";
import { Link, useLocation } from "react-router-dom";
import logo from "../assets/yachay_white.png";

// Top bar links (Sobre, Metodología, Bases, Publicaciones)
const TopNavLink = ({ to, children }) => {
  const location = useLocation();
  const active = location.pathname === to;
  const className =
    "top-nav-link" + (active ? " top-nav-link--active" : "");

  return (
    <Link to={to} className={className}>
      {children}
    </Link>
  );
};

// Bottom bar links (Indicadores, Validación)
const SecondaryNavLink = ({ to, children }) => {
  const location = useLocation();
  const active = location.pathname === to;
  const className =
    "secondary-nav-link" +
    (active ? " secondary-nav-link--active" : "");

  return (
    <Link to={to} className={className}>
      {children}
    </Link>
  );
};

const Header = () => {
  return (
    <header className="espe-header">
      {/* BARRA SUPERIOR AZUL: solo menú a la derecha */}
      <div className="espe-topbar">
        <div className="espe-secondbar-left">
          <img
            src={logo}
            alt="Universidad Yachay Tech"
            className="espe-secondbar-logo"
          />
        </div>
        <div className="espe-topbar-left" />
        <nav className="espe-topbar-nav">
          <TopNavLink to="/sobre-el-proyecto">Sobre el Proyecto</TopNavLink>
          <TopNavLink to="/bases-usadas">Bases Usadas</TopNavLink>
          <TopNavLink to="/metodologia">Metodología</TopNavLink>
          <TopNavLink to="/publicaciones">Publicaciones</TopNavLink>
          <TopNavLink to="/indicadores">Indicadores</TopNavLink>
        </nav>
      </div>

      {/* SEGUNDA FILA (gris claro): logo a la izquierda, Indicadores / Validación a la derecha */}
      {/* <div className="espe-secondbar">
        <div className="espe-secondbar-left">
          <img
            src={logo}
            alt="Universidad Yachay Tech"
            className="espe-secondbar-logo"
          />
        </div>

        <nav className="espe-secondbar-nav">
          <SecondaryNavLink to="/indicadores">Indicadores</SecondaryNavLink>
          <SecondaryNavLink to="/validacion">Validación INEC</SecondaryNavLink>
          Página web hecha por Patricio J. Mendoza Núñez */}
        {/* </nav> */}
      {/* </div> */}
    </header>
  );
};

export default Header;
