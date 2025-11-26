// server.js (ESM)
import "dotenv/config";
import express from "express";
import cors from "cors";
import axios from "axios";
import jwt from "jsonwebtoken";

const app = express();
app.use(express.json());
// app.use(cors());

app.use(
  cors({
    origin: "http://localhost:3000", // puerto del frontend
    methods: ["GET", "POST", "OPTIONS"],
    allowedHeaders: ["Content-Type", "Authorization"],
  })
);

// (Opcional pero a veces útil)
app.options("*", cors());


// ---------- ENV ----------
const PORT = process.env.PORT || 8080;
const SUPERSET_URL = process.env.SUPERSET_URL || "http://superset:8088";
const SUP_USER = process.env.SUPERSET_USER;
const SUP_PASS = process.env.SUPERSET_PASS;

if (!SUP_USER || !SUP_PASS) {
  throw new Error("Faltan SUPERSET_USER o SUPERSET_PASS en las variables de entorno");
}

const ALLOWED_RAW = process.env.ALLOWED_DASHBOARDS || "";
const ALLOWED_DASHBOARDS = new Set(
  ALLOWED_RAW.split(",").map((s) => s.trim()).filter(Boolean)
);

// Desactivar en producción
// console.log("Gateway config:", {
//   PORT,
//   SUPERSET_URL,
//   SUP_USER,
//   // OJO: nunca loguees la password en producción
//   hasSupPass: Boolean(SUP_PASS),
//   ALLOWED_DASHBOARDS,
// });

// ---------- LOGIN Y TOKEN CACHÉ ----------
let cachedAccessToken = null;
let cachedAccessExp = 0;

async function getSupersetAccessToken() {
  const now = Math.floor(Date.now() / 1000);
  if (cachedAccessToken && cachedAccessExp - 60 > now) {
    return cachedAccessToken;
  }

  const loginUrl = `${SUPERSET_URL}/api/v1/security/login`;
  const { data } = await axios.post(loginUrl, {
    username: SUP_USER,
    password: SUP_PASS,
    provider: "db",
    refresh: true,
  });

  const token = data?.access_token;
  if (!token) throw new Error("No se obtuvo access_token de Superset");

  const decoded = jwt.decode(token);
  cachedAccessToken = token;
  cachedAccessExp = decoded?.exp || (now + 300);
  return token;
}

// ---------- API: guest token ----------
app.post("/api/superset/guest-token", async (req, res) => {
  try {
    const { dashboardId } = req.body || {};
    if (!dashboardId) {
      return res.status(400).json({ error: "Falta 'dashboardId' en el body" });
    }

    if (ALLOWED_DASHBOARDS.size && !ALLOWED_DASHBOARDS.has(String(dashboardId))) {
      return res.status(403).json({
        error: "Dashboard no permitido por ALLOWED_DASHBOARDS",
      });
    }

    const accessToken = await getSupersetAccessToken();

    const guestUrl = `${SUPERSET_URL}/api/v1/security/guest_token/`;
    const payload = {
      resources: [{ type: "dashboard", id: String(dashboardId) }],
      rls: [],
      user: { username: "embedded-viewer" },
    };

    const { data } = await axios.post(guestUrl, payload, {
      headers: {
        Authorization: `Bearer ${accessToken}`,
        "Content-Type": "application/json",
      },
    });

    if (!data?.token) {
      return res.status(502).json({ error: "Superset no devolvió 'token'" });
    }

    res.json({ token: data.token });
  } catch (err) {
    console.error(err?.response?.data || err.message);
    const status = err?.response?.status || 500;
    res.status(status).json({
      error:
        err?.response?.data?.message ||
        err?.message ||
        "Error generando guest token",
    });
  }
});

// ---------- HEALTH ----------
app.get("/health", (_req, res) => res.json({ ok: true }));

app.listen(PORT, () => {
  console.log(`-> Gateway listening on http://localhost:${PORT}`);
});