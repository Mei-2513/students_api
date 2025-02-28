# Students API

Este proyecto es una API en Flask que usa PostgreSQL como base de datos y se ejecuta en Docker con Docker Compose. También permite gestionar un registro de estudiantes, incluyendo la creación, actualización, consulta y eliminación de datos.

## 📌 Requisitos
- Docker y Docker Compose instalados.

## 🚀 Instalación y Ejecución
1. Clona el repositorio:
   ```bash
   git clone https://github.com/Mei-2513/students_api.git
   cd students_api
   ```

2. Construye y levanta los servicios usando el comando:

   ```bash
   docker-compose up -d --build
   ```

3. Para verificar que la API funciona, prueba este comando:

   ```bash
   curl http://localhost:5000/students
   ```

4. Para obtener todos los estudiantes:

   ```bash
   curl -X GET http://localhost:5000/students
   ```

   **Ejemplo de respuesta:**
   ```json
   [{ "carrera": "Ingeniería", "edad": 22, "id": 2, "nombre": "Juan" }]
   ```

5. Para agregar un nuevo estudiante:

   ```bash
   curl -X POST http://localhost:5000/students -H "Content-Type: application/json" -d '{ "nombre": "Juan", "edad": 22, "carrera": "Ingeniería" }'
   ```

   **Respuesta:**
    json
   { "message": "Estudiante agregado", "id": 1 }
   ```

6. Para actualizar un estudiante:

   ```bash
   curl -X PUT http://localhost:5000/students/1 -H "Content-Type: application/json" -d '{ "nombre": "Juan Pérez", "edad": 23, "carrera": "Ingeniería de Software" }'
   ```

   **Respuesta:**
   ``json
   { "message": "Estudiante actualizado" }
   ```

7. Para eliminar un estudiante:

   ```bash
   curl -X DELETE http://localhost:5000/students/1
   ```

   **Respuesta:**
   ``json
   { "message": "Estudiante eliminado" }
   ```

8. Para comprobar los contenedores en ejecución:

   ```bash
   docker ps
   ```

9. Para apagar los contenedores:

   ```bash
   docker-compose down
   ```


