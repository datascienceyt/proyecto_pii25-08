# Configuración de Superset

Este documento describe la configuración de conexión a la base de datos, datasets, métricas y control de accesos.

---

## 🔗 Conexión a ClickHouse

- Driver: `clickhouse-sqlalchemy`.
- Configuración vía variables de entorno:
  ```yaml
  DATABASE_DIALECT=clickhouse
  DATABASE_HOST=clickhouse
  DATABASE_PORT=8123
  DATABASE_DB=indicadores
  DATABASE_USER=admin
  DATABASE_PASSWORD=secret_pw
  ```

---

## 📊 Datasets

- **Indicadores Persona (Canton)** → basado en `mv_indicadores_persona_canton`.
- **Indicadores Vivienda** → basado en `enemdu_vivienda`.
- **Presupuesto Finanzas** → basado en `mf_finanzas`.

---

## 📈 Métricas y Dashboards

- **Empleo y Subempleo**: TPG, Tasa de empleo, Subempleo.
- **Formalidad e Informalidad**.
- **Brechas de Género**: salario, empleo adecuado.
- **Juventud y NNA**: desempleo juvenil, trabajo infantil.
- **Presupuesto por provincia y cantón**.

---

## 👤 Permisos y Seguridad

- Usuario `admin` creado automáticamente en arranque:
  - Usuario: `admin`.
  - Password: configurable en `.env`.
- Dashboards de ejemplo deshabilitados (`SUPERSET_LOAD_EXAMPLES=no`).
- Recomendación: integrar con LDAP u OIDC en producción.

---
