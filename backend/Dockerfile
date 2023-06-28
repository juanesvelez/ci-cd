# Usamos una imagen de Node.js
FROM node:14

# Establecemos el directorio de trabajo
WORKDIR /usr/src/app

# Copiamos el archivo package.json al contenedor
COPY package*.json ./


RUN apt-get update

# Instalamos las dependencias de la aplicación
RUN npm install

# Copiamos el resto del código al contenedor
COPY . .

# Exponemos el puerto en el que se ejecuta la aplicación
EXPOSE 3000

COPY wait-for-it.sh /usr/src/app/wait-for-it.sh
RUN chmod +x /usr/src/app/wait-for-it.sh
# Ejecutamos la aplicación
CMD [ "./wait-for-it.sh", "db:3306", "--", "node", "server.js" ]
