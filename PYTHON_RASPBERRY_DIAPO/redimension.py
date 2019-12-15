#cambiar la dimension de la imagen
import numpy as np
#importar la libreria opencv 
import cv2
img=cv2.imread("imagen1.png")
#encotrar las dimensiones de la imagen
dimension=np.shape(img)
print(dimension)
#utilizar el metodo resize
imgr=cv2.resize(img,(500,500),interpolation=cv2.INTER_AREA)
dim2=np.shape(imgr)
print(dim2)
#en formato png 
cv2.imshow("HOLA MUNDO",imgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
