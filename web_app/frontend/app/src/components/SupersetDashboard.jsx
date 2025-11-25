// src/components/SupersetDashboard.jsx
import React, { useEffect, useRef } from "react";
import { embedDashboard } from "@superset-ui/embedded-sdk";

// Ajusta estas URLs a tu entorno
const SUPERSET_DOMAIN = "http://localhost:8088";
const BACKEND_GATEWAY = "http://localhost:8080";

const SupersetDashboard = ({ dashboardId }) => {
  const containerRef = useRef(null);

  useEffect(() => {
    if (!dashboardId) {
      if (containerRef.current) {
        containerRef.current.innerHTML = "";
      }
      return;
    }
    if (!containerRef.current) return;

    let destroyed = false;
    let api = null;

    async function fetchGuestToken() {
      const res = await fetch(`${BACKEND_GATEWAY}/api/superset/guest-token`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ dashboardId }),
      });

      if (!res.ok) {
        throw new Error(`Backend ${res.status}`);
      }

      const data = await res.json();
      if (!data?.token || typeof data.token !== "string") {
        throw new Error("El backend no devolvió un token válido");
      }
      return data.token;
    }

    async function doEmbed() {
      try {
        api = await embedDashboard({
          id: String(dashboardId),
          supersetDomain: SUPERSET_DOMAIN,
          mountPoint: containerRef.current,
          // el SDK llamará a esta función cada vez que necesite (incluida la renovación)
          fetchGuestToken,
          dashboardUiConfig: {
            hideTitle: true,
          },
        });

        // forzar que el iframe llene el contenedor
        const iframe = containerRef.current.querySelector("iframe");
        if (iframe) {
          iframe.style.width = "100%";
          iframe.style.height = "100%";
          iframe.style.border = "0";
          iframe.style.display = "block";
        }
      } catch (e) {
        console.error(e);
        if (!destroyed && containerRef.current) {
          containerRef.current.innerHTML = `<div style="padding:16px;color:#b00">${e.message}</div>`;
        }
      }
    }

    doEmbed();

    return () => {
      destroyed = true;
      if (api && typeof api.destroy === "function") {
        api.destroy(); // detenemos el embed, ya no debe pedir tokens
      }
      if (containerRef.current) {
        containerRef.current.innerHTML = "";
      }
    };
  }, [dashboardId]);

  return (
    <div
      ref={containerRef}
      id="superset-container"
      style={{
        width: "100%",
        minHeight: "100vh",
        height: "145vh",
        background: "#f5f7fa",
        borderRadius: 12,
        overflow: "hidden",
      }}
    />
  );
};

export default SupersetDashboard;
