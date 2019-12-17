#importar el modulo ast
import ast
#ingresar tupla desde la shell de python
tupla=ast.literal_eval(input("Ingresar tupla"))
#Cantidad de elementos de la tupla

#crear un diccionario
diccionario={"nombre":"manuel","apellido":"diaz"}
print(diccionario["apellido"])
diccionario[4]=10
#creación de un diccionario 2
#Numero de elementos ingresador en la tupla
N=len(tupla)
diccionario2=dict()
for valor in range(N):
    diccionario2["var"+str(valor+1)]=tupla[valor]
    
print(diccionario2)
 
