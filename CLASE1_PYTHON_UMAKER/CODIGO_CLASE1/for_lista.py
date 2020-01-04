"""
uso de la listas y bucles for
"""
#lista ´para almacenar pares
l1=[]
#lista para almacenar numeros impares
l2=[]
#crear una lista1
lista1=[10,5,7,6,7,15,30,20]
#encontrar cantidad de numeros pares
#contador
cont=0
conti=0
for var in lista1:
    # uso del % para saber si es par o no
    if var%2==0:
        l1.append(var)
        #incrementar el contador
        cont=cont+1
    else:
        l2.append(var)
        conti=conti+1
print("CODIGO FINALIZO")
print("N° de numeros pares es igual a: ",cont)
print("N° de numeros impares es igual a :",conti)
print("LISTA ORIGINAL",lista1)
print("LISTA PAR:",l1)
print("LISTA IMPAR:",l2)