"""
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso. 
"""

def seleccion_creditos(creditos_asignaturas,asignatura):
    return creditos_asignaturas.get(asignatura)


if __name__ == "__main__":

    creditos_asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    creditos_totales = 0

    #Procesar
    for asignatura in creditos_asignaturas:
        credito = seleccion_creditos(creditos_asignaturas,asignatura)
        creditos_totales += credito
        #Salida
        print(asignatura + " tiene " + str(credito) + " creditos.")

    #Salida
    print("El numero total de creditos es: " + str(creditos_totales))