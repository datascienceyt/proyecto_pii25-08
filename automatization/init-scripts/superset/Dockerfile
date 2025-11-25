FROM apache/superset:latest

USER root

ENV HOME=/home/superset \
    SUPERSET_HOME=/home/superset \
    PIP_CACHE_DIR=/home/superset/.cache/pip

# Toolchain para compilar paquetes tipo python-geohash
RUN set -eux; \
    if command -v apt-get >/dev/null 2>&1; then \
      apt-get update && \
      DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        build-essential gcc g++ python3-dev curl && \
      rm -rf /var/lib/apt/lists/*; \
    elif command -v apk >/dev/null 2>&1; then \
      apk add --no-cache build-base gcc g++ musl-dev python3-dev curl; \
    elif command -v yum >/dev/null 2>&1; then \
      yum install -y gcc gcc-c++ make python3-devel curl && \
      yum clean all; \
    fi

# HOME y cache de pip
RUN mkdir -p /home/superset/.cache/pip && chown -R superset:superset /home/superset

# Instalar dependencias detectando el intérprete y asegurando pip en el venv
RUN set -eux; \
    # 1) Detecta intérprete
    if [ -x /app/.venv/bin/python ]; then \
      PY=/app/.venv/bin/python; \
    else \
      PY="$(command -v python3 || command -v python)"; \
    fi; \
    # 2) Asegura pip en ese intérprete (el venv de Superset no siempre trae pip)
    "$PY" -m ensurepip --upgrade || true; \
    # 3) Siempre usar "python -m pip" para evitar problemas de PATH
    PIPCMD="$PY -m pip"; \
    $PIPCMD install --no-cache-dir --upgrade pip wheel setuptools; \
    # 4) Instala tus extras/drivers
    $PIPCMD install --no-cache-dir \
      flask_cors \
      clickhouse-sqlalchemy \
      clickhouse-driver \
      'sqlalchemy==1.4.54' \
      clickhouse-connect
# Nota: 'apache-superset' ya viene en la imagen; si quieres forzar [cors]:
#    $PIPCMD install --no-cache-dir 'apache-superset[cors]'

# Copiamos scripts/config y entrypoint
# (Si prefieres seguir montándolos por volumen, puedes omitir estos COPY)
# Aquí los dejamos como opcional: si existen, se copian; si no, no falla.
# Reemplaza las rutas si tu estructura difiere.
COPY --chown=superset:superset ./ /app/superset-init
COPY --chown=superset:superset ./superset_config.py /app/pythonpath/superset_config.py

# Copia el entrypoint de arranque
COPY ./entrypoint.sh /usr/local/bin/custom-entrypoint.sh
RUN chmod +x /usr/local/bin/custom-entrypoint.sh

# Deja root para poder chown el bind mount en runtime y luego bajar a 'superset'
USER root
EXPOSE 8088
ENTRYPOINT ["/usr/local/bin/custom-entrypoint.sh"]
CMD ["run"]
