"""
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario. 
"""

def comparar_diccionario(diccionario, divisa):
        return diccionario.get(divisa)


if __name__ == "__main__":

    #Entrada

    diccionario = {'EURO':'€', 'DOLLAR':'$', 'YEN':'¥'}

    introduce_divisa = input("Introduce una divisa: ")

    #Procesar

    divisa = introduce_divisa.upper()

    resultado = comparar_diccionario(diccionario,divisa)

    #Salida

    if resultado:
        print("La divisa del " + divisa + " es " + resultado)
    else:
        print("La divisa no forma parte del diccionario")


    