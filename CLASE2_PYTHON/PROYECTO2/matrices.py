#crear un arreglo matricial
M1=[[10,20,30],[20,20,0],[10,10,10]]
Filas=len(M1)
Columnas=len(M1[0])
print(Filas,Columnas)
#REALIZAR LA SUMA DE LOS ELEMENOS DE LA MATRIZ M1
suma=0
for fila in range(Filas):
    for columna in range(Columnas):
      suma=suma+M1[fila][columna]
print(suma)