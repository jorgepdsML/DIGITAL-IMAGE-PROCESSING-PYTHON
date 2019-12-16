import time
#bool , True , False
#uso del bucle while
a=0
#colocar un tiempo de referencia
t1=time.time()
#miestra la condición sea verdadera , el bloque se sigue ejecutando
while True:
    #imprimir el valor de a 
    print(a)
    #aumentar la variable a en una unidad
    a=a+1
    time.sleep(1)
    if (time.time()-t1)>15:
        print("HAN PASADO 15 SEGUNDOS")
        break
  
    
print("FIN DEL PROGRAMA")
