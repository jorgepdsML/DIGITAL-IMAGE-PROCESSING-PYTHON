"""
CODIGO PARA CREAR UNA CLASE Y DEFINIR METODOS

"""
#clase ARRAY() que reciba como argumento una matriz
#método de instancia -> binarizar()
#método de instancia -> normalizar() maximo de una unidad
class ARRAY():
    def __init__(self,m1):
        #atributo de instancia
        self.M=m1
        #determinar la cantidad de filas
        self.Nf,self.Nc=len(self.M),len(self.M[0])
    def binarizar(self,umbral):
        M2=[]
        #crear matriz M2 que tenga la mismas filas que la matris de entrada
        for fi in range(self.Nf):
            M2.append([])
        #realizar recorrido sobre la matriz de entrada
        for r in range(self.Nf):
            for c in range(self.Nc):
                if self.M[r][c]>=umbral:
                    M2[r].append(1)
                else:
                    M2[r].append(0)
        return M2
class ARRAY2(ARRAY):
    #agregar un método a la clase ARRAY2
    def normalizar(self):
        print("FUNCIÓN NORMALIZAR")
m1=[[100,20],
    [30,20]]
#objeto creado
array1=ARRAY2(m1)
#utilizar el metodo binarizar
m2=array1.binarizar(80)
print(m2)
#metodo normalizar
array1.normalizar()




