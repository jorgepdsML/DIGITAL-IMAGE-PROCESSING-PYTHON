import numpy as np
import cv2
import os
#bgr
img=cv2.imread("imagen1.jpg")
#convertir a gris
gris=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#ecualizara el histograma
gris2=cv2.equalizeHist(gris)
#crear un objeto de la clase CascadeClassifier
faces=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#utilizara el método detectMultiScale
rostros=faces.detectMultiScale(gris2,1.2,5)
if rostros !=():
    print(rostros.shape,rostros.ndim)
    x,y=rostros[0,0],rostros[0,1]
    w,h=rostros[0,2],rostros[0,3]
    #se detecto un rostro
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
    #realizar un recorte de la region de interes
    region=img[y:y+h,x:x+w,:]
    #conseguir la ruta de trabajo actual
    ruta_base=os.getcwd()
    #SI NO EXISTE LA CARPETA PERSONA_A , LO CREAMOS
    if "PERSONA_Bq" not in os.listdir():
        os.mkdir("PERSONA_B")
    #ACCEDER A LA CARPETA PERSONA_A
    os.chdir("PERSONA_B")
    #GUARDAR LA IMAGEN DENTRO DE LA CARPETA PERSONA_A
    cv2.imwrite("izumi1.png",region)
    #REGRESAR A LA RUTA DESDE DONDE INGRESAMOS A LA CARPETAA PERSONA_A
    os.chdir(ruta_base)
    cv2.imshow("IMAGEN",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    cv2.imshow("IMAGEN", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

