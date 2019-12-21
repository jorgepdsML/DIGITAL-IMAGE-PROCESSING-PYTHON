import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig=plt.figure()
ax1=fig.add_subplot(1,1,1)
x1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,18]
x2 = [10,20,30,10,20,30,10,20,30,10,20,30,10,20,30,1,1,2,10]
N=len(x1)
def animar(i):
    print(i)
    if i<N:
        xar = []
        var = []
        for a in range(i-1):
            xar.append(x1[a])
            var.append(x2[a])
        ax1.clear()
        ax1.plot(xar, var)
        plt.xlim((0, 20))
        plt.ylim((0, 40))


an1=animation.FuncAnimation(fig,animar,interval=1000)
plt.show()