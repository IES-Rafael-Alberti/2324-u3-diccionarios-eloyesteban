"""
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
"""

def seleccionar_mes_dict(dict_mes,fecha):
    return dict_mes.get(fecha[1])


if __name__ == "__main__":

    dict_mes = {"01" : "Enero", "02" : "Febrero", "03" : "Marzo", "04" : "Abril", "05" : "Mayo", "06" : "Junio", "07" : "Julio", "08" : "Agosto", "09" : "Septiembre", "10" : "Octubre", "11" : "Noviembre", "12" : "Diciembre"}

    #Entrada
    fecha = input("Introduce la fecha en el formato dd/mm/aaaa: ")
    
    #Procesar
    fecha = fecha.split("/")
    print(fecha)
    resultado = seleccionar_mes_dict(dict_mes,fecha) #Almacenamos el return de la funcion en la variable resultado

    if resultado:
        
        print(fecha[0] + " de " + resultado + " de " + fecha[2])
    else:

        print("Introduce una fecha válida!!")

    
