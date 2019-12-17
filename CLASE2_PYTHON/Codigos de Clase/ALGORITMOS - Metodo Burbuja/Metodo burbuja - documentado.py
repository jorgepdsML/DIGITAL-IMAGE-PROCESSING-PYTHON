#Librerias a usar
import ast
import os
import time


#Solicitamos una entrada el cual sera (por asignacion automatica de python) una variable "string" pero tendra la forma de una variable tipo "Lista"
entrada = input("Ingrese la lista de numeros: ")

#Trasformamos esa variable "string" con forma de "lista" a una autentica lista
a = ast.literal_eval(entrada)

#La cantidad de iteraciones sera igual a la cantidad total de terminos menos 1, usamos la funcion "len()" para saber cuantos terminos tiene 
#nuestra lista ingresada
b = len(a)-1

#Bucle para efectuar las secuancias, en cada secuencia se resta 1 iteracion hasta llegar a cero, cuando esto pase, se saldra de la funcion "while"
while (b!=0):
	for i in range (0,b):
		if a[i]>a[i+1]:
			a[i],a[i+1] = a[i+1],a[i]
			os.system("cls")
			print (a)
			time.sleep(1)
	b = b-1   

#Borrar los datos anteriores de la pantalla
os.system("cls")


#Mostramos el resultado
print ("finalizado! ")    
print (a)

#Pausamos
input()