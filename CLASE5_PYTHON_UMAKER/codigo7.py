import pickle
import numpy as np
a2=open("info","rb")
contenido=a2.read()
dato=pickle.loads(contenido)
a2.close()
print(dato,type(dato))