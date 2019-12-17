#---------importar modulos necesarios---------
import numpy as np
import cv2
from matplotlib import pyplot as plt
#----------------------------------------------------
imagen=cv2.imread("hola.png")
#convertir espacio de color BGR - GRAY
igray=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
#ecualizar el histograma
iequ=cv2.equalizeHist(igray)
#MOSTRAR IMAGEN
cv2.imshow("grises",igray)
cv2.imshow("imagen ecualizada",iequ)
#ESPERAR A QUE SE PRESIONE UNA TECLA PARA SEGUIR EN EL FLUJO DE PROGRAMA

#calcular el histograma asociado a la imagen en escala de grises
histograma=cv2.calcHist([igray],[0],None,[256],[0,256])
histograma2=cv2.calcHist([iequ],[0],None,[256],[0,256])
cv2.waitKey(0)
#CERRAMOS LAS VENTANAS
cv2.destroyAllWindows()
#utilizar un umbral
umbral=80
umbral2=200
x=np.ones((1000))
x=umbral*x
y=np.linspace(0,100000,1000)
plt.subplot(121)
plt.plot(histograma)
plt.plot(x,y)
plt.title("HISTOGRAMA")
plt.xlabel("NIVEL DE INTENSIDAD")
plt.ylabel("NUMERO DE PIXELES")
plt.subplot(122)
plt.plot(histograma2)
plt.plot(x,y)
plt.title("HISTOGRAMA ECUALIZADO")
plt.xlabel("NIVEL DE INTENSIDAD")
plt.ylabel("NUMERO DE PIXELES")
plt.show()
print("SEGMENTACIÓN")
#realizar la segmentación
Iseg=np.where(igray>70,0,255)
Iseg2=np.where(iequ<umbral2 and iequ>umbral,0,255)
cv2.imshow("IMAGEN SEGMENTANDA 1",np.uint8(Iseg))
cv2.imshow("IMAGEN SEGMENTANDA 2",np.uint8(Iseg2))

cv2.waitKey(0)
cv2.destroyAllWindows()