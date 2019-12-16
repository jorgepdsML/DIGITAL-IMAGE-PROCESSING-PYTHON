#uso de funciones y variables globales
#definir una funcion con nombre energia

def energia(x1):
    N=len(x1)#cantidad de elementos
    suma=0
    for it in x1:
        suma=suma+it**2
    return suma
#funcion que retorna el promedio de aritmetico de una lista
def suma_lista(x1):
    #devuelve el promedio aritmetico de una lista
    N=len(x1)
    promedio=sum(x1)/N
    return promedio

    
        
