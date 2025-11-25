#!/bin/sh
set -e

VENV="/app/.venv"
SS="$VENV/bin/superset"
PY="$VENV/bin/python"

# Ajusta permisos del HOME (necesario con bind mounts en Windows)
chown -R superset:superset /home/superset || true
mkdir -p /home/superset/.cache/pip && chown -R superset:superset /home/superset/.cache || true

# Función para ejecutar como usuario 'superset'
as_superset() {
  su -s /bin/sh -c "$*" superset
}

case "$1" in
  run)
    # Migraciones
    as_superset "$SS db upgrade"

    # Crear admin sólo si no existe
    if ! as_superset "$SS fab list-users" | grep -qi 'admin@'; then
      as_superset "$SS fab create-admin \
        --username admin \
        --firstname ${SUPERSET_ADMIN_FIRSTNAME:-Admin} \
        --lastname ${SUPERSET_ADMIN_LASTNAME:-User} \
        --email ${SUPERSET_ADMIN_EMAIL:-admin@example.com} \
        --password ${SUPERSET_ADMIN_PASSWORD:-admin}"
    fi

    # Script de inicialización propio (si existe)
    if [ -f /app/superset-init/init_superset_db.py ]; then
      as_superset "$PY /app/superset-init/init_superset_db.py"
    fi

    # Inicialización estándar de Superset
    as_superset "$SS init"

    # Arrancar servidor
    exec su -s /bin/sh -c "$SS run -h 0.0.0.0 -p 8088" superset
    ;;

  worker)
    # Ejemplo: arrancar Celery worker si lo necesitas
    exec su -s /bin/sh -c "$SS worker" superset
    ;;

  *)
    # Cualquier otro comando se ejecuta tal cual
    exec "$@"
    ;;
esac