class neurona():
    c=0#atributo del tipo clase
    #metodos publicos
    def __init__(self,a,b):
        #definir dos atributos
        #atributos publicos
        self.nombre=a
        self.edad=b
    def mi_nombre(self):
        print("MI NOMBRE ES:",self.nombre)
        return self.nombre,self.edad
    def mi_edad(self):
        print("MI EDAD ES:" ,self.edad)
#crear objeto
n1=neurona("jorge",23)
nombre,edad=n1.mi_nombre()
print(nombre,edad)

