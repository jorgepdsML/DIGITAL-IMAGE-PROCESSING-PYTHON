#import el modulo serial
#import serial

#crear una clase en PYTHON
class vehiculo():
    #DEFINIR METODO
    def avanzar(self):
        print("YO PUEDO AVANZAR")
    def detener(self):
        print("YO ME PUEDO DETENER")
#CREAR OBJETO 1, INSTANCIAR
toyota=vehiculo()
toyota.avanzar()
toyota.detener()

#CREAR OBJETO 2 , INSTANCIAR
nissan=vehiculo()
nissan.avanzar()
nissan.detener()
