#importar numpy como np
import numpy as np
a1=np.array([ [3,40,100],
              [1,240,100],
              [0,-5,20] ])
print("ARREGLO a1:",a1)
#calcular el maximo valor del arreglo a1
print("FORMA DEL ARREGLO a1",a1.shape)
print("DIMENSIONES DEL ARREGLO a1 es:",a1.ndim)
amax=a1.max(axis=1)
print("maximo valor es:",amax)
#uso del método argmax
argmax=a1.argmax(axis=1)
print("ARGUMENTO QUE HACE MAXIMO AL ARREGLO: ",argmax)
#función where
a2=np.where(a1>=50,255,0)
print("ARREGLO a2 :es ",a2)