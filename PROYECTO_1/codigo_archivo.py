#CREAR ARCHIVO DE TEXTO EN PYTHON
import time
time.sleep(1)
#MODO ESCRITURA
texto="PYTHON PYTHON Y MANEJO DE ARCHIVOS"
#objeto para el manejo de archivo
archivo=open("holamundo.txt","w")
#metodo write
archivo.write(texto)
#metodo close
archivo.close()
input("PRESIONAR UN BOTON PARA CONTINUAR")
#MODO LECTURA
archivo=open("holamundo.txt","r")

dato=archivo.read()

archivo.close()

print(dato)
