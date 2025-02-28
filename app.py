import time
import psycopg2
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@db/students_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de estudiantes
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    carrera = db.Column(db.String(100), nullable=False)

# Esperar a que la base de datos esté lista
def wait_for_db():
    retries = 10
    while retries > 0:
        try:
            conn = psycopg2.connect(
                dbname="students_db",
                user="admin",
                password="admin",
                host="db",
                port="5432"
            )
            conn.close()
            print("📌 Conexión a PostgreSQL exitosa")
            return
        except psycopg2.OperationalError:
            print("⏳ Esperando que la base de datos esté lista...")
            time.sleep(5)
            retries -= 1
    print("❌ No se pudo conectar a la base de datos después de varios intentos.")
    exit(1)

# Crear la base de datos si no existe
with app.app_context():
    wait_for_db()
    db.create_all()

# Obtener todos los estudiantes
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    students_list = [{"id": s.id, "nombre": s.nombre, "edad": s.edad, "carrera": s.carrera} for s in students]
    return jsonify(students_list)

# Agregar un estudiante
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(nombre=data['nombre'], edad=data['edad'], carrera=data['carrera'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"message": "Estudiante agregado", "id": new_student.id})

# Actualizar un estudiante
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({"message": "Estudiante no encontrado"}), 404
    data = request.get_json()
    student.nombre = data['nombre']
    student.edad = data['edad']
    student.carrera = data['carrera']
    db.session.commit()
    return jsonify({"message": "Estudiante actualizado"})

# Eliminar un estudiante
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({"message": "Estudiante no encontrado"}), 404
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Estudiante eliminado"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

