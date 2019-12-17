import ast

x = ast.literal_eval(input("Ingrese una lista: "))
suma = 0
for i in x:
	suma = suma + i 

"""
for i in range(len(x)):
	suma = suma + x[i]
"""

promedio = suma/len(x)
print ("El promedio es:",promedio)
input()