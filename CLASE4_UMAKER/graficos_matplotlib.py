#importar pyplot de matplotlib
from matplotlib import pyplot as plt
#to , tf , N
def linspace(to,tf,N):
    razon=(tf-to)/N
    ls=[]
    for val in range(N):
        ls.append(to+val*razon)
    return ls
def relu(x):
    lr=[]
    for val in x:
        if val>=0:
            lr.append(val)
        else:
            lr.append(0)
    return lr
def escalon(l): # función escalón
    y=[] # lista vacia
    for val in l: # para cada valor que ingresa de la lista
        if val>=0: # condición verdadera
            y.append(1) #agregar un valor
        else:       #condición falsa
            y.append(0) #agregar otro valor
    return y
def logistic(g): # función logistica
    y=[]
    for x in g:   #  Función a desarrollar 1/(1+exp(-x))
        y.append(1/(1+(2.71**(-x))))
    return y
def sumafunciones(f1,f2):
    try:
        ls=[]
        for index in range(len(f1)):
            ls.append(f1[index]+f2[index])
        return ls
    except:
        print("ERROR EN LA FUNCIÓN")
        return None

t=linspace(-3,3,10)
y=relu(t)
#plot
plt.subplot(141)
plt.plot(t,y,color="green")
plt.title("FUNCIÓN RELU")
plt.xlabel("EJE X")
plt.ylabel("EJE Y")

y2=escalon(t)
plt.subplot(142)
plt.plot(t,y2)
plt.title("FUNCIÓN ESCALON")
plt.xlabel("EJE X")
plt.ylabel("EJE Y")
plt.ylim((0,2))
#función 3
y3=logistic(t)
#funcion suma y2+y3
y4=sumafunciones(y2,y3)
plt.subplot(143)
plt.plot(t,y3)
plt.title("FUNCIÓN LOGISTICA")
plt.xlabel("EJE X")
plt.ylabel("EJE Y")
plt.ylim((0,2))

plt.subplot(144)
plt.plot(t,y4)
plt.ylim((0,2))
plt.title("SUMA DE FUNCIONES")
plt.show()