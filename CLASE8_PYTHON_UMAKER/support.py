import numpy as np
import cv2
def deteccion_face(Igray,param1=None,param2=None):
    if param1==None or param2==None:
        param1,param2=1.3,5
    # crear el objeto
    faces_detect = cv2.CascadeClassifier(
        'C:\\Users\\pdsjo\\Desktop\\Desk_files\\CARPETA_CURSOS_PROYECTOS\\ARCHIVOS_JORGE\\CLASES_ORDENADAS\\PAPERSFORIRIS'
        '\\haarcascade_frontalface_default.xml')
    #realizar la detección de rostros ,
    faces=faces_detect.detectMultiScale(Igray,param1,param2)
    #se detecto alguna cara?
    if faces is not ():
        return faces
    else:
        return None