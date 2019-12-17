from time import sleep
import os
#conseguir ruta de este script
ruta=os.getcwd()
print("RUTA DE MI SCRIPT",ruta,type(ruta))
#CREAR UNA CARPETA LLAMADA carpeta1
#os.mkdir("carpeta1")
contenido=os.listdir()
print(contenido)
os.chdir("carpeta1")
archivo=open("hola.txt","w")
archivo.write("ESTOY EN LA CARPETA1")
archivo.close()
ruta1=os.getcwd()
print("RUTA ACTUAL",ruta1)
#REGRESAR AL DIRECTORIO ANTERIOR
os.chdir(ruta)
print("RUTA REGRESADA",os.getcwd())
