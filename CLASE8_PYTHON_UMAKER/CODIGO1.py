"""
CODIGO PARA CREAR UNA INTERFAZ GRAFICA
"""
from PIL import Image as pilmg
from PIL import ImageTk
from tkinter import *
import numpy as np
import cv2
#------sección para crear la interfaz-----
api=Tk()
api.geometry("520x520")
api.title("---INTERFAZ GRAFICA---")
#leer imagen en bgr
bgr=cv2.imread("imagen1.jpg")
#cambiar dimensiones de la imagen
bgr=cv2.resize(bgr,(240,240),interpolation=cv2.INTER_CUBIC)
#--------crear un objeto de la clase Image
imag=pilmg.fromarray(cv2.cvtColor(bgr,cv2.COLOR_BGR2RGB))
#------convertir la imagen a la clase ImageTk
imgtk=ImageTk.PhotoImage(imag)
#-------definir funciónes vinculados a los botones
def escala_gris():
    global c1,imag,imgtk
    #CONVERTIR A ESCALA DE GRIS LA IMAGEN bgr
    gris=cv2.cvtColor(bgr,cv2.COLOR_BGR2GRAY)
    #borrar el contenido anterior
    c1.delete("all")
    # --------crear un objeto de la clase Image
    imag = pilmg.fromarray(gris)
    # ------convertir la imagen a la clase ImageTk
    imgtk = ImageTk.PhotoImage(imag)
#-----añadir widgets a la interfaz grafica
#ETIQUETA FIJA
e1=Label(api,text="BOTON 1")
e1.place(x=400,y=265)
#BOTON1
b1=Button(api,text="ESCALA DE GRISES",command=escala_gris,fg="blue")
b1.place(x=400,y=300)
#TEXTO EDITABLE
t1=Text(api,width=10,height=2)
t1.place(x=380,y=350)
#Crear un canvas
c1=Canvas(api,width=400,height=300)
c1.place(x=0,y=0)
c1.create_image(120, 120, image=imgtk)
while True:
    try:
        #actualizar la interfaz grafica
        api.update()
        api.update_idletasks()
        #mostrar la imagen en el canvas (xo,yo,image=imagetk)
        c1.create_image(120, 120, image=imgtk)
    except:
        print("ERROR EN EL TRY")
        break
print("FIN DEL PROGRAMA")