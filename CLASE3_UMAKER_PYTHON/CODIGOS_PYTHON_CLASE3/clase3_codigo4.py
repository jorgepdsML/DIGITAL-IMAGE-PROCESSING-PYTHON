l1=[2,3,4]
l2=l1.copy()
l1[0]=200
print("UBICACIÓN: ",hex(id(l1)),l1)
print("UBICACIÓN: ",hex(id(l2)),l2)
#uso de diccionario
diccionario={"x1":[],"x2":[],"x3":[]}
cont=0
print("DICCIONARIO AL INICIO ",diccionario)
while cont<3:
    a1=input("INGRESAR CAMPO1")
    a2=input("INGRESAR CAMPO2")
    a3=input("INGRESAR CAMPO3")
    diccionario["x1"].append(a1)
    diccionario["x2"].append(a2)
    diccionario["x3"].append(a3)
    cont=cont+1
print("DICCIONARIO AL FINAL ",diccionario)
#realizar la busqueda de la fila numero 2 del diccionario
listav=[]
for campos in diccionario:
    print(campos)
    listav.append(diccionario[campos][1])
print(listav)
