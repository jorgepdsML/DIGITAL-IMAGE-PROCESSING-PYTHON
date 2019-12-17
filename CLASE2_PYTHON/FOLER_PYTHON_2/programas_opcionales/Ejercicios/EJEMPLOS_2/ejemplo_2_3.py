#Ingresamos la altura:
h = int(input("Ingrese la altura: "))

#Espacios vacios a partir de la altura ingresada:
v = int(h-1/2)

#Variable para el incremento de cantidad de
#asteriscos de manera impar:
n = 1

#Bucle de 'h' secuencias para al altura:
for i in range(h):
	print (" "*v+"*"*n)
	v -= 1
	n += 2
	
#Pausamos la consola esperando por un 'enter'
input()