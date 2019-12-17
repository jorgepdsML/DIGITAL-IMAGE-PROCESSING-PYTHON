

#Ingresamos el nombre:
nombre = input("Ingrese su nombre: ")

#Averiguamos la extension del nombre
ext = len(nombre)

#Creamos la  variable  de  la  linea superior e inferior:
s_i = "="*(ext+4)

#Creamos la  variable  de  la  linea del nombre:
lin_nombre = "= "+nombre+" ="

#Unimos los resultados en  un  unico 'String' con saltos de linea:
resultado = s_i+"\n"+lin_nombre+"\n"+s_i

#Imprimimos el resultado:
print (resultado)

#Pausamos la consola esperando por la tecla 'enter':
input()
