lista=[1,-2,-10,4]
N=len(lista)
while(N!=0):
    for i in range(0,N-1):
        if(lista[i]>lista[i+1]):
            aux=lista[i]
            lista[i]=lista[i+1]
            lista[i+1]=aux
    N=N-1

        
