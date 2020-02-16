"""import los modulos necesarios
"""
import numpy as np
import cv2
#crear objeto para el registro de la camara web
camara=cv2.VideoCapture(0)
while True:
    #estado,imagen
    estado,frame=camara.read()
    #convertir a gray
    gris=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # mostrar la imagen
    cv2.imshow("IMAGEN ORIGINAL", gris)
    #REALIZAR LA ECUALIZACIÓN DEL HISTOGRAMA
    #INTENTAR ECUALIZAR LOS NIVELES DE INTENSIDAD
    gris2=cv2.equalizeHist(gris)
    #umbralización mediante el algoritmo de otsu
    umbral,segment=cv2.threshold(gris2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    print("UMBRAL ENCONTRADO ES :",umbral)
    cv2.imshow("IMAGEN SEGMENTADA", segment)
    #usar el waitKey para esperar que un boton se presione
    if cv2.waitKey(1)==ord("t"):
        camara.release()
        cv2.destroyAllWindows()
        break
print("FINISH")