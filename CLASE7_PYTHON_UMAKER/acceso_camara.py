import numpy as np
import cv2
#Crear un objeto de la clase VideoCapture(0)
video=cv2.VideoCapture(0)
#objeto para detectar caras
faces=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
estado=True
while estado==True:
    #leer las imagenes de la camara
    _,img=video.read() #BGR
    imgrg=img.copy()
    #Convertir la imagen BGR  a GRIS
    gris=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #Ecualizar el histograma de la imagen gris
    gris2=cv2.equalizeHist(gris)
    #utilizar el método detecMulstiScale()
    rostros=faces.detectMultiScale(gris2,1.3,5)
    #cuando es tupla vacias , no hay caras
    if rostros != ():
        #solo si hay un rostro
        if rostros.shape[0] == 1:
            # acceder a cada rostros
            for x, y, w, h in rostros:
                # graficar rectagulo
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
                # imagen solo rostro (recorte del rostro)
                img_rostro = img[y:y + h, x:x + w, :]
                gris_rostro=gris[y:y+h,x:x+w]


        #cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    #LOCALIZAR UN OBJETO , CARAS
    cv2.imshow("IMAGEN ORIGINAL",img)
    cv2.imshow("IMAGEN GRIS",gris)
    cv2.imshow("IMAGEN ECUALIZADA",gris2)
    #esperar a la letra p para ejecutar el bloque if
    if cv2.waitKey(1)==ord("p"):
        #guardar imagen
        if img_rostro is not None:
            #img_rostro=cv2.resize(img_rostro,(224,224),interpolation=cv2.INTER_AREA)
            cv2.imwrite("jorge0.png",img_rostro)
        video.release()
        cv2.destroyAllWindows()
        estado=False
print("FIN DEL CODIGO")
