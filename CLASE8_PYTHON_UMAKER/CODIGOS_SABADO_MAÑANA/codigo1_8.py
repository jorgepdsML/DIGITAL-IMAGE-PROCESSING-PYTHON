#---IMPORTAR TODO DE TKINTER
from tkinter import *
from PIL import Image as pil_image
from PIL import ImageTk
import numpy as np
import cv2
#crear aplicación
api=Tk()
#utilizar el método geometry
api.geometry("500x500")
#establece un titulo en la interfaz grafica
api.title("INTERFAZ GRAFICA")
#----------------------------leer imagen con opencv BGR
img=cv2.imread("imagen1.jpg")
#-------------convertir imagen BGR en RGB
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img=cv2.resize(img,(340,340),interpolation=cv2.INTER_AREA)
#gris
gris=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#hsv
hsv=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
#convertir array en un objeto de la clase Image
imgt=pil_image.fromarray(img)
#convertir objet de la clase Image a la clase ImageTk
imgtk=ImageTk.PhotoImage(image=imgt)
#CREAR CANVAS
canvas1=Canvas(api,width=300,height=400)
canvas1.place(x=0,y=0)
#mostrar la imagen en el canvas
canvas1.create_image(170, 170, image=imgtk)
def rgb_change():
    global canvas1,imagen_nuevo
    canvas1.delete("all")
    #convertir imagen en escala rgb a la clase ImageTk
    imagen_nuevo=ImageTk.PhotoImage(pil_image.fromarray(img))
    #mostrar imagen en rgb
    canvas1.create_image(170,170,image=imagen_nuevo)
def gray_change():
    global canvas1,imagen_nuevo
    canvas1.delete("all")
    #mostrar imagen en gray
    # convertir la imagen escala de gris a la clase ImageTk
    imagen_nuevo = ImageTk.PhotoImage(pil_image.fromarray(gris))
    # mostrar imagen en rgb
    canvas1.create_image(170, 170, image=imagen_nuevo)
def hsv_change():
    global canvas1,imagen_nuevo
    canvas1.delete("all")
    #mostrar imagen hsv
    # convertir la imagen escala de gris a la clase ImageTk
    imagen_nuevo = ImageTk.PhotoImage(pil_image.fromarray(hsv))
    # mostrar imagen en rgb
    canvas1.create_image(170, 170, image=imagen_nuevo)

#objeto boton1 de la clase Button
label1=Label(api,text="RGB")
label1.place(x=450,y=30)
boton1=Button(api,text="OK",command=rgb_change,fg="black")
boton1.place(x=450,y=45)

label2=Label(api,text="GRAY")
label2.place(x=450,y=70)
boton2=Button(api,text="OK",command=gray_change,fg="black")
boton2.place(x=450,y=85)

label3=Label(api,text="HSV")
label3.place(x=450,y=110)
boton3=Button(api,text="OK",command=hsv_change,fg="black")
boton3.place(x=450,y=125)
#hacer uso del método mainloop
api.mainloop()
print("FIN DEL CODIGO")