from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de datos simulada en memoria
BASE_DATOS_TAREAS = []

@app.route('/tareas', methods=['POST'])
def crear_tarea():
    datos = request.get_json()
    # Validación básica de datos faltantes
    if not datos or 'titulo' not in datos or 'empleado_id' not in datos:
        return jsonify({"error": "Datos inválidos o faltantes"}), 400
    
    nueva_tarea = {
        "id": len(BASE_DATOS_TAREAS) + 1,
        "titulo": datos['titulo'],
        "empleado_id": datos['empleado_id'],
        "completada": False
    }
    BASE_DATOS_TAREAS.append(nueva_tarea)
    return jsonify(nueva_tarea), 201

@app.route('/tareas', methods=['GET'])
def listar_tareas():
    return jsonify(BASE_DATOS_TAREAS), 200

if __name__ == '__main__':
    app.run(debug=True)
