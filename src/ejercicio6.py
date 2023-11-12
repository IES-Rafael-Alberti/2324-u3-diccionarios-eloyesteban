"""
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""

def inicializa_persona():
    persona = {}
    
    return persona

def pide_informacion_por_consola():
    tipo_dato = input("introduce el tipo de dato que es: ")
    dato = input("Introduce " + tipo_dato + ": ")
            
    return tipo_dato, dato

def registra_dato(persona:dict, tipo_dato:str, dato:str):
    persona[tipo_dato] = dato


if __name__ == "__main__":
    try:
        persona = inicializa_persona()

        # Entrada
        num_datos = int(input("Introduce la cantidad de datos que quieres almacenar: "))

        # Procesar
        for i in range(num_datos):

            # Entrada
            tipo_dato, dato = pide_informacion_por_consola()
            
            # Procesar
            registra_dato(persona, tipo_dato, dato)

            # Salida
            print(persona)

    except ValueError:
        print(f"Error al ingresar la cantidad de datos")
    except Exception:
        print(f"Error general")


