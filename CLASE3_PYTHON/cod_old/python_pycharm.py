#importar el modulo
import time
#Crear un diccionario con el nombre diccionario
diccionario=dict()
print(type(diccionario))
#ingresar un valor desde la shell
key1=input("INGRESAR EL CAMPO ")
value1=input("INGRESAR EL VALOR")
diccionario[key1]=value1
print(diccionario)
#IMPRIMIR EL VALOR DE CAMPO key
print(diccionario[key1])
#DEFINIR UN DICCIONARIO MEDIANTE EL USO DE LLAVES

dict2={"TEMPERATURA":25,"HUMEDAD RELATIVA":80,"LUGAR":"salaverry"}
print(dict2)

#CREAR UNA LISTA
lista1=[10,20]
lista2=lista1.copy()
print("LISTA 1:",lista1)
lista2.append(30)
print("LISTA 1:",lista1)