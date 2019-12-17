import numpy as np
import cv2
from matplotlib import pyplot
class operacion_imagenes():
    def __init__(self,I,nm="rgb_grises"):
        #atributo para saber que operación
        self.operacion=nm
        #atributo que denote a la imagen de entrada
        self.imagen=I
    #metodo para realizar la operación que se le ha pasado como argumento
    def realizar(self):
        if self.operacion=="rgb_grises":
            Imagf=self.imagen.astype(np.float)
            #realizar la operación de conversion de rgb a grises
            Ig=0.29*Imagf[:,:,0]+0.58*Imagf[:,:,1]+0.11*Imagf[:,:,2]
            #convertir de flotante a entero
            Ig=np.uint8(Ig)
            return Ig
        else :
            if self.operacion=="histograma":
                print("OPERACIÓN HISTOGRAMA")
#leer la imagen
Imagen=cv2.imread("hola.png")
#crear un objeto
ob1=operacion_imagenes(Imagen,"rgb_grises")
#utilizar metodo realizar
Imagen2=ob1.realizar()
cv2.imshow("IMAGEN RGB",Imagen)
cv2.imshow("IMAGEN GRAY",Imagen2)
cv2.waitKey(0)
cv2.destroyAllWindows()

