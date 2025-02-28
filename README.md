# Students API

Este proyecto es una API en Flask que usa PostgreSQL como base de datos y se ejecuta en Docker con Docker Compose, tambien esta API permite gestionar un registro de estudiantes, incluyendo la creación, actualización, consulta y eliminación de datos.

## 📌 Requisitos
- Docker y Docker Compose instalados.

## 🚀 Instalación y Ejecución
1. Clona el repositorio:
   ```bash
   git clone https://github.com/Mei-2513/students_api.git
   cd students_api

2. Construye y levanta los servicios-->usando el comando:

           docker-compose up -d --build

3.Para verificar que la API funciona, prueba este comando:

           curl http://localhost:5000/students

4.Para obtener todos los estudiantes:
         
           curl -X GET http://localhost:5000/students

Ejemplo de respuesta:

[
  {
    "carrera": "Ingeniería",
    "edad": 22,
    "id": 2,
    "nombre": "Juan"
  }
]

5.Para agregar un nuevo estudiante:

curl -X POST http://localhost:5000/students -H "Content-Type: application/json" -d '{
  "nombre": "Juan",
  "edad": 22,
  "carrera": "Ingeniería"
}'
Respuesta: {
  "message": "Estudiante agregado",
  "id": 1
}


6.Para actualizar: 
 
   curl -X PUT http://localhost:5000/students/1 -H "Content-Type: application/json" -d '{
  "nombre": "Juan Pérez",
  "edad": 23,
  "carrera": "Ingeniería de Software"
}'

Respuesta: {
  "message": "Estudiante actualizado"
}

7.Para eliminar: 

curl -X DELETE http://localhost:5000/students/1

Respuesta: {
  "message": "Estudiante eliminado"
}


8. Para comprobar los contenedores:
 
 docker ps



9.Para apagar los contenedores:

           docker-compose down






















