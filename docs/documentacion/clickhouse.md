# Esquema ClickHouse

## Base
- `indicadores` (MergeTree; partición por `periodo`, orden por `periodo`).

## Tablas principales
- `enemdu_persona` (edad, sexo, condact, ingresos, etc.).  
- `enemdu_vivienda` (materiales, servicios básicos, etc.).  
- `mf_finanzas` (presupuesto por territorio).

> Además, la ingesta contempla **Latinobarómetro** y **V-Dem** como tablas agregadas por país-año preparadas por los procesos de `automatic_ingest`. (Ver manual y scripts de ingest.)

## Vistas materializadas
- `mv_indicadores_persona_canton`: métricas laborales (TPG, empleo, informalidad, brechas, desempleo juvenil, etc.).

## Operación
- Health: `curl http://localhost:8123/ping`  
- Cliente: `clickhouse-client --host clickhouse_server --port 9000 --user $CH_USER --password $CH_PASSWORD`
