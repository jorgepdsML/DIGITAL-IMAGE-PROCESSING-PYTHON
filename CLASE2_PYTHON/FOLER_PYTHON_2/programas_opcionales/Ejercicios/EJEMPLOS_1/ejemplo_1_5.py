#Basicamente para resolver este problema, efectuamos
#una comprobacion  de  'residuos'  con  cada  numero
#natural desde 1 hasta el mismo numero  mediante  un
#bucle 'for'.


n = int(input("Ingrese un numero natural: "))

for i in range(1,n+1):
	if n%i == 0:
		print (i)