import pytest
from app import app, BASE_DATOS_TAREAS

@pytest.fixture
def cliente():
    app.config['TESTING'] = True
    with app.test_client() as cliente:
        yield cliente
    # Limpia la base de datos simulada tras cada prueba
    BASE_DATOS_TAREAS.clear()

# Prueba: Crear tarea de forma exitosa
def test_crear_tarea_exitoso(cliente):
    respuesta = cliente.post('/tareas', json={"titulo": "Reciclar lote PET-02", "empleado_id": 101})
    assert respuesta.status_code == 201
    assert respuesta.get_json()['titulo'] == "Reciclar lote PET-02"

# Prueba: Validar que falle si faltan datos obligatorios
def test_crear_tarea_invalida(cliente):
    respuesta = cliente.post('/tareas', json={"empleado_id": 101}) # Falta el título corporativo
    assert respuesta.status_code == 400
    assert "error" in respuesta.get_json()

