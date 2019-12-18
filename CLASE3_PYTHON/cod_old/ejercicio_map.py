#definir una lista
#lista de elementos desde el cero hasta el 20
import time
def funcion_mat(x):
    #0<=x<=5
    if 0<=x and x<5:
        y=x
    elif(x>=5):
        y=x**2
    else:
        y=abs(x)+2*x
    #retornar el valor de y
    return y
#------------------usar la función map --------------------
lista_x=[-10,0,2,10,20]
y=map(funcion_mat,lista_x)
print("clase del objeto y:",type(y))

for valor in lista_x:
    print(valor,end=" ")
print("\n")
#crear una lista2
lista2=list()
#---------------acceder a cada elemento del objeto map ----------
#agregarlo a una lista llamada lista2 mediante el metodo append
for valor in y:
    lista2.append(valor)
    print(valor,end=" ")
print("\n")
#------------------------------------------------------
print("LISTA2:",lista2)
str1="hola mundo"
#verificar si existe un elemento dentro de esa lista
verificacion=25 in lista2
verificacion2="hola" in str1
#------------------------------------------------------
print(verificacion)
print(verificacion2)
#-----------Creación de triangulo iscoceles------------
