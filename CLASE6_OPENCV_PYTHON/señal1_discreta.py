from matplotlib import pyplot as plt
import numpy as np
#secuencia x1
x1=np.array([0,2,0,5,4,6])
N=np.size(x1)
#secuencias discretas
n=np.arange(N)
#secuencia x2
x2=np.array([1,-1,1,-1,0,2])
#operacion suma
x3=x1+x2
#operacion resta
x4=x1-x2
#realizar grafica con matplotlib
plt.subplot(221)
plt.stem(n,x1)
plt.title("SECUENCIA x1")
plt.xlabel("n")
plt.ylabel("x1[n]")
#--------------------------
plt.subplot(222)
plt.stem(n,x2)
plt.title("SECUENCIA x2")
plt.xlabel("n")
plt.ylabel("x2[n]")
#------------------------
plt.subplot(223)
plt.plot(n,x3)
plt.title("SECUENCIA x3")
plt.xlabel("n")
plt.ylabel("x3[n]")
#------------------------
plt.subplot(224)
plt.plot(n,x4)
plt.title("SECUENCIA x4")
plt.xlabel("n")
plt.ylabel("x4[n]")
plt.show()