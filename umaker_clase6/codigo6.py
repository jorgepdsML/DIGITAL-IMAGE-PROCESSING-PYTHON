"""import los modulos necesarios
"""
import numpy as np
import cv2
#crear objeto para el registro de la camara web
camara=cv2.VideoCapture(0)
Kernel=np.array([[-1,0,1],
                 [0,0,0],
                 [-1,0,1]])
while True:
    #estado,imagen
    estado,frame=camara.read()
    #convertir a gray
    gris=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # mostrar la imagen
    #REALIZAR LA ECUALIZACIÓN DEL HISTOGRAMA
    #INTENTAR ECUALIZAR LOS NIVELES DE INTENSIDAD
    gris2=cv2.equalizeHist(gris)
    #uso de un filtro gaussiano para eliminar el ruido
    gris2=cv2.GaussianBlur(gris,(3,3),1)
    cv2.imshow("IMAGEN ORIGINAL", np.uint8(gris2))
    # realizar la operación de convolución en 2D
    img2 = cv2.filter2D(gris2, -1, kernel=Kernel)
    #umbralizar la imagen img2
    bordes=np.where(img2>=20,255,0)
    cv2.imshow("IMAGEN DE SOLO BORDES", np.uint8(bordes))
    #usar el waitKey para esperar que un boton se presione
    if cv2.waitKey(1)==ord("t"):
        camara.release()
        cv2.destroyAllWindows()
        break
print("FINISH")