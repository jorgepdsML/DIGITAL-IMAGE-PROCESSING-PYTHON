import numpy as np
import cv2
from matplotlib import pyplot as plt
#utilizar indice de la camara
camara=cv2.VideoCapture(0)
#leer imagen de la camara
flag,imagen=camara.read()
#utilizar metodo de clase cv2
cv2.imshow("MENSAJE",imagen)
#almacenar la imagen
cv2.imwrite("hola.png",imagen)
#cv2.waitKey(0)
cv2.waitKey(0)
#limpiar ventanas de lo que se muetra en python
camara.release()
cv2.destroyAllWindows()