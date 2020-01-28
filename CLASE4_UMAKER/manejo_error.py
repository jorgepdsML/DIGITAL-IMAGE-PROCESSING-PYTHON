#uso del bucle while y el bloque try-except
while True:
    try:
        a=float(input("INGRESAR VALOR :"))
        b=float(input("INGRESAR VALO2 :"))
        #realizar división entre los números
        c=a/b
        print("VALOR DE LA DIVISIÓN ES: ",c)
        print("SALIENDO DEL BUCLE WHILE, uso del break")
        break
    except:
        print("ERROR")
