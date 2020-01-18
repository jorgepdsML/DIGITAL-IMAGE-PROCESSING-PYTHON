#definición de una función sin parametros  y que no retorne valor
def umaker_python():
    print("INICIANDO PYTHON")
    print("EN UMAKER")
    print("FIN DE LA FUNCIÓN")
#invocar a la función
#devolvera None
c=umaker_python()
print("valor que se ha retornado",c)
umaker_python()
#definición de una función que espere 2 parametros y que no retorne un valor
c=30
print("VARIABLE C AL INICIO",c)
def imprimir_mensaje(x,y):
    x=2*x
    y=2*y
    print("VARIABLE1: ",x)
    print("VARIABL2: ",y)
    c=60
    print("VARIABLE C DENTRO DE LA FUNCIÓN:",c)
print("VARIABLE C DESPUES DE LA FUNCIÓN")
a=20
b=30
imprimir_mensaje(a,b)

