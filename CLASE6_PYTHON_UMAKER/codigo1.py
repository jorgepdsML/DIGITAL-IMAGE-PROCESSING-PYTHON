import numpy as np
l1=np.linspace(0,200,1000)
print(l1.shape)
#crear un objeto del tipo ndarray
a1=np.array([1,2,4.0])
a2=np.array([[2,4],
             [5,6]])
#utilizar el atributo llamado ndim
print("DIMENSION ES: {}".format(a1.ndim))
print("FORMA DE ARREGLO {}".format(a1.shape))
print("DIMENSION ES: {}".format(a2.ndim))
print("FORMA DE ARREGLO {}".format(a2.shape))
#acceder a toda la primera fila
f1=a2[0][:]
print(f1)
print("DIMENSION ES: {}".format(f1.ndim))