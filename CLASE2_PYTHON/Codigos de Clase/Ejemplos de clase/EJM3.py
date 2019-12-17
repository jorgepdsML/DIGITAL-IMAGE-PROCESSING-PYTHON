import functools
#Obtener el promedio de los elementos de la lista X
x = [16.2,19.6,17,11.25,14.72,16.13]
##################################################
suma = 0
for i in range(len(x)):
	suma += x[i]
promedio = suma/len(x)
##################################################
promedio2 = functools.reduce(lambda x,y:x+y,x)/len(x)

print (promedio)

print (promedio2)
