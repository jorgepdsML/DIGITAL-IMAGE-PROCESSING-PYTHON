import os
#(sistema operativo)
#obtener la ubicacion de este archivo python
#crear una carpeta carpeta_archivo
#os.mkdir("carpeta_archivo")
#acceder a esa carpeta
import time

os.chdir("carpeta_archivo")
ubicacion=os.getcwd()
#CREAR UN ARCHIVO DE TEXTO EN ESA CARPETA
#archivo=open("sensores.txt",modo)
#modo ="r"
#modo="w" , modo="a"
archivo=open("sensores.txt","w")
#determinar tiempo de referencia
t1=time.time()
while (time.time()-t1)<=5:
    archivo.write("BUENOS DIAS A TODOS  HOY ES DIA DOMINGO DEL 2019\n")
    time.sleep(0.5)
    
#cerrar archivo
archivo.close()
#ABRIR EL ARCHIVO EN MODO LECTURA
archivo=open("sensores.txt",'r')
for linea in archivo:
    print(linea)
    time.sleep(1)
archivo.close
