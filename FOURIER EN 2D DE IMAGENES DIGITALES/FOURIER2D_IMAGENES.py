#-------IMPORTAR NUMPY & OpenCV--------

import numpy as np
import cv2
#---LEER IMAGEN ----------
#ESPECIFICAR RUTA DONDE ESTA LA IMAGEN SI NO ESTA EN EL MISMO NIVEL DE DIRECTORIO
imagen=cv2.imread('open1.png')
Nf=512
Nc=512
#-----ESCALAMIENTO DE LA IMAGEN 
imagen=cv2.resize(imagen,(Nc,Nf))
#CONVERSIÓN A ESCALA DE GRISES uint8
i_gray=cv2.cvtColor(imagen,cv2.COLOR_RGB2GRAY)
#CONVERSIÓN A PUNTO FLOTANTE PARA REALIZAR OPERACIONES MATEMATICAS
i_grayd=np.float64(i_gray) 
#TRANSFORMADA DE FOURIER EN 2D
Fuv=np.fft.fft2(i_grayd)
Fuv=np.fft.fftshift(Fuv)
#OBTENER LA MAGNITUD DE LA TRANSFORMADA DE FOURIER DE LA IMAGEN 
Fuv_abs=np.abs(Fuv)
#ESPECTRO EN ESCALA LOGARITMICA
Fuv_log=20*np.log10(Fuv_abs)
#MOSTRAR IMAGEN EN ESCALA GRISES Y SU ESPECTRO DE FRECUENCIA
cv2.imshow("IMAGEN ORIGINAL",i_gray)
cv2.imshow("ESPECTRO DE FOURIER",np.uint8(255*Fuv_log/np.max(Fuv_log)))

#DISEÑO DEL FILTRO PASA ALTO IDEAL
#---------------------------------------------------------------------
F1=np.arange(-Nf/2+1,Nf/2+1,1)
F2=np.arange(-Nc/2+1,Nc/2+1,1)
[X,Y]=np.meshgrid(F1,F2)
D=np.sqrt(X**2+Y**2)
D=D/np.max(D)
#DEFINIR RADIO DE CORTE
Do=0.59
#Creación del Filtro Ideal en 2D
Huv=np.zeros((Nf,Nc))
#PRIMER CREAR EL FILTRO PASA BAJO IDEAL
for i in range(Nf):
    for j in range(Nc):
        if(D[i,j]<Do):
            Huv[i,j]=1
#CONVERTIR A PASA ALTO IDEAL
Huv=1-Huv
#----------------------------------------------------
cv2.imshow("FILTRO 2D PASA ALTO IDEAL",np.uint8(255*Huv))
#--------------------------FILTRADO EN FRECUENCIA
#-MULTIPLICACIÓN ELEMENTO A ELEMENTO EN EL DOMINIO DE LA FRECUENCIA
Guv=Huv*Fuv
#MAGNITUD
Guv_abs=np.abs(Guv)
Guv_abs=np.uint8(255*Guv_abs/np.max(Guv_abs))
cv2.imshow('ESPECTRO DE FRECUENCIA G',Guv_abs)
#---TRANSFORMADA INVERSA PARA OBTENER LA SEÑAL FILTRADA 
#IFFT2
gxy=np.fft.ifft2(Guv)
gxy=np.abs(gxy)
gxy=np.uint8(gxy)
#--MOSTRAR LA IMAGEN FILTRADA
cv2.imshow('IMAGEN FILTRADA',gxy)

cv2.waitKey(0)
cv2.destroyAllWindows()
