#funciones anidadas 
def polinomio(a2,a1,a0):
    print("FUNCIÓN EXTERNA INVOCADA")
    def inner_function(x):
        val=a2*(x**2)+a1*x+a0
        return val
    return inner_function
f1=polinomio(0,2,1)
#utilizando la función f1 para x=0 hasta 3
for val in range(4):
    print(f1(val),end=" ")

