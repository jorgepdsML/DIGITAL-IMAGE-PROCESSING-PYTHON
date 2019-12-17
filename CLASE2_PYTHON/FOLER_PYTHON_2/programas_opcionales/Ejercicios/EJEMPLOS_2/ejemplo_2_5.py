#Ingresamos la base forzando al usuario a 
#ingresar un numero impar:
while True:
	b = int(input("Ingrese la extension de la base: "))
	if not(b%2 == 0):
		break
	print ("Ingrese un numero impar!")

#Espacios vacios (lado izquierdo del triangulo)
#Decrementa de 1 en 1 por cada linea
v = int((b-1)/2)

#Espacios vacios (interior del triangulo)
#Incrementa de 2 en 2 por cada linea
ev = 1

#Primer asterisco (superior al triangulo)
print (" "*v+"*")
v -= 1		

#Bucle 'for' para los lados del triangulo
for i in range(int((b+1)/2)-2):
	print (" "*v+"*"+" "*ev+"*")
	v -= 1
	ev += 2

#Linea de asteriscos final (inferior al triangulo)
#Verificamos si la base es 1  o  no  para  incluir
#este caso:
if b!=1:
	print ("*"*b)

#Pausamos en consola:
input()