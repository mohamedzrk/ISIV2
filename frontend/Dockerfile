# Utilizar Node para construir la app
FROM node:18 AS build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY ./src ./src
COPY ./public ./public

RUN npm run build

# Utilizar nginx para servir los archivos
FROM nginx:alpine

COPY --from=build /app/build /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
