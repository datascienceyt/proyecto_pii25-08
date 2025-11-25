// src/components/Footer.jsx
import React from "react";

const Footer = () => {
  return (
    <footer className="espe-footer-mini">
      <div className="espe-footer-mini-content">
        <span>
          © {new Date().getFullYear()} Universidad Yachay Tech · Proyecto de Democracia en Latinoamérica
        </span>
      </div>
    </footer>
  );
};

export default Footer;
