#uso de tuplas y los metodos count e index y manejo de diccionarios
#crear una tupla
import ast
import sys
#crear una lista
lista1=[10,20,30,40]
#tupla1
tupla1=(10,20,30,40)
#encontrar  la cantidad de veces que se repite 40 en la tupla
n40=tupla1.count(40)
print("N veces:",n40)
p40=tupla1.index(40)
print("Indice: ",p40)
#LISTA
print("LISTA ",lista1,sys.getsizeof(lista1))
#TUPLA
print('TUPLA',tupla1,sys.getsizeof(tupla1))

