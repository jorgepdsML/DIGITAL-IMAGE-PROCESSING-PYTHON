#para interactuar python y el sistema operativo
import os
#para determinar la fecha
import datetime 
#encontrar la ruta de mi archivo
ruta_p=os.getcwd()
print(ruta_p)
#crear una lista para almacenar los nombres de los usuarios
lista_usuarios=list()
#numero de usuarios
N=input("ingresar el numero de usuarios")
#convertir a entero 
N=int(N)
#para cada usuario
for it in range(N):
    usx=input("ingresar nombre y apellido : ")
    #determinar la fecha y hora de ingreso
    fecha=datetime.datetime.now()
    fecha=str(fecha)
    fecha=fecha[0:19]
    #agregar en la lista
    lista_usuarios.append(usx)
    file1=open("usuarios.txt","a")
    file1.write(lista_usuarios[it]+" "+fecha+"\n")
    file1.close()

#LEER ARCHIVO QUE HA SIDO CREADO
file1=open("usuarios.txt","r")
texto=file1.read()
#almacenar los nombres en una lista
lista_nueva=texto.split('\n')
file1.close()

fs=input("¿deseas abrir el archivo ?")
if fs=="si":
    os.system("usuarios.txt")
else:
    print("archivo cerrado")

