#-------IMAGEN EN ESCALA BINARIA-------
import numpy as np
import cv2
#arreglo de 2D 241x241
img=np.zeros((241,241))
cv2.imshow("IMAGEN BINARIA",img)
#atributo shape (filas,columnas)
#DETERMINAR EL NÚMERO FILAS DE LA img
Nf=img.shape[0]#Número de filas
Nc=img.shape[1]#Número de columnas
cont=0
#realizar recorrido sobre  todas la filas
for a in range((Nf-1)//2,-1,-1):
    cont=cont+1
    #realizar recorrido sobre todas las columnas
    for b in range(Nc-2*cont,-1,-1):
        img[a,b]=255

#realizar el calculo de area
#acceder a las filas
Area=0
for x in range(Nf):
    for y in range(Nc):
        if img[x,y]==255:
            Area=Area+1
print("AREA DEL OBJETO EN PIXELS: ",Area)
print("RATIO DEL AREA CON RESPECTO AL TOTAL",np.round(100*Area/img.size))
cv2.imshow("IMAGEN BINARIA2",np.uint8(img))
#ESPERAR A QUE SE PRESIONE UNA TECLA PARA CONTINUAR
cv2.waitKey(0)
#CERRAR LAS VENTANAS
cv2.destroyAllWindows()