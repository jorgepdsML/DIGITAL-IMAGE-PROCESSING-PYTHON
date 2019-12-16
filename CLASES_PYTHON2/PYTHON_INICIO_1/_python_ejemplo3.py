#lista x
x=range(0,9,1)
x=list(x)
#lista h
h=list(range(10,19,1))
#calcular el producto interno
if len(x)==len(h):
    producto_punto=0
    for posicion in range(len(x)):
        producto_punto=producto_punto+x[posicion]*h[posicion]
    print(producto_punto)
print("PROGRAMA HA FINALIZADO")
