from src.ejercicio3 import comprobar_fruta

def test_comprobar_fruta():
    precio_frutas = {"PLATANO" : 1.35, "MANZANA" : 0.80, "PERA" : 0.85, "NARANJA" : 0.70}
    assert comprobar_fruta(precio_frutas,"PLATANO") == 1.35
    assert comprobar_fruta(precio_frutas,"MANZANA") == 0.80
    assert comprobar_fruta(precio_frutas,"PERA") == 0.85
    assert comprobar_fruta(precio_frutas,"NARANJA") == 0.70