#with -- as
#administración de contexto
#archivo=open("archivo_clase5.txt","a")
#crear un objeto llamado archivo mediante el uso del with
with open("archivo_clase5.txt","w") as archivo:
    #escribir datos en el archivo
    archivo.write("ESTAMOS UTILIZANDO EL with Y EL as\n hola mundo")
    #no se requiere pasarle el metodo close
