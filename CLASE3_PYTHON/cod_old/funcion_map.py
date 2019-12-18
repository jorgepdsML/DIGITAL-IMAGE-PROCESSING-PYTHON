#definir una funcion t=2*x
import time
def funcion_map(x):
    t=10*x
    return t
#llamar a la función funcion_map
tiempo=10
temp=funcion_map(tiempo)
print(tiempo,temp)
lista1=[0,10,20,30,40]
#recibir una función , elemento iterable
temp_l=map(funcion_map,lista1)
print("objeto map ", temp_l)
#iterar cada aelemento de la lista
for l1 in lista1:
    print(l1,end=' ')
print('\n')
#iterar a los elmentos del objeto temp_l
for i in temp_l:
    #imprimir cada valor del objeto map
    time.sleep(2)
    print(i,end=' ')
