#uso de bloque try-except
try:
    import buenosdias
    a=float(input("INGRESAR UN VALOR: ")) #ValueError
    #x = 20 + "30"  # TypeError
    b=float(input("INGRESAR OTRO VALOR: "))
    print("LO QUE SE INGRESO ES:",a,b)
    c=a/b
    print(c)
except ModuleNotFoundError:
    print("ERROR POR IMPORTAR UN MODULO")
except ValueError:
    print("ERROR AL CONVERTIR DE STRING A FLOTANTE : ERROR TIPO ValueError")
except TypeError:
    print("SE DETECTO UN ERROR DE TIPO TypeError")
except ZeroDivisionError:
    print("ERROR DE DIVISIÓN DE UN NÚMERO POR CERO: ZeroDivision Error")
except:
    print("ERROR DESCONOCIDO EN EL BLOQUE TRY")
#se ejecuta si en caso hay o no hay un error el bloque try
finally:
    print("BLOQUE FINALLY EN EJECUCIÓN")
