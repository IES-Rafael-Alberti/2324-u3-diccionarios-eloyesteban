from src.ejercicio6 import registra_dato, inicializa_persona

def test_registra_dato():
    persona = {}
    tipo_dato = "edad"
    dato = "25"

    registra_dato(persona, tipo_dato, dato)

    assert tipo_dato in persona
    assert persona[tipo_dato] == dato

def test_inicializa_persona():
    persona = inicializa_persona()
    assert isinstance(persona, dict)
    assert not persona
