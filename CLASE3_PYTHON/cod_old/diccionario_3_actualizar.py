#definir una función llamada actualizar_diccionario(diccionario,lista1,lista2)
#variable global y entero
x=10
print("variable x: ",x)
def suma(a,b):
    global x
    x=25
    print("variable x: ",x)
    return  a+b+x
#llamar a la función
l=suma(10,20)
#print("imprimir la suma ",l)
print("variable x : " ,x)
#-----------------función actualizar_diccionario----------
#--------------------------------------------------------
def actualizar_diccionario(dic1,lista1,lista2):
    dic1["temperatura"]=lista1
    dic1["presión"]=lista2
#-------------------------------------------------------
dic1=dict()
dic1["temperatura"]=list()
dic1["presión"]=list()
print("diccionario vacio: ",dic1)
actualizar_diccionario(dic1,[10,20,30,40,50],[100,200,300,400,500])
print("diccionario con datos:",dic1)
#--------------------------------for campo in diccionario:------------
for campo in dic1:
    #acceder a la lista asociado al campo1
    l1=dic1[campo]
    #numero de elementos
    N1=len(l1)
    #crear una variable
    suma=0
    for i in range(N1):
        suma=l1[i]+suma
    suma=suma/N1
    print("PROMEDIO ARITMETICO DEL CAMPO "+campo,suma)
