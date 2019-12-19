try :
    #pedir la variable N°1 desde la shell de python
    variable1=input("ingresar variable N° 1: ")
    #convertir el valor a entero
    variable1=int(variable1)
    #pedir la variable N°2 desde la shell de python
    variable2=input("ingresar variable N° 2 : ")
    #convertir el valor a entero
    variable2=int(variable2)
    #REALIZAR LA SUMA
    suma=variable1+variable2
    print(“la suma es de : ”, suma)
except:
    print("se encontró un error en el bloque try")     
