#Resolvemos el problema mediante un
#doble bucle 'for'

#Ingreso de Altura:
h = int(input("Ingrese la altura: "))

#Ingreso del Lado:
l = int(input("Ingrese el lado: "))

#Efectuamos la graficacion:
for i in range(h):
	for i in range(l):
		print("*",end="")
	#Efectuamos un salto de linea:
	print()


#Pausamos la consola:
input()