#uso de funciones y el keyword global
x=20
y=30
print("valor de x inicio",x)
def restar_alterado(a,b):
    #variable local dentro de la función
    v=a-b
    global x
    x=50
    print("valor de x dentro de la función",x)
    return v
c=restar_alterado(20,20)
print(c)
print("valor de x final",x)