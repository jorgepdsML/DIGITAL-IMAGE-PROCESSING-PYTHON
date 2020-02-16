from matplotlib import pyplot as plt
from matplotlib import animation as nm
def animacion(cont):
    x,y=[],[]
    #abrir archivo de texto
    a1=open("sensores.txt","r")
    for linea in a1:
        linea=linea[0:len(linea)-1]
        a,b=linea.split(',')
        x.append(float(a))
        y.append(float(b))
    ax1.clear()
    plt.plot(x,y)
    a1.close()
#crear un objeto Figure
figura=plt.figure()
ax1=figura.add_subplot(1,1,1)
ax1.set_title("GRAFICO1")
ax1.set_xlabel("EJE X")
ax1.set_ylabel("EJE Y")
#crear una objeto de la clase FuncAnimation
an1=nm.FuncAnimation(figura,animacion,interval=1000)
plt.show()