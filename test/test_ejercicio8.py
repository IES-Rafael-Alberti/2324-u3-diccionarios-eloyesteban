from src.ejercicio8 import registra_dato, pide_frase_por_consola, pide_palabras_por_consola, inicializa_diccionario

def test_registra_dato():
    diccionario = {}
    palabra_input = "casa:house"

    registra_dato(diccionario, palabra_input)

    assert "casa" in diccionario
    assert diccionario["casa"] == "house"

def test_pide_frase_por_consola(monkeypatch):
    frase_input = "La casa es bonita"

    monkeypatch.setattr('builtins.input', lambda _: frase_input)

    frase = pide_frase_por_consola()

    assert frase == frase_input

def test_pide_palabras_por_consola(monkeypatch):
    palabras_input = "casa:house, perro:dog, gato:cat"

    monkeypatch.setattr('builtins.input', lambda _: palabras_input)

    palabras = pide_palabras_por_consola()

    assert palabras == palabras_input

def test_inicializa_diccionario():
    diccionario = inicializa_diccionario()
    assert isinstance(diccionario, dict)
    assert not diccionario 