#definir una función que reciba una matriz y que determine su transpuesta
def transpuesta(x):
    #determinar la cantidad de filas
    Nf=len(x)
    #cantidad de columnas de la matriz x
    Nc=len(x[0])
    #crear una matriz mt
    mt=[]
    for filas2 in range(Nc):
        mt.append([])
    #acceder a cada fila de la matriz de entrada M
    for row in range(Nf):
        #acceder a cada columna de la matriz de entrada M
        for col in range(Nc):
            mt[col].append(M[row][col])
    return mt
M=[[1,2],[3,5],[0,0]]
N=transpuesta(M)
print("MATRIZ DE ENTRADA M: ",M)
print("MATRIZ TRANSPUESTA N: ",N)
