#uso de numpy
import numpy as np
#crear un arreglo de 3D
a3=np.array([ [[1,1],[2,2] ],
              [[5,4],[0,2] ],
              [[5,2],[200,100] ]])
print("DIMENSIONES ES: ",a3.ndim)
print("FORMA DEL ARREGLO: ",a3.shape)
print("CANTIDAD DE PIXELES",a3.size)
#---ACCEDER A CADA CAPA DE LA IMAGEN a3------
r=a3[0][:][:]
g=a3[1][:][:]
b=a3[2][:][:]
#---gris------------------------------------
gris=0.299*r+0.587*g+0.14*b
print(gris)
