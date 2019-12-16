import cmath
#para la fase
#lista para la parte real
r1=list(range(0,9,1))
#lista para la parte imaginara
i1=list(range(0,9,1))
#funciones a utilizar
#math.pi
#cmath.phase(complejo) fase en radianes
#abs(complejo) magnitud
#1)
#definir una nueva lista de complejos llamada c1
#con parte real r1 y parte imaginaria i1
c1=list()
N1=len(r1)
N2=len(i1)
if N1==N2:
    #acceder de forma simultanea a la lista de parte real y parte imaginaria
    for real,imag in zip(r1,i1):
        #real almacena el numero real
        #imag almacena el numero imaginario
        c1.append(complex(real,imag))
print(c1)
#2)
#determinar el modulo de la lista compleja
#y almacenarlo en una lista llamada mod_c1
f=float(format(20.50003,".2f"))
 
mod_c1=list()
mod_c1.append(float(format((20.253),".1f")))
print(mod_c1)
#3)
#determinar la phase en grados de la lista compleja
#y almacenarlo en una lista llamada fas_c1
fas_c1=list()


