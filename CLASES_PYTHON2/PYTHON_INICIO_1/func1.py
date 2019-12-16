"""
reutilizar las funciones en un modulo llamado funciones.py
"""
#importar el modulo tkinter
from tkinter import *
vent=Tk()
vent.geometry("500x500")
#crear un boton
def encender():
    print("ENCENDER")
    
b1=Button(vent,text="ON",command=encender)
b1.place(x=200,y=200)
vent.mainloop()

