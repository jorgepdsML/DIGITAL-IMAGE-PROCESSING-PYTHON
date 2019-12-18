#importando todas las funciones desde tkinter
from tkinter import *
from time import sleep
#crear una ventana (objeto)
ventana=Tk()
ventana.geometry("600x600")
#agregar un titulo a la interfa grafica
ventana.title("ESTO ES UNA INTERFAZ GRAFICA EN PYTHON")
#---------CREAR BOTONES EN LA INTERFAZ GRAFICA------------
def encender():
    print("EL BOTON 1 HA SIDO PRESIONADO")
def apagar():
    print("EL BOTON 2 HA SIDO PRESIONADO")
boton1=Button(ventana,text="ENCENDER",command=encender)
boton2=Button(ventana,text="APAGAR",command=apagar)
boton1.place(x=300,y=300)
boton2.place(x=200,y=300)
#bucle infinito para la interfaz grafica
mainloop()