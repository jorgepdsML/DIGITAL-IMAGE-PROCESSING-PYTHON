#uso del elemento iterable range
#lista con 3 elementos
l1=["hola","buenos dias","labotec"]
#lista sin elementos
l2=list() # []
#copiar elementos de una lista a otra lista
#uso del metodo copy()
l3=l1.copy()
print(l3)
#determinar la ubicación en memoria
dir1=id(l1)
dir2=id(l3)
dir1_hex=hex(dir1)
dir2_hex=hex(dir2)
print("dirección 1",dir1_hex,"dirección 2 ",dir2_hex)

#uso del metodo appen()
l1.append("martes")
print(l3)
print("lista l2",l2)
#uso del bucle para asginar elementos de una lista l1 a una lista vacia l2
for valor in l1:
    l2.append(valor)
print("lista l2",l2)
