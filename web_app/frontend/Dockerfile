FROM node:22-alpine

WORKDIR /app

COPY app/package*.json ./
RUN npm install
RUN npm install react-router-dom --save


COPY app ./

CMD ["npm", "start"]
