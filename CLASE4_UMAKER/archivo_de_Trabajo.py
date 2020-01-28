#import modulo
#Desde un modulo importar todo
from funciones import *
y=ESTADO
#Desde el modulo tkinter importar todo
from tkinter import *
#creación de un objeto para crear una aplicación
aplicacion=Tk()
#uso de su método geometry para indicarle la dimensión
aplicacion.geometry("400x400")
#uso de su metodo title para colocar un titulo
aplicacion.title("APLICATIVO CON PYTHON")
#crear una función para el boton encender
def turn_on():
    #mostrar mensaje en la shell de python cuando el boton fue presionado
    print("BOTON DE ENCENDER")
    #mostrar texto en la aplicación
    nombre=texto.get("1.0",END)
    with open(nombre[0:len(nombre)-1]+".txt","a") as archivo:
        archivo.write("CREANDO ARCHIVO DESDE TKINTER\n")
def turn_off():
    texto.delete("1.0",END)
    #función turn_off()
    print("BOTON APAGAR")
#Crear un boton
boton=Button(aplicacion,text="ENCENDER",command=turn_on)
boton.place(x=100,y=100)
#Crear un Label
etiq1=Label(aplicacion,text="BOTON N° 1")
etiq1.place(x=100,y=70)
#Crear otro boton
boton2=Button(aplicacion,text="APAGAR",command=turn_off)
boton2.place(x=200,y=100)
#Crear un label
etiq2=Label(aplicacion,text="BOTON N° 2")
etiq2.place(x=200,y=70)
#Crear un Text
texto=Text(aplicacion,width=20,height=2)
texto.place(x=110,y=130)
#Método que bloquea otros eventos
aplicacion.mainloop()
print("EL PROGRAMA HA FINALIZADO")