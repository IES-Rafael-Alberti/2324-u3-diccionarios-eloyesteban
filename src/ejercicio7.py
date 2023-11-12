"""
Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato
"""

def inicializa_cesta_compra():
    cesta_compra = {} 
    return cesta_compra


def pide_informacion_por_consola():
    item = input("introduce el item que va añadir a la cesta: ")
    item = item.upper()
    precio = float(input("Introduce el precio de " + item + ": "))
    return item, precio


def registra_dato(cesta_compra:dict, item:str, precio:float):
    cesta_compra[item] = precio
            


if __name__ == "__main__":

    cesta_compra = inicializa_cesta_compra()
    
    continuar = True

    #Procesar
    while continuar:
        #Entrada
        item, precio = pide_informacion_por_consola()
        #Procesar
        registra_dato(cesta_compra,item,precio)
        #Entrada
        continuar = input('¿Quieres añadir artículos a la lista (Si/No)? ').upper() == "SI"
    coste = 0
    
    #Salida
    print("Cesta de Compra")
    for item, precio in cesta_compra.items():
        print(item, "\t", precio)
        coste += precio
    print("Coste total: ", coste )
