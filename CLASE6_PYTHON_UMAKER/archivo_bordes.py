import numpy as np
import cv2
#utilizar la operación de convolución
img=cv2.imread("imagen.png")
#cambiar escala RGB a GRISES
grises=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
grises=cv2.equalizeHist(grises)
#cambiar a escala en punto flotante
grises_f=np.asarray(grises,dtype=float)
#definicón de un kernel
Kernel=np.array([[-1,0,1],
                 [0,0,0],
                 [-1,0,1]])
#realizar la operación de convolución en 2D
img2=cv2.filter2D(grises,-1,kernel=Kernel)
#mostrar la imagen
cv2.imshow("IMAGEN ORIGINAL",grises)
cv2.imshow("IMAGEN RESULTANTE",np.uint8(img2))
cv2.waitKey(0)
cv2.destroyAllWindows()
