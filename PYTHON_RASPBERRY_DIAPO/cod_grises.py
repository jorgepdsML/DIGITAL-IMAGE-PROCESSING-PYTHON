import numpy as np
import cv2
img=cv2.imread("imagen_r.png")
dim1=np.shape(img)
#convertir a escala de grises
igr=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
dim2=np.shape(igr)
print(dim1,dim2)
cv2.imshow("IMAGEN RGB",img)
cv2.imshow("IMAGREN GRISES",igr)
cv2.waitKey(0)
cv2.destroyAllWindows()
#calcular el histograma
hist = cv2.calcHist([igr],[0],None,[256],[0,256])
from matplotlib import pyplot as plt
plt.plot(hist)
plt.show()
