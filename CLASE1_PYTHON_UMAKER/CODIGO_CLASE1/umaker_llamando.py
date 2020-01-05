import sys
print(sys.argv)
print(sys.platform)
#segundo manera de importar funciones desde un modulo
#del modulo python_func importar todas las funciones
from python_func import *
#del modulo time import solo la funcion sleep
from time import sleep
print("INICIANDO CODIGO")
sleep(1)
umaker()
holamundo(10)
