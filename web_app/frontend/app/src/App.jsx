// src/App.jsx
import React from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import ProjectPage from "./pages/ProjectPage";
import MethodologyPage from "./pages/MethodologyPage";
import BasesUsadasPage from "./pages/BasesUsadasPage";
import IndicatorsPage from "./pages/IndicatorsPage";
import ValidationPage from "./pages/ValidationPage";
import PublicationsPage from "./pages/PublicationsPage";
import "./styles.css";

const App = () => {
  return (
    <BrowserRouter>
      <Header />
      <main className="app-main">
        <Routes>
          {/* Homepage → redirige a "Sobre el Proyecto" */}
          <Route
            path="/"
            element={<Navigate to="/sobre-el-proyecto" replace />}
          />

          <Route path="/sobre-el-proyecto" element={<ProjectPage />} />
          <Route path="/metodologia" element={<MethodologyPage />} />
          <Route path="/bases-usadas" element={<BasesUsadasPage />} />
          <Route path="/publicaciones" element={<PublicationsPage />} />
          <Route path="/indicadores" element={<IndicatorsPage />} />
          <Route path="/validacion" element={<ValidationPage />} />

          <Route
            path="*"
            element={
              <div className="page">
                <h2>404</h2>
                <p>La página solicitada no existe.</p>
              </div>
            }
          />
        </Routes>
      </main>
      <Footer />
    </BrowserRouter>
  );
};

export default App;
