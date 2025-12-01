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

# 3) Copia los scripts
COPY *.py /app/
COPY *.sh /app/