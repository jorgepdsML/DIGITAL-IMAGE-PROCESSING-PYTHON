#la definción de funciones
def par_impar(x):
    #preguntar si el numero es impar
    if x%2==1:
        #el número fue impar , retornar mensaje impar
        return "impar"
    else:
        #el número fue par , retornar mensaje par
        return "par"
l1=[10,23]
#uso de la función map para aplicar una función sobre cada elemento
# de una lista
y=map(par_impar,l1)
#convertir el tipo de dato map a una lista
y=list(y)# [ , , , , ]
#imprimir el resultado
print(y)
