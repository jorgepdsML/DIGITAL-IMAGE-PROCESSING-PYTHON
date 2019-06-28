#SUSCRIBETE AL CANAL DE Jorge Miranda Redes Neuronales para ver videos de programacion en python y opencv para procesamiento digital d
# imagenes , inteligencia artificial , microcontroladores dspic30F, 33F y procesamiento digital de señales teorico y practico 


import numpy as np 
import cv2
#CREAR  OBJETO PARA LA ADQUISICION DE IMAGENES
video=cv2.VideoCapture(0) 
while   True:
    #METODO READ PARA LA LECTURA DE LAS IMAGENES DADOS POR EL OBJETO LLAMADO video
    ret,frame1=video.read()
    #RGB-GRISES 
    frame=cv2.cvtColor(frame1,cv2.COLOR_RGB2GRAY)
    #RECOMENDABLE REALIZAR UN PROCESO DE FILTRADO 
    #CONVERSION DE DATO DE TIPO ENTERO 8bit EN FLOTANTES
    frame_float=frame.astype(float)
    #KERNEL DE SOBEL
    Hsx=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    Hsy=np.transpose(Hsx)
    #BORDES  EN  LAS  DIRECCIONES  HORIZONTALES  Y  VERTICALES
    bordex=cv2.filter2D(frame_float,-1,Hsx)
    bordey=cv2.filter2D(frame_float,-1,Hsy)
     #CALCULO DE LA MAGNITUD DEL GRADIENTE 
    Mxy=bordex**2+bordey**2 #OPERACION PIXEL POR PIXEL
    Mxy=np.sqrt(Mxy)
    #NORMALIZACION
    Mxy=Mxy/np.max(Mxy)
    #SEGMENTACION
    mask=np.where(Mxy>0.1,255,0)
    mask=np.uint8(mask)
    cv2.imshow('BORDES',mask)
    k=cv2.waitKey(1)&0xFF
    if(k==ord('p')):
        print('ACABO EL PROGRAMA')
        break
video.release()
cv2.destroyAllWindows()  
     
    
     
    
    
    

    
 
