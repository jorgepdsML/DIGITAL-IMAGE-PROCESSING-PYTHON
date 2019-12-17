#Basicamente para resolver este problema, efectuamos
#una comprobacion  de  'residuos'  con  cada  numero
#natural desde 1 hasta el mismo numero  mediante  un
#bucle 'for'.

#Ingresamos el numero natural:
n = int(input("Ingrese un numero natural: "))

#Buscamos los divisores con el  primer  bucle  'for'
#desde 2 hasta el mismo numero:
for i in range(2,n+1):
	#Si encuentra un divisor, verificamos si es primo.
	if n%i == 0:
		#Si su divisor es 2, es factor primo
		if i == 2:
			print (i)
		#Si su divisor es mayor que 2, hay que verificar
		else:
			for j in range(2,i):
				#verificamos si es divisible por algun numero
				#de 2 a i-1
				if i%j == 0:
					break
				#si no lo es, entonces tambien es primo
				if j== i-1:
					print (i)
			

#Esperamos por un 'enter' para cerrar
input()

