from matplotlib import pyplot as plt
#define el tiempo
t=[0,1,2,3,5]
#define la temperatura
temperatura=[25,30,24,26,27]
humedad=[60,50,70,80,90]
#graficar
plt.subplot(221)
plt.plot(t,temperatura,color="blue")
plt.title("GRAFICO EN PYTHON")
plt.xlabel("tiempo")
plt.ylabel("temperatura")
plt.subplot(222)
plt.plot(t,humedad)
plt.title("GRAFICO EN PYTHON")
plt.xlabel("tiempo")
plt.ylabel("HUMEDAD")
plt.show()