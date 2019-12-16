"""
DEFINIR TIPO DE DATOS COMPLEJO
"""
import math
import cmath
c1=3+4j
c2=complex(3,4)
#magnitud abs
m1=abs(c2)
p1=cmath.phase(c2)
p1=180*p1/math.pi
print(m1,p1)
#definir una lista de numeros complejos
x=list()
x.append(c1)
x.append(c2)
print(x)

#utilizar bucle for
a=[10,20,60,50]
b=[30,40,50]
for v1,v2 in zip(a,b):
    print(v1,v2)
for indice,valor in enumerate(a):
    print(indice,valor)
