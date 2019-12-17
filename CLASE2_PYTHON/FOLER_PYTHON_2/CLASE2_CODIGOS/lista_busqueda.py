#busqueda de elementos en una lista y tupla
import ast
#Crear una lista desde la shell de python
lista=ast.literal_eval(input("INGRESAR UNA LISTA : "))
#buscar la cantidad de veces que se repite el numero 5
#crear una funcion llamada num_5

def num_5(x):
    #Numero de elementos de lista
    N=len(x)
    cont=0
    #realizar el recorrido sobre el numero 5
    for val in x:
        #encontrar el numero 5
        if val==5:
            cont=cont+1
    return cont
print(num_5(lista))
        
        
