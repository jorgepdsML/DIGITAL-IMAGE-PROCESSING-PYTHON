'''
Para resolver este problema, verificaremos el  residuo  de
dividir el numero ingresado por los naturales de '2' hasta
'n-1', si en alguno de este calculo  del  residuo  resulta
igual a cero, entonces no es un primo, caso contrario,  si
en ninguno es cero, entonces si es un primo.  Haremos  uso
del bucle 'for'.
'''

n = int(input("Ingrese un numero natural: "))

for i in range(2,n):
	if n%i == 0 or n == 2:
		print ("El numero no es primo, es divisible por:",i)
		break
	if i == n-1:
		print ("El numero es primo!")

#Incluimos el caso n = 2:
if n == 2:
	print ("El numero es primo!")
elif n == 1:
	print ("El numero 1 no es primo!")

input()