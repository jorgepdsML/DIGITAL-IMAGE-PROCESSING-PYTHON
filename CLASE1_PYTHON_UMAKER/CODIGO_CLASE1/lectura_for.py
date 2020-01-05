"""
uso del bucle para la lectura de archivo de texto
"""
import time
archivo=open("umaker.txt","r")
#hacer uso del bucle for para acceder linea por linea el documento
for linea in archivo:
    #acceder a todos los caracteres menos el ultimo
    print(linea[0:len(linea)-1])
    time.sleep(2)
archivo.close()