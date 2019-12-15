#realizar semgnetacion por color
import numpy as np
import cv2
camara=cv2.VideoCapture(-1)
#rango minimo de color rojo
lw_rojo=(150,0,0)
lm_rojo=(255,12,100)
while True:
    f,imag=camara.read()
    imag=cv2.cvtColor(imag,cv2.COLOR_BGR2RGB)
    #crear una mascara
    mascara=cv2.inRange(imag,lw_rojo,lm_rojo)
    #realizar una operacion and
    iseg=cv2.bitwise_and(imag,imag,mask=mascara)
    if cv2.waitKey(1)==ord("t"):
        break
    cv2.imshow("IMAGEN SEGMENTADA",imag)
camara.release()
cv2.destroyAllWindows()