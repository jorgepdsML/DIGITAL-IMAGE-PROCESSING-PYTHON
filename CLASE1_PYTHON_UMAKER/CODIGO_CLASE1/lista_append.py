"""
uso de lista y el metodo append
"""
#creando una lista
lista1=[10,20,30]
print("LISTA ANTERIOR: ",lista1)
#uso del metodo append
lista1.append(100)
print("LISTA DESPUES DEL append: ",lista1)

valor=lista1.pop(0)
print("LISTA DESPUES DEL pop: ",lista1)
print("EL VALOR QUE YA NO ESTA ES :" , valor)
