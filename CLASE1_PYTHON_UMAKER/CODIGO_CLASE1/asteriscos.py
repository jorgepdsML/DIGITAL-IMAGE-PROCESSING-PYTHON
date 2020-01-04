"""
ESTE PROGRAMA ES PARA DIBUJAR UN TRIANGULO DE ASTERISCOS
"""
#pedir dato desde la shell de python
h=int(input("INGRESAR NIVEL: "))
#USO DEL FOR
for nivel in range(1,h+1,1):
    # print("N° de nivel: ", nivel)
    print((h - nivel) * " " + (2 * nivel - 1) * "*" + (h - nivel) * " ")
for nivel in range(h,0,-1):
    #print("N° de nivel: ", nivel)
    print((h-nivel)*" "+ (2*nivel-1)*"*"+(h-nivel)*" ")