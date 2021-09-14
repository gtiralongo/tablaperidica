from difflib import SequenceMatcher as SM
ARCHIVO = "\tabla periodica.csv"
#\tabla periodica.csv

def leerDesdeArchivo(nombreArchivo):
    tabla = {}
    archivo = open(nombreArchivo,'r')
    linea = archivo.readline()

    while linea != "":
        elemento = []
        # linea.replace('\n','') buscar la forma de sacar el \n
        sep = linea.split(",")
        # nuemros = numero ++ 1
        # print(numeros)
        for p in sep:
            elemento.append(p)
            # print(p)
            # if p == nAtomico ++ 1:
        for i in elemento:
            tabla.update({elemento[0] :{"número atomico":elemento[0],"elemento":elemento[1],"simbolo":elemento[2],"grupo":elemento[3],"masa":elemento[4],"configuracion electronica":elemento[5],"formula electronica":elemento[6],"Punto de fusion":elemento[7],"Punto de ebullicion":elemento[8]}})
            # if elemento[0] == numeros:
        linea = archivo.readline()
        # print(tabla)
    archivo.close()
    return tabla

    # tablaPeriodica ={"número atomico":,"elemento":,"simbolo":,"grupo":,"masa":,"configuracion electronica":,"formula electronica":,"Punto de fusion":,"Punto de ebullicion":}


#
# def buscador(valorBuscado,origenDeBusqueda):
#     origen = origenDeBusqueda
#     for b in origen:
#         if valorBuscado == origen:
#             print(b)
#
#     return b

# def my_decorator(func):
#     def decorar(func):
#         "----------------"
#         func
#         "----------------"
#         return(func)
#     return decorar

# @my_decorator
def buscador(origenDeBusqueda):
    valorBuscado = input("Escriba el valor buscado: ")
    element_list = []
    for b in origenDeBusqueda:
        for i in origenDeBusqueda[b]:
            if SM(None,origenDeBusqueda[b][i],valorBuscado).ratio() > 0.75: # se puede modificar el ratio de coincidencia minimo
            # if origenDeBusqueda[b][i] == valorBuscado:
                element_list.append(origenDeBusqueda[b]) #agregar una opcion para seguir buscando si no entuentra el varlor buscado
    if len(element_list) == 0:
        print("El valor no fue encontrado por favor vuelva a intentarlo")
        buscador(origenDeBusqueda)
    else:
        for el in element_list: 
            print("--------------------")
            print("Elemento encontrado:")
            print(" ")
            print(el)
        # return print(element_list)      
                
# return origenDeBusqueda[b]

def main():
    tabla = leerDesdeArchivo(ARCHIVO)
    print("Puede realizar la busqueda por numero atomico, elemento, simbolo, grupo, masa, configuracion electrica, formula electronica, punto de fusión, punto de ebullición")
    print("Categotias de grupo :\n"+"a1 Singular\n"+"0 gas noble\n"+"a1 alcalino\n"+"a2 alcalino-terreo\n"+"a3 terreo\n"+"a4 carbonoideo\n"+"a5 nitrogenoideo\n"+"a6 anfigeno\n"+"a7 halogeno\n"+"b3 metal de transicion\n"+"b4 metal de transicion\n"+"b5 metal de transicion\n"+"b6 metal de transicion\n"+"b7 metal de transicion\n"+"b8 metal de transicion\n"+"b1 metal de transicion\n"+"b2 metal de transicion\n"+"b3 lantanido\n"+"b3 actinido\n"+"sin determinar")
    buscador(tabla)

main()
