#importar modulos necesarios
#----------------------------------------------------
import numpy as np
import cv2
import time
#----------------------------------------------------
#crear objeto
camara=cv2.VideoCapture(0)
t1=time.time()
while True:
    if (time.time()-t1)>=30 or cv2.waitKey(1)==ord("q"):
        break
    #objeto.metodo()
    flag,imagen_actual=camara.read()
    #realizar un cambio del tipo de dato a flotante
    If=imagen_actual.astype(np.float)
    #acceder a cada capa de la imagen flotante If
    Ir = If[:,:,0]
    Ig = If[:,:,1]
    Ib = If[:,:,2]
    #realizar una operación de transformación de escala RGB a grises
    Ig=0.29*Ir+0.58*Ig+0.11*Ib
    #realizar la siguiente operación
    #I=contraste*I+brillo
    Ign=1.2*If+10
    #convertir de flotante a entero
    Ig=np.uint8(Ig)
    Ign=np.uint8(Ign)
    cv2.imshow("IMAGEN EN TIEMPO REAL1 ",np.uint8(If))
    cv2.imshow("IMAGEN EN TIEMPO REAL2 ",Ign)
camara.release()
cv2.destroyAllWindows()
