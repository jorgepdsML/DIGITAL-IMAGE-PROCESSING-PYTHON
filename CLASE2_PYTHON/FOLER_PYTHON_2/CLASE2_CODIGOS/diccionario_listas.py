#crear un diccionario de elementos definidos mediante unas listas
#tener en cuenta los metodos append , insert y pop de las listas
#Ingresar los campos asociado al diccionario
import ast
tupla_campos=ast.literal_eval(input("ingresar nombre de los campos"))
#crear el diccionario con los campos que ingresemos por la shell de python
diccionario=dict()
#identificar el numero de campos
N=len(tupla_campos)
for campos in tupla_campos:
    diccionario[campos]=list()
print(diccionario)
#asignar un conjunto de elementos al diccionario
lista=[2,10,11]
#insertar los elementos de la lista al diccionario
#acceder a un elemento y mediante el metodo append ,agregar un elemento
diccionario['var1'].append(2)
diccionario["var2"].append(10)
diccionario['var1'].append(2)
diccionario["var2"].append(10)
print(diccionario)
    
