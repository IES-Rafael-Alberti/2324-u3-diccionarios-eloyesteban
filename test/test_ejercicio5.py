from src.ejercicio5 import seleccion_creditos

def test_seleccion_creditos():
    creditos_asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    assert seleccion_creditos(creditos_asignaturas,"Matemáticas") == 6