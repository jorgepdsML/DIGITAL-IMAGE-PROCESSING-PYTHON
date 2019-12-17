#metodo de la burbuja para el ordenamiento de datos de forma ascendente
import ast
lista=ast.literal_eval(input("ingresar lista: "))
print(lista)
#numero de elementos de la lista
M=len(lista)
#la variable R define la cantidad de iteraciones en el primer recorrido
R=M-1
#si la cantidad de recorridos llega a ser cero , detenar el ordenamiento
while R!=0:
    #realizar el recorrido
    for ind in range(0,R):
        #Comparar el elemento anterior con el posterior
        if lista[ind]>lista[ind+1]:
            aux=lista[ind]
            lista[ind]=lista[ind+1]
            lista[ind+1]=aux
    #imprimir la lista en cada recorrido que se ha ejecutado
    #por cada recorrido disminuir en uno la cantidad de iteraciones
    R=R-1
print("METODO DE LA BURBUJA",lista)   
lista2=ast.literal_eval(input("ingresar lista2: "))
#ordenar lista en forma ascendente
lista2.sort()
#metodo reverse intercambia los valores extremos
lista2.reverse()
#realizar el ordenamiento mediante el metodo sort
print("METODO sort() de una lista",lista2)
        
