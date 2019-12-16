#archivo principal
#incluir un archivo externo
from funcion1 import *
#importar el modulo time
import time
#datetime
import datetime

c1=list(range(0,5,1))#list(range(5))
#utilizar funcion energia
e1=energia(c1)
#imprimir el valor
print(e1)
#funcion promedio arimetico
pa1=suma_lista(c1)
#imprimir el valor
print(pa1)
#esperar 2 segundos
time.sleep(2)
#imprimir lista
print(c1)
#variable t1
t1=datetime.datetime.now()
t1=str(t1)
print(t1)
