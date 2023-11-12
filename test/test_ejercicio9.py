from src.ejercicio9 import definir_facturas,registra_dato

def test_definir_facturas():
    facturas = definir_facturas()
    assert facturas == {}

def test_registra_dato():
    facturas = {}
    numero_factura = "F001"
    coste = 100.0
    pendiente = 0.0
    registra_dato(facturas, numero_factura, coste, pendiente)
    assert facturas == {"F001": 100.0}
