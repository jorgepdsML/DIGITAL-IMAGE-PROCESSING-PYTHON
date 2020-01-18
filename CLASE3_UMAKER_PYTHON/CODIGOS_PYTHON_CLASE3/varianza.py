def media(x):
    #determinar si x es una lista
    if isinstance(x,list):
        suma=sum(x)
        promedio=suma/len(x)
        return promedio
    #x no es una lista
    else:
        return None
#definir una función llamada desviacion
def desviacion(x):
    #determinar si x es una lista
    if isinstance(x,list):
        u=media(x)
        suma=0
        for val in x:
            suma=suma+(val-u)**2
        #varianza de la lista x
        varianza=suma/len(x)
        #desviación standard de la lista x
        desvi=suma**(1/2)
        #retornar desviación standard, varianza
        return desvi,varianza
    else:
        None
#lista de prueba
lista=[1,0.8,0.9,1.1,1.2,1.3]
lista2=[10,1,0,-20,5,7,5000]
d,v=desviacion(lista)
d2,v2=desviacion(lista2)
print("DESVIACIÓN STANDAR",d)
print("VARIANZA",v)
print("DESVIACIÓN STANDAR",d2)
print("VARIANZA",v2)