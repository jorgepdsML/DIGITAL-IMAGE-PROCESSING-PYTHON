#crear una lista y uso de la palabra reservada break
lista=list(range(10))
#realizar un recorrido sobre la lista
for it in lista:
    if it==5:
        print("se ha ejecutado el break")
        break
    print(it)
