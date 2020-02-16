"""
primer codigo de python clase 5

"""
class persona():
    #método de instancia
    def hablar(self,x):
        print("YO PUEDO HABLAR",x)
    def caminar(self):
        print("yo puedo caminar")
#---INSTANCIANDO NUEVOS OBJETOS---------
#primera instancia
o1=persona()
#segunda instancia
o2=persona()
#OBJETO.METODO()
#acceder al método hablar
o1.hablar("Y PROGRAMAR")
#accder al método caminar de objeto o2
o2.caminar()




