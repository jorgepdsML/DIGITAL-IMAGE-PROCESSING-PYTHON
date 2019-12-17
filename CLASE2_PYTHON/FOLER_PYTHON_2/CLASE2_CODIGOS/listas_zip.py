#uso de la funcion zip
val=[10,20,5,-10,6,20,30]
#N elementos de la lista
N=len(val)
#crear una lista con los indices de la lista anterior
ind=list(range(N))
#Crear una tupla con 4 elementos
tupla1=("matematica","ciencia","python","hola mundo")
#crear el objeto zip
zip1=zip(ind,val,tupla1)
for inde,valor,tuplaval in zip1:
    #imprimir indice y su valor
    print(inde,valor,tuplaval)
