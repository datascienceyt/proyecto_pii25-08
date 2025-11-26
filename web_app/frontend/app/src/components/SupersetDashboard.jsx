// src/components/SupersetDashboard.jsx
import React, { useEffect, useRef } from "react";
import { embedDashboard } from "@superset-ui/embedded-sdk";

const SUPERSET_DOMAIN = "http://localhost:8088";
const BACKEND_GATEWAY = "http://localhost:8080";

const SupersetDashboard = ({ dashboardId }) => {
  const containerRef = useRef(null);

  useEffect(() => {
    // Capture the mount element once for this effect run
    const mountEl = containerRef.current;

    if (!dashboardId) {
      if (mountEl) {
        mountEl.innerHTML = "";
      }
      return;
    }
    if (!mountEl) return;

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
        throw new Error("Backend did not return a valid token");
      }
      return data.token;
    }

    async function doEmbed() {
      try {
        api = await embedDashboard({
          id: String(dashboardId),
          supersetDomain: SUPERSET_DOMAIN,
          mountPoint: mountEl,
          // SDK will call this whenever it needs a token (including renewals)
          fetchGuestToken,
          dashboardUiConfig: {
            hideTitle: true,
          },
        });

        // Force iframe to fill the container
        const iframe = mountEl.querySelector("iframe");
        if (iframe) {
          iframe.style.width = "100%";
          iframe.style.height = "100%";
          iframe.style.border = "0";
          iframe.style.display = "block";
        }
      } catch (e) {
        console.error(e);
        if (!destroyed && mountEl) {
          mountEl.innerHTML = `<div style="padding:16px;color:#b00">${e.message}</div>`;
        }
      }
    }

    doEmbed();

    return () => {
      destroyed = true;
      if (api && typeof api.destroy === "function") {
        api.destroy(); // stop the embed, it should not request tokens anymore
      }
      if (mountEl) {
        mountEl.innerHTML = "";
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
