import os
from flask import Flask, request, jsonify, redirect, url_for, render_template, send_from_directory
from models.alumno import collection, Alumno
from bson.objectid import ObjectId

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Crear un nuevo alumno
@app.route('/alumnos', methods=['POST'])
def create_alumno():
    data = request.json
    nuevo_alumno = Alumno(data['alumno'], data['edad'], data['carrera'], data['forma_del_ser'])
    result = collection.insert_one(nuevo_alumno.to_dict())
    return jsonify(str(result.inserted_id)), 201

# Obtener todos los alumnos
@app.route('/alumnos', methods=['GET'])
def get_alumnos():
    alumnos = list(collection.find())
    for alumno in alumnos:
        alumno['_id'] = str(alumno['_id'])
    return jsonify(alumnos), 200

# Obtener un alumno por ID
@app.route('/alumnos/<id>', methods=['GET'])
def get_alumno(id):
    alumno = collection.find_one({"_id": ObjectId(id)})
    if alumno:
        alumno['_id'] = str(alumno['_id'])
        return jsonify(alumno), 200
    else:
        return jsonify({"error": "Alumno no encontrado"}), 404

# Actualizar un alumno por ID
@app.route('/alumnos/<id>', methods=['PUT'])
def update_alumno(id):
    data = request.json
    result = collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    if result.matched_count:
        return jsonify({"message": "Alumno actualizado exitosamente"}), 200
    else:
        return jsonify({"error": "Alumno no encontrado"}), 404

# Eliminar un alumno por ID
@app.route('/alumnos/<id>', methods=['DELETE'])
def delete_alumno(id):
    result = collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return jsonify({"message": "Alumno eliminado exitosamente"}), 200
    else:
        return jsonify({"error": "Alumno no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)