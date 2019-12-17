import time
#crear una lista de 5 elementos
lista=[30,10,5,-10,20]
#encontrar el maximo mediante el bucle for
v_max=lista[0]
t1=time.time()
#mediante bucle for
for it in lista:
    #comparar el valor con la referencia
    if it>v_max:
        #actualizar la variable v_max
        v_max=it
    
t2=time.time()
#uso de la función max
v_max_f=max(lista)
print(v_max,v_max_f)
 
        
    
