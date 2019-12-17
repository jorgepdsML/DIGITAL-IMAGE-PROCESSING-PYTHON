#crear clase persona
class persona():
    #constructor , sirve como función de inicialización
    def __init__(self,n):
        self.nombre=n
    def hablar(self):
        print("YO PUEDO HABLAR")
    def caminar(self):
        print("YO PUEDO CAMINAR")
#INSTANCIAR OBJETOS
#objeto1
objeto1=persona("JORGE")
print(objeto1.nombre)
objeto1.hablar()
objeto1.caminar()
#objeto2
objeto2=persona("ORLANDO")
print(objeto2.nombre)
objeto2.caminar()
objeto2.hablar()
