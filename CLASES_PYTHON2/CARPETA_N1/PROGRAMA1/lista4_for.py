#uso de listas ,range, metodo append ,pop y bucle for
lista=list()
#uso del bucle for
N=input("Ingresar el numero de elementos")
print(N)
for it in range(int(N)):
    var=input("ingresar numero : ")
    lista.append(var)
    
input("presionar enter para sacar el ultimo elemento")
#uso del metodo pop para sacar el ultimo elemento de una lista y mostrarlo en la shell de python
for it in range(int(N)):
    print(lista.pop())
