"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello. 
"""

def comprobar_fruta(precio_frutas, fruta):
    return precio_frutas.get(fruta)

if __name__ == "__main__":

    precio_frutas = {"PLATANO" : 1.35, "MANZANA" : 0.80, "PERA" : 0.85, "NARANJA" : 0.70}

    #Entrada
    fruta = input("Elige una fruta de la lista(PLATANO-MANZANA-PERA-NARANJA): ")
    fruta = fruta.upper()

    #Procesar
    resultado = comprobar_fruta(precio_frutas, fruta)

    if resultado:
        kilo = float(input("Introduce los kilos de fruta: "))
        precio = resultado * kilo
        
        #Salida
        print("Has seleccionado " + str(kilo) + " kg de " + fruta + ", son " + str(precio) + " euros" ) 
    else:
        #Salida
        print("No disponemos de esa fruta, por favor elige una de la lista!!")
    

    