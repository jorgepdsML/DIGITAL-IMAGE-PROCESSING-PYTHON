"""
clase llamada circulo

"""
class circulo():
    #atributo de tipo clase
    n=0
    #constructor
    def __init__(self,radio,name):
        #crear atributo de instancia
        self.r=radio
        self.nombre=name
        print("SE HA CREADO OBJETO")
    def __str__(self):
        return "SOY UN OBJETO CON NOMBRE {}".format(self.nombre)
    #método de instancia
    def area(self):
        return 3.14*(self.r**2)
    #método que retorne el perimetro
    def perimetro(self):
        return 2*3.14*self.r
#instanciar un objeto
c1=circulo(4,"CIRCULO1")
print(c1)
#acceder al metodo area
print("area del circulo1 es: ",c1.area())
print("perimetro del circulo1 es ",c1.perimetro())
