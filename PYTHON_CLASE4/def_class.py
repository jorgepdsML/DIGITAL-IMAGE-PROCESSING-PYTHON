#utilizar las definicion de clase
import numpy as np
#crear un objeto , instanciar un objecto
n1=np.array([1,2,3])
n2=np.array([[1,2],[3,4]])
#metodos del objeto n1 que pertenece a la clase numpy.ndarray
n3=n2.max()
#atributos del objeto n1 que pertenece a la clase numpy.ndarray
n4=n1.shape

print("maximo valor",n3,"la forma",n4)