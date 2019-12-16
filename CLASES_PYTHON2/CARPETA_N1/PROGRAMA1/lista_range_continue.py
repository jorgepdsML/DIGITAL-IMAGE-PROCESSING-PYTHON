#crear una lista y uso de la palabra reservada continue
lista=list(range(20))
#realizar un recorrido sobre la lista
for it in lista:
    if (it%2!=0 and it%3==0):
        print("numero impar y multiplo del numero 3 : ",it)
        
