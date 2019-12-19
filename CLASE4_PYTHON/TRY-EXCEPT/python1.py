#Se hace el requerimiento de la altura del triángulo

h=input("Ingrese el altura del Triángulo Isósceles: ")
#Cambio de tipo de dato
h=int(h)

if(h>0):
    for i in range(1,h+1):
        r=i-1 #Le resta un uno al número que entra en el bucle para
            #darle forma a la serie e imprima solo números impares:
            # 2*r+1=i; donde r=i-1
        #Por el requerimiento de números impares coincide que el
        # # de espacios en blanco es acorde a la fila, es decir a la
        # altura ingresada y se obtendra de la resta de la altura menos
        # el contador
        num_espacios=h-i
        print(' '*num_espacios+(2*r+1)*"*")
else:
    print("Ingrese un parámetro correcto")
