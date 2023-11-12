"""
Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro. 
"""

def definir_facturas():
    facturas = {} 
    return facturas

def pide_informacion_por_consola():
    numero_factura = input('Introduce el número de la factura: ')
    coste = float(input('Introduce el coste de la factura: '))
    return numero_factura, coste

def registra_dato(facturas:dict, numero_factura:str, coste:float, pendiente:float):
    facturas[numero_factura] = coste

def pago_de_factura(factura:dict, numero_factura:str, coste:float, pendiente:float):
    numero_factura = input('Introduce el número de la factura a pagar: ')
    coste = facturas.pop(numero_factura, 0)



if __name__ == "__main__":

    facturas = definir_facturas()

    pagado = 0
    pendiente = 0

    menu = input('¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? ')
    menu = menu.upper()

    while menu != "T":
        if menu == 'A':
            numero_factura, coste = pide_informacion_por_consola()
            registra_dato(facturas,numero_factura,coste,pendiente)
            pendiente += coste

        elif menu == "P":
            pago_de_factura(facturas,numero_factura,coste,pendiente)
            pagado += coste 
            pendiente -= coste
        print("Pagado: " + str(pagado))
        print("Pendiente:" + str(pendiente))
        menu = input("¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)?")
        menu = menu.upper()


