class point():
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def coordenada(self):
        print(self.x,self.y)
    def __add__(self, other):
        x=self.x+other.x
        y=self.y+other.y
        return (x,y)
    def __call__(self,*args):
        suma=0
        for val in args:
            suma=suma+val
        return suma
#instanciando un nuevo objeto
a1=point(10,10)
#llamando a la función call
d=a1(100,200,1000,500,1000)
print(d)