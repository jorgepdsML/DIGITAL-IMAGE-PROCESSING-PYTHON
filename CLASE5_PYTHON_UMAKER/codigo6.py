"""
script que permite convertir de un objeto de python a un flujo de bytes
"""
import pickle,time
import numpy as np
l1=np.array([[1,2],[0,1]])
#convertir la lista a flujo de bytes
b1=pickle.dumps(l1)
#guardar la variable b1 en un archivo binario
a1=open("info","wb")
a1.write(b1)
a1.close()
