
#Ingresamos el texto a analizar
texto = "en el amanecer al quinto dia"

#Tenemos nuestra variable de referencia
#para cada letra
base = 0

#Efectuamos un bucle 'for' con una variable
#tipo set la cual elimina elementos repetidos
#de la variable 'texto'
for i in set(texto):
	#Obviamos el caso donde analice el
	#espacio vacio:
	if i != " ":
		print (i+" - ",end="")	
		#Efectuamos el conteo:
		for j in texto:
			if j == i:
				base += 1
		print (base)
		base = 0 

#Hacemos una pausa en consola.			
input()	