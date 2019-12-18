#CREAR DICCIONARO CON LOS CAMPOS TE TEMPERATURA,HUMEDAD RELATIVA , LUGAR
tabla1=dict()
#crear listas dentro de cada campo de la tabla1
tabla1["temperatura"]=list()
tabla1["humedad relativa"]=list()
tabla1["lugar"]=list()
#IMPRIMIR LA TABLA
print(tabla1)
#realizar un bucle for
for i in range(2):
    v1=int(input("INGRESAR EL VALOR ASOCIADO A LA temperatura"))
    #indexar al campo de temperatura y agregar el elemento a la lista
    tabla1["temperatura"].append(v1)
    v2=int(input("INGRESAR EL VALOR ASOCIADO A LA humedad"))
    #inexar al campo de humeda relativa y agregar el elemento a su lista
    tabla1["humedad relativa"].append(v2)
    v3=input("INGRESAR EL VALOR ASOCIADO AL lugar")
    tabla1["lugar"].append(v3)
print(tabla1)
#REALIZAR UN RECORRIDO SOBRE LOS DICCIONARIOS MEDIANTE EL BUCLE FOR

for campos in tabla1:
    print(tabla1[campos],end=' ')
