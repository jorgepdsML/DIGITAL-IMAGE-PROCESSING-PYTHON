"""
uso de funciones anidadas
"""
#decoradores
#función externa
def saludos():
    print("FUNCIÓN EXTERNA INVOCADA")
    #función anidada
    def despedida():
        print("FUNCIÓN ANIDADA INVOCADA")
    despedida()

    print("ACABANDO LA FUNCIÓN EXTERNA ")
saludos()
