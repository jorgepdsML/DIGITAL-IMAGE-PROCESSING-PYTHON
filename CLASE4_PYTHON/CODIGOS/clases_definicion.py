#uso de la definición de clases en python
#mediante el uso del constructor __init__
#para pasarle argumentos
class vehiculo():
    #constructor de la clase , metodo magico __init__
    def __init__(self,n):
        #definir un atributo
        self.marca=n
    def mi_marca(self):
        print("MI MARCA ES: ",self.marca)
    def avanzar(self):
        print("YO PUEDO AVANZAR")




#INSTANCIAR OBJETOS MEDIANTE 1 PARAMETRO ADICIONAL
toyota=vehiculo("TOYOTA")
nissan=vehiculo("NISSAN")
#ACCEDER AL METODO MI MARCA , QUE IMPRIMI LA MARCA DEL CARRO
toyota.mi_marca()
#ACCEDER AL ATRIBUTO marca del objeto toyota
print(toyota.marca)
nissan.mi_marca()