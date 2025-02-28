# Imagen base de Python
FROM python:3.10

# Definir el directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY requirements.txt requirements.txt
COPY app.py app.py

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]

