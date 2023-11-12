from src.ejercicio7 import registra_dato, inicializa_cesta_compra

def test_registra_dato():
    cesta_compra = {}
    item = "Producto"
    precio = 10.5

    registra_dato(cesta_compra, item, precio)

    assert item in cesta_compra
    assert cesta_compra[item] == precio

def test_inicializa_cesta_compra():
    cesta_compra = inicializa_cesta_compra()
    assert isinstance(cesta_compra, dict)
    assert not cesta_compra