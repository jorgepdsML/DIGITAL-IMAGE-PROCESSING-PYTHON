

import numpy as np
import cv2
from matplotlib import pyplot as plt
camara=cv2.VideoCapture(0)
#definir umbral minimo y maximo
#AZUL PURO (0,0,255)
#--------------------UMBRALES PARA COLOR AZUL
#RGB
umin=(50,80,130)
#umin=(0,0,0)
#RGB
umax=(100,140,255)
#----------------------------
#VERDE PURO (0,255,0)

#uso del bucle while
while True:
    #frame almacena la imagen
    ret,frame=camara.read()
    #convertir de escala BGR a RGB
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    #crear una mascara
    mascara=cv2.inRange(frame,umin,umax)
    #realizar el proceso de segmentación
    frame2=cv2.bitwise_and(frame,frame,mask=mascara)
    cv2.imshow("IMAGEN SEGMENTADA",frame2)
    if cv2.waitKey(1)==ord("p"):
        break
camara.release()
cv2.destroyAllWindows()