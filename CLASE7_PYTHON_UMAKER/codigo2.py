"""
uso del modulo numpy y manejo de la camara
"""
import numpy as np
import cv2
#--crear objeto que apunte a la camara
video=cv2.VideoCapture(0)
#método read()
while True:
    #--------imagen en escala BGR----------
    estate,frame=video.read()
    #--------CONVERTIR DE LA ESCALA BGR A ESCALA GRAY
    gris=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #--------REALIZAR UNA BINARIZACIÓN DE LA IMAGEN EN ESCALA DE GRIS
    umbral=120
    binaria=np.where( gris>=umbral,255,0)
    binaria=np.uint8(binaria)
    cv2.imshow("IMAGEN EN GRISES",gris)
    cv2.imshow("IMAGEN BINARIA",binaria)
    if cv2.waitKey(1)==ord("s"):
        #liberar el uso de la camara
        video.release()
        cv2.destroyAllWindows()
        break
print("---FIN DEL CODIGO----")