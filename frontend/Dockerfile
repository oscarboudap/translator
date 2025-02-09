FROM node:16

# Configurar el directorio de trabajo
WORKDIR /app

# Copiar archivos de dependencias
COPY translator/package.json .

RUN npm install

# Copiar el código fuente
COPY . .

# Exponer el puerto de React
EXPOSE 3000

# Comando para iniciar la aplicación
CMD ["npm", "start"]