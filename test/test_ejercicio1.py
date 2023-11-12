from src.ejercicio1 import comparar_diccionario

def test_comparar_diccionario():
    diccionario = {'EURO':'€', 'DOLLAR':'$', 'YEN':'¥'}
    assert comparar_diccionario(diccionario,"EURO") == "€"
    assert comparar_diccionario(diccionario,"DOLLAR") == "$"
    assert comparar_diccionario(diccionario,"YEN") == "¥"