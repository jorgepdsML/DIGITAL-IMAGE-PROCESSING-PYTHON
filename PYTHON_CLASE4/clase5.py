import numpy as np
import cv2
#leer una imagen
imagen=cv2.imread("hola.png")

print(np.max(imagen))
#utilizar modulo numpy
dimen=np.shape(imagen)
#Numero de pixeles
Np=dimen[0]*dimen[1]*dimen[2]
print("NUMERO DE PIXELES",Np)
print("DIMENSIONES",dimen)
print("TIPO DE DATO DE LA IMAGEN",type(imagen))
input("PRESIONAR UN BOTON")
cv2.imshow("IMAGEN 1",imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()