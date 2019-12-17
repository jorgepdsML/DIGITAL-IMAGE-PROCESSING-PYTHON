#Desarrollamos este codigo acumulando valores
#e  imprimiendolos  usado  una  variable   de
#acumulacion con inicio igual a '0'.

base = 0

#Numero natural a ingresar:
variable_ingreso = int(input("Ingrese el numero natural: "))

#Bucle de suma acumulada:
for i in range(variable_ingreso+1):
	base += i
	print(base)

#Pausamos a la espera por un 'enter' para cerrar la consola
input()