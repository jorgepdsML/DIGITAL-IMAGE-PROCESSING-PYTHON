#lista
l1=[7,10] , list
#tupla
t1=(10,100) , tuple
#range
r1=range(0,5,1) # 0 1 2 3 4  range
#definir un diccionario , key :value
diccionario={"temperatura":20,"humedad":60} # dict
#mostrar el diccionario y su tipo de dato
print(diccionario,type(diccionario))
#acceder al campo temperatura
print("temperatura",diccionario["temperatura"])
print("humedad",diccionario["humedad"])
#modificar el valor de cada campo
diccionario["temperatura"]=30
diccionario["humedad"]=100
print(diccionario)