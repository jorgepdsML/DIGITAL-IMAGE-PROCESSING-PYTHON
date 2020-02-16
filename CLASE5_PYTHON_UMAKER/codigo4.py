"""
SCRIPT NUMERO 4 , MANEJO DE CLASES Y HERENCIAS
"""
class clase1():
    #constructor
    def __init__(self,n,c):
        self.name=n
        self.ciudad=c
    def mi_nombre(self):
        print("mi nombre es: {} ".format(self.name))
    def estoy_en(self):
        print("esto en : {} ".format(self.ciudad))
c1=clase1("jorge","umaker")
print(dir(c1))
c1.mi_nombre()
class clase2(clase1):
    #overriding
    def __init__(self,n,c,carr):
        clase1.__init__(self,n,c)
        self.profesion=carr
    def mi_carrera(self):
        print(self.profesion)
c2=clase2("jorge","umaker","python")
c2.mi_carrera()
