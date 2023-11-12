""" 
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
""" 


if __name__ == "__main__":

    diccionario = {}
   
    #Entrada
    diccionario["nombre"] = input("Introduce tu nombre: ")
    diccionario["edad"] = input("Introduce tu edad: ")
    diccionario["dirección"] = input("Introduce tu dirección: ")
    diccionario["telefono"] = input("Introduce tu telefono: ")

    #Salida
    print(diccionario["nombre"] + " tiene " + diccionario["edad"] + " años, vive en " + diccionario["dirección"] + " y su número de telefono es " + diccionario["telefono"])
   
    