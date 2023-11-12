from src.ejercicio4 import seleccionar_mes_dict

def test_seleccionar_mes_dict():
    dict_mes = {"01" : "Enero", "02" : "Febrero", "03" : "Marzo", "04" : "Abril", "05" : "Mayo", "06" : "Junio", "07" : "Julio", "08" : "Agosto", "09" : "Septiembre", "10" : "Octubre", "11" : "Noviembre", "12" : "Diciembre"}
    assert seleccionar_mes_dict(dict_mes,['12', '02', '2014']) == "Febrero"