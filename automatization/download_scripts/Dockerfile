FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1

# 1) Instala Chrome y utilidades (sin apt-key)
#    - Usa keyring en /etc/apt/keyrings y la opción signed-by
#    - --no-install-recommends para imagen más pequeña
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl gnupg ca-certificates wget unzip && \
    install -m 0755 -d /etc/apt/keyrings && \
    curl -fsSL https://dl.google.com/linux/linux_signing_key.pub \
      | gpg --dearmor -o /etc/apt/keyrings/google-linux-signing-keyring.gpg && \
    chmod a+r /etc/apt/keyrings/google-linux-signing-keyring.gpg && \
    echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/google-linux-signing-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" \
      > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends google-chrome-stable && \
    # Paquetes útiles para Chrome en entornos headless (fuentes y algunos libs)
    apt-get install -y --no-install-recommends fonts-liberation libasound2 libnspr4 libnss3 libxss1 libgbm1 && \
    # Limpieza
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 2) Instala dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -r requirements.txt

# 3) Copia tus scripts
COPY *.py /app/
COPY *.sh /app/

# # 4) Variables por defecto (puedes sobreescribirlas en docker-compose)
# ENV ENEMDU_ROOT=/data/raw/ENEMDU \
#     LATINOBAROMETRO_ROOT=/data/raw/LATINOBAROMETRO_ \
#     VDEM_ROOT=/data/raw/VDEM \
#     VDEM_DATA=/data/VDEM \
#     PERSONA_UNPROC=/data/enemdu_persona/unprocessed \
#     PERSONA_PROCESSED=/data/enemdu_persona/processed \
#     VIVIENDA_UNPROC=/data/enemdu_vivienda/unprocessed \
#     VIVIENDA_PROCESSED=/data/enemdu_vivienda/processed \
#     LATINOBAROMETRO_UNPROC=/data/latinobarometro/unprocessed \
#     LATINOBAROMETRO_DICT_CSV=/data/latinobarometro/latinobarometro_glossary_candidates_BM.csv \
#     LATINOBAROMETRO_NORM_CSV=/data/latinobarometro/normalized_csv \
#     LATINOBAROMETRO_PROCESSED=/data/latinobarometro/processed

# # 5) Crea los directorios de datos
# RUN mkdir -p "$ENEMDU_ROOT" \
#              "$LATINOBAROMETRO_ROOT" "$VDEM_ROOT" \
#              "$LATINOBAROMETRO_NORM_CSV" \
#              "$VDEM_DATA" "$LATINOBAROMETRO_UNPROC" \
#              "$LATINOBAROMETRO_PROCESSED" \
#              "$PERSONA_UNPROC" "$PERSONA_PROCESSED" \
#              "$VIVIENDA_UNPROC" "$VIVIENDA_PROCESSED"

# # 6) Al arrancar, descargas y luego limpiezas
# # CMD ["sh", "-c", "python enemdu_descarga.py && python latinobarometro_descarga.py && python vdem_descarga.py && python limpieza_persona.py && python limpieza_vivienda.py && python limpieza_vdem.py && python limpieza_latinobarometro.py"]
