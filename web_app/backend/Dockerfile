FROM node:20-alpine
WORKDIR /app

# Solo copiamos manifest para aprovechar la caché de Docker
COPY package*.json ./

# Instala dependencias de producción sin lockfile
RUN npm install axios-cookiejar-support express cors axios jsonwebtoken dotenv
RUN npm install --omit=dev --no-audit --no-fund

# Copiamos el código
COPY server.js ./

EXPOSE 8080
CMD ["node", "server.js"]
