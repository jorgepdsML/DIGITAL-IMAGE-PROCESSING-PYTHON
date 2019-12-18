#uso del modulo datetime
import datetime
import time
#tiene el metodo now
fecha=datetime.datetime.now()
#convertir datetime a string
fecha=str(fecha)
#obtener el tamaño del string
N=len(fecha)
#obtener un nuevo strng
fecha_actual=fecha[0:19]
print(fecha_actual)
#diccionario
diccionario={"temperatura":[],"Fecha":[]}
diccionario["temperatura"].append(40)
fecha=datetime.datetime.now()
fecha=str(fecha)
N=len(fecha)
fecha_actual=fecha[0:19]
diccionario["Fecha"].append(fecha_actual)
print(diccionario)
time.sleep(4)
diccionario["temperatura"].append(35)
fecha=datetime.datetime.now()
#convertir datetime a string
fecha=str(fecha)
#obtener el tamaño del string
N=len(fecha)
#obtener un nuevo strng
fecha_actual=fecha[0:19]
diccionario["Fecha"].append(fecha_actual)
print(diccionario)