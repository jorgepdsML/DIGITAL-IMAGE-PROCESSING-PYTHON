#Usamos un bucle 'for' para resolver el problema

for i in range(2000,3201):
	if (i%7==0) and not(i%5==0):
		print (i)


#Esperamos por una tecla para cerrar la consola de python
input()