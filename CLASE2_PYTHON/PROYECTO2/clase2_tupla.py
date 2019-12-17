import sys
#LISTA Y TUPLA
lista1=[20,0,5]
#TUPLA
tupla1=(20,0,5)
#modificar el elemento 0 de la lista 1 la tupla tupla1
#lista1[0]=200
print(lista1)
#tupla1[0]="buenos dias"
print(tupla1)
#función len
N1=len(lista1)
N2=len(tupla1)
print(N1,N2)
#modulo.funcion
t1=sys.getsizeof(lista1)
t2=sys.getsizeof(tupla1)
print("cantidad en bytes de la lista 1 ",t1,"cantidad en bytes de la tupla1",t2)