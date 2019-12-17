#ingresar una lista por la shell de python
import ast
import time
x=ast.literal_eval(input("ingresar una lista de numeros : "))
def med_var(x):
    u=sum(x)
    N=len(x)
    #media del arreglo x
    u=u/N
    #varianza
    var=0
    #para cada valor del arreglo
    for val in x:
        var=(val-u)**2+var
    #dividir el numeros entre N
    var=var/N
    #desviación standar
    dev=pow(var,1/2)
    return u,var,dev
u,var,dev=med_var(x)
print("media del vector X : ",u)
print("Varianza del vector X:",var)
print("Desviación standard del vector X:",dev)
#crear una función de normalización
def normalizacion(x):
    #calculando la media y desvianción standard
    med,vari,devi=med_var(x)
    x2=list()
    for val in x:
        x2.append((val-med)/devi)
    return x2
x2=normalizacion(x)
u,var,dev=med_var(x2)
print("media del vector X2 : ",u)
print("Varianza del vector X2:",var)
print("Desviación standard del vector X2:",dev)

time.sleep(10)
