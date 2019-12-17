#Resolvemos el problema mediante  un
#bucle 'for' multiplicando  en  cada
#secuencia del bucle por la variable
#'i' al simbolo a usar (asterisco).

#Ingreso de Altura:
h = int(input("Ingrese la altura: "))

for i in range(1,h+1):
	print ("*"*i)