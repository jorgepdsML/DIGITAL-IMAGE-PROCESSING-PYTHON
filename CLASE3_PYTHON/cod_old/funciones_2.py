#definir una función que reciba 2 argumentos y que pueda crear un diccionario
#con los 2 argumentos como campos (key) y en cada campo , crear una lista vacia
#funcion con nombre crear_diccionario
def crear_diccionario(campo1,campo2):
    #crear diccionario vacio
    diccionario=dict()
    #crear un campo con el nombre campo1 y una lista vacia
    diccionario[campo1]=list()
    #crear un campo con el nombre campo2 y una lista vacia
    diccionario[campo2]=list()
    return diccionario
#--------------------------------------

dic1=crear_diccionario("temperatura","presion")
print("el diccionario se ha creado correctamente")
print(dic1)
print(dic1.items)
#---crear una función que reciba un diccionario y que retorne un diccionario
#con los elementos insertados mediante el uso de 2 listas
print("FUNCIONA CREAR asignar_listas")
#--------------------------------------------
def asignar_listas(diccionario,lista1,lista2):
    #crear un diccionario dict2
    dict2=dict()
    #determinar el número de campos
    N_campos=len(diccionario)
    dict2['temperatura']=lista1
    dict2['presion']=lista2
    return dict2
#-------------------------------------------------
l1=[10,20,30,25]
l2=[60,70,50,60]
print("CREAR NUEVO DICCIONARIO CON LOS ELEMENTOS ALMACENADOS")
diccionario2=asignar_listas(dic1,l1,l2)
print(diccionario2)
#--------------------------------------------------------------



