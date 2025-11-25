# Operaciones y Runbooks

Este documento cubre procedimientos de operación: backups, rotación de logs y resolución de problemas.

---

## 📦 Backups

- **ClickHouse**:
  - Respaldar volumen `clickhouse_data` (`/var/lib/clickhouse`).
  - Opción: usar `clickhouse-backup` para dumps incrementales.

- **Superset**:
  - Volumen `superset_home`.
  - Exportar dashboards y datasets vía CLI:
    ```bash
    superset export-dashboards -f backup_dashboards.zip
    ```

---

## 📝 Rotación de Logs

- Directorios:
  - `ingest/logs`: ejecución y estado.
  - `ingest/errors`: errores en ingestión.
- Integración recomendada con `logrotate` o ELK Stack.
- Políticas sugeridas:
  - Retención: 30 días.
  - Rotación: semanal.

---

## 🛠️ Troubleshooting

### Ver estado de contenedores
```bash
docker-compose ps
```

### Forzar descarga de ENEMDU
```bash
docker-compose exec enemdu_descarga python enemdu_descarga.py --force
```

### Reprocesar manualmente limpieza
```bash
docker-compose exec enemdu_descarga python limpieza_persona.py
docker-compose exec enemdu_descarga python limpieza_vivienda.py
```

### Resetear base de datos
```bash
docker-compose down --volumes
docker-compose up --build
```

### Validar salud de ClickHouse
```bash
curl http://localhost:8123/ping
```

### Logs de ingestión
- Revisar `/ingest/logs` y `/ingest/errors`.
- Buscar errores de tipo:
  - **Formato inválido** (columnas mal tipadas).
  - **Duplicados**.
  - **Conexión rechazada** a ClickHouse.

---
