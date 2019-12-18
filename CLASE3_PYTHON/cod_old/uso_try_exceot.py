#hacer uso del try y except
v1=input('INGRESAR UN NÚMERO')
v2=input('INGRESAR OTRO NÚMERO')
try:
    v1=int(v1)
    v2=int(v2)
    #REALIZAR LA DIVISION
    D1=v1/v2
    print("DIVISION",D1)
except:
    print("HA OCURRIDO UN ERROR EN EL BLOQUE try")