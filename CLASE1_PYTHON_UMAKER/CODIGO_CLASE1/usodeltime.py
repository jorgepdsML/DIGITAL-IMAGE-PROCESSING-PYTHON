"""
uso del modulo time
"""
import time
#realizar un programa que dure solo 20 segundos y luego imprimir
#fin de codigo
#crear un objeto que haga referencia a un archivo de texto
archivo=open("umaker.txt","a")

t1=time.time()
while True:
    archivo.write("2020 \n")
    time.sleep(2)
    if (time.time()-t1)>=20:
        archivo.close()
        print("HA TRANSCURRIDO 20 segundos")
        break