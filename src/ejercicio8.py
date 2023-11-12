""" 
Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
""" 

def inicializa_diccionario():
    diccionario = {}
    return diccionario

def pide_palabras_por_consola():
    palabras = input("Introduce las palabras en el siguiente formato (palabra:traduccion) separadas por comas: ")
    return palabras

def registra_dato(diccionario, palabra):
    español, ingles = palabra.split(":")
    diccionario[español.strip()] = ingles.strip()

def pide_frase_por_consola():
    frase = input("Introduce la frase que quieres traducir a inglés: ")
    return frase

if __name__ == "__main__":
    diccionario = inicializa_diccionario()

    # Entrada
    palabras = pide_palabras_por_consola()

    # Procesar
    for palabra in palabras.split(","):
        registra_dato(diccionario, palabra)
    
    # Entrada
    frase = pide_frase_por_consola()

    # Procesar y salida
    traduccion = " ".join(diccionario.get(palabra, "") for palabra in frase.split())
    print("Traducción:", traduccion)
