"""
en este programa se realizara el uso de listas y strings
lista=[valor1,valor2,valor3]
"""

lista1=[10,"HOLA MUNDO",20.25]
#len , devuelve la cantidad de elementos
N=len(lista1)
print("lista ",lista1,end=" ")
print("N de elementos ",N)
#ACCEDER AL PRIMER ELEMENTO
lista1[0]=100
l1=lista1[0]
print("PRIMER ELEMENTO DE LA LISTA",l1)
#CREAR UNA LISTA QUE TENGA OTRA LISTA y numeros enteros
#lista t1
t1=[[10,20],[30,40]]
#acceder al primer elemento
tt1=t1[1][1]
print(tt1)
