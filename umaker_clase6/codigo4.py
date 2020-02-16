#IMPORTAR MODULOS NECESARIOS
import numpy as np
import cv2
from matplotlib import pyplot as plt
#---leer una imagen
I=cv2.imread("imagen.png")
#determinar la forma de arreglo
s1=I.shape
#mostrar las dimensiones
print("IMAGEN CON DIMENSIONES: ",s1)
#convertir a flotante
img=np.asarray(I,dtype=float)
r=img[:,:,0]#capa R
g=img[:,:,1]#capa G
b=img[:,:,2]#capa B
#--operacion de conversión de rgb a gray
gris=(0.299)*r + (0.587)*g+ (0.14)*b
#convertir de flotante a entero de 8 bits sin signo
gris=np.uint8(np.max(gris)*gris/255)
#UTILIZANDO OPENCV
gris2=cv2.cvtColor(I,cv2.COLOR_RGB2GRAY)
#determinar el histograma
histo=cv2.calcHist([gris],[0],None,[256],[0,256])
#incrementar el brillo
contraste=1.2
brillo=40
grisb=contraste*gris+brillo
grisb=cv2.equalizeHist(gris)
histo2=cv2.calcHist([grisb],[0],None,[256],[0,256])
cv2.imshow("IMAGEN RGB",I)
cv2.imshow("IMAGEN GRISES ORIGINAL",gris)
cv2.imshow("IMAGEN GRISES +BRILLANTE",grisb)
cv2.waitKey(0)
#cv2.destroyAllWindows()
plt.subplot(121)
plt.plot(histo)
plt.subplot(122)
plt.plot(histo2)
plt.show()
print("FIN DEL CODIGO")