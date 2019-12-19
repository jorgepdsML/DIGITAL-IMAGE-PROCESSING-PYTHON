#uso de la función map
#definir una función
def duplicar(x):
    #devolver el valor duplicado
    return 2*x
l1=[0,1,2,10,50]
#uso de función duplicar
l3=duplicar(l1)
#uso la función map
l2=map(duplicar,l1) #0 1 2 10 50
#convertir a lista
l2=list(l2)
print("lista sin map",l3,"lista con map",l2)

