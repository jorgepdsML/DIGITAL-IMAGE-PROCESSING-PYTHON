"""
USO DE BUCLE FOR , funcion input , print
"""
h=input("INGRESAR ALTURA: ")
h=int(h)
#realizar un bucle for
for nivel in range(1,h+1,1):
    print((h-nivel)*" "+(2*nivel-1)*"*"+(h-nivel)*" ")

