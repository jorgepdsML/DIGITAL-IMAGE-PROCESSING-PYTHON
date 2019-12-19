#realizar una operación matematica
#colocar el codigo que posiblemente puede generar un error
try :
    n1 = float(input("INGRESAR NÚMERADOR : "))
    d1 = float(input("INGRESAR DENOMINADOR: "))
    #division
    c1=n1/d1
    print(c1)
#el bloque except se ejecuta cuando se encontro un error en el bloque try
#capturar error especifico
except ZeroDivisionError:
    print("INGRESAR UN DENOMINADOR DIFERENTE DE 0")
#capturar error especifico
except ValueError:
    print("CONVERSIÓN DE DATOS INCORRECTO")
#capturar cualquier tipo de error que se encontro en el bloque try
except:
    print("REVISAR EL BLOQUE TRY , SE ENCONTRO UN ERROR")
