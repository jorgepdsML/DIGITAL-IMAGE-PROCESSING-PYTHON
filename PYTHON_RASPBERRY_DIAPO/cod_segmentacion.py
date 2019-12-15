#segmentar una imagen mediante el uso de un umbral
import numpy as np
import cv2
img=cv2.imread("imagen_r.png")
dim1=np.shape(img)
#convertir a escala de grises
igr=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#realizar la segmentacion
umbral=100 #nivel de intensidad
iseg=np.where(igr>umbral,255,0)
cv2.imshow("IMAGEN ORIGINAL",igr)
cv2.imshow("IMAGEN SEGMENTADA",np.uint8(iseg))
cv2.waitKey(0)
cv2.destroyAllWindows()
