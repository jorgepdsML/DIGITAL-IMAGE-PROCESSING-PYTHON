
#definir una función basica

#uso del decorador para modificar una función como argumento
def decorador(func):
    def funcion_inner(x):
        func(x)
        print(x)
    return funcion_inner
#una manera de utilizar el decorador
#foo=decorador(foo)
#foo(20)
@decorador
def foo(y):
    print("FUNCIÓN FOO")
foo(20)