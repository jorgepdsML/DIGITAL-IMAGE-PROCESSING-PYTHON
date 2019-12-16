"""
USO DEL BUCLE FOR Y SU DE LA FUNCIÓN range()
NECESARIO DEFINIR UN ELEMENTO ITERABLE COMO POR EJEMPLO UNA LISTA
"""
#definir una lista , l1
r1=range(0,10,1)
#convertir el range a lista
l2=list(r1)
#uso del bucle for
for a in l2:
    print(a,end=" ")
