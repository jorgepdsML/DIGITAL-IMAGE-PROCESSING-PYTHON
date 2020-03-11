name="imagen1.jpg"
import numpy as np
import cv2
import time
from matplotlib import pyplot as plt
#---leer la imagen con la secuencia BGR
img=cv2.imread(name)
#---convertir la imagen a escala de grises
gris=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#--calcular el histograma de la imagen en escala gris
histo1=cv2.calcHist([gris],[0],None,[256],[0,256])
print("FORMA",gris.shape,"N° pixeles",gris.size,"DIMENSIONES",gris.ndim)
cv2.imshow("IMAGEN ORIGINAL",gris)
#---Realizar una operación de pixel--
c=1
b=25
gris2=gris.copy()
t1=time.time()
for x in range(gris.shape[0]):
    for y in range(gris.shape[1]):
        #limite maximo 255
        if c*gris[x,y]+b>=255:
            gris2[x,y]=255
        #limite maximo 0
        elif c*gris[x,y]+b<=0:
            gris2[x,y]=0
        #dentro del rango
        else:
            gris2[x,y]=c * gris[x, y] + b
t2=time.time()
print("TIEMPO DE CALCULO ",int(t2-t1))
gris2=np.uint8(gris2)
histo2=cv2.calcHist([gris2],[0],None,[256],[0,256])
cv2.imshow("IMAGEN MODIFICADA",gris2)
cv2.waitKey(0)
#-----------LUEGO DEL waitKey GRAFICOS LOS HISTOGRAMA EN UN SUBPLOT
plt.subplot(121)
plt.plot(histo1)
plt.xlabel("NIVEL DE INTESIDAD")
plt.ylabel("NÚMERO DE PIXELES")
plt.title("HISTOGRAMA 1")
plt.subplot(122)
plt.plot(histo2)
plt.xlabel("NIVEL DE INTESIDAD")
plt.ylabel("NÚMERO DE PIXELES")
plt.title("HISTOGRAMA 2")
plt.show()
#-----------------------------------