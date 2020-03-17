#Written by jorge orlando miranda ñahui
import cv2
from tkinter import *
from PIL import Image as pilimg
from PIL import ImageTk
from support import deteccion_face
import time,os,glob
#----------Objeto para la interfaz grafica
api=Tk()
api.geometry("650x600")
api.title("APLICACIÓN PARA MANIPULACIÓN DE IMAGENES")
#--CREAR DIRECTORIO TRAINING
if "training" not in os.listdir():
    os.mkdir("training")
if "testing" not in os.listdir():
    os.mkdir("testing")
#variable globales
ESTADO=0
info=0
img=0
OK=False
#---funciones vinculados a cada boton de tkinter
def confirmar():
    global OK,canv
    # limpiar canvas
    canv.delete("all")
    #verificar que la imagen haya sido correcta
    if OK==True:
        print("REGISTRAR CORRECTAMENTE")
        #VERIFICAR SI ESTA SELCCIONA EL TRAINING O EL TESTING
        #LEER EL CONTENIDO DEL TEXTO

        persona=nombre.get(1.0,END).rstrip(" ")
        persona=persona.lower()
        persona=persona.rstrip("\n")
        print(len(persona))
        if var1.get()==True and var2.get()==False:
            actual=os.getcwd()
            print(actual)
            print(os.listdir())
            #acceder a training
            os.chdir("training")
            #crear nuevo directorio si no lo hay
            if not persona in os.listdir():
                os.mkdir(persona)
            #agregar las regiones de interes en el directorio
            if persona in os.listdir():
                actual2 = os.getcwd()
                os.chdir(persona)
                registros=glob.glob("*.png")
                #determinar si esta vacio
                if registros==0:
                    #comenzar desde 0
                    cv2.imwrite(persona+"0.png",cv2.resize(frame2,(224,224)))
                else:
                    #agregar desde la cuenta len(registros)
                    cv2.imwrite(persona+str(len(registros))+".png",cv2.resize(frame2,(224,224)))
            #regresar al directorio de trabajo
            os.chdir(actual)
        elif var1.get()==False and var2.get()==True:
            actual = os.getcwd()
            # acceder a training
            os.chdir("testing")
            # almacenar la imagen
            print("imagen en :", os.getcwd())

            if persona not in os.listdir():
                os.mkdir(persona)
            if persona in os.listdir():
                actual2 = os.getcwd()
                os.chdir(persona)
                registros = glob.glob("*.png")
                print("NUMERO DE REGISTRO ES:", len(registros))
                # determinar si esta vacio
                if registros == 0:
                    # comenzar desde 0
                    cv2.imwrite(persona + "0.png", cv2.resize(frame, (224, 224)))
                else:
                    # agregar desde la cuenta len(registros)
                    cv2.imwrite(persona + str(len(registros)) + ".png", frame)
            # regresar al directorio de trabajo
            os.chdir(actual)
        else:
            print("ERROR EN EL REGISTRO")
        OK=False
    else:
        print("INCORRECTO")
def continuar():
    global OK,canv
    # limpiar canvas
    canv.delete("all")
    OK=False
roi=0
def capturar():
    global canv,imgc,OK,roi,frame2,fils,cols
    #adquirir la imagen con la region de interes
    #determinar el numero de frames que sea de 1
    faces=deteccion_face(gris,param1=1.3,param2=5)
    if faces is not None:
        if faces.shape[0]==1:
            OK=True
            print("ROSTRO ENCONTRADO ROI")
            # extraer region de convergencia
            for (x, y, w, h) in faces:
                frame2=frame_ref[y:y+h,x:x+h,:]
                fils = np.shape(frame2)[0]
                cols = np.shape(frame2)[1]
                # realizar un escalamiento en todos los lados
                # convertir el array frame en imagen PIL
                imagee = pilimg.fromarray(cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB))
                # convertir a  PhotoImage
                imgc = ImageTk.PhotoImage(imagee)
                fils = np.shape(frame2)[0]
                cols = np.shape(frame2)[1]
                #limpiar canvas
                canv.delete("all")
                canv.create_image(0  + fils // 2, 0 + cols // 2, image=imgc)
                print(frame2.shape)
        elif len(faces > 1):
            print("EXISTEN MAS DE UNA CARA")
        else:
            print("POSICIONAR EL ROSTRO")
    else:
        print("ROSTRO NO ENCONTRADO")
xo,yo=500,50
#--------CANVAS
canv=Canvas(api,width=480,height=500)
#canv.create_rectangle(0,0,400,400)
canv.place(x=0,y=0)

#----------CHECKBOX PARA ESPECIFICAR EL DIRECTORIO TRAINING O TESTING
#-------TRAINING O TESTING


var1=BooleanVar()
Checkbutton(api, text="TRAINING", variable=var1).place(x=xo,y=50)

var2=BooleanVar()
Checkbutton(api, text="TESTING", variable=var2).place(x=xo,y=70)


#----------TEXTO PARA ESPECIFICAR EL NOMBRE DE LA PERSONA
nombre=Text(api,width=10,height=1)
nombre.place(x=xo,y=175)
label2=Label(api,text="NOMBRE DEL USUARIO")
label2.place(x=xo,y=150)
#---------Texto que muestra el Número de muestras por Persona
cuenta=Text(api,width=10,height=1)
cuenta.place(x=xo,y=225)
label3=Label(api,text="N° DE REGISTROS")
label3.place(x=xo,y=205)
#-------------------
#---------TEXTO MENSAJE AL USUARIO DE RESULTADOS-------
mensaje=Text(api,width=10,heigh=1)
mensaje.place(x=xo,y=260)
label4=Label(api,text="----MENSAJE----")
label4.place(x=xo,y=240)
#-------------BOTON PARA REALIZAR LA CAPTURA DE IMAGEN-------
capturar=Button(api,text="CAPTURAR",command=capturar,highlightbackground='#3E4149')
capturar.place(x=xo,y=320)
#------------BOTON PARA VALIDAR LA CAPTURA DE LA IMAGEN
continua=Button(api,text=" SI ",command=confirmar,fg="blue")
continua.place(x=xo-15,y=370)
#------------BOTON PARA NO VALIDAR LA CAPTURA DE LA IMAGEN
negacion=Button(api,text=" NO ",command=continuar,fg="black")
negacion.place(x=xo+45,y=370)
#-----------------------------------------
#Crear objeto VideoCapture
video=cv2.VideoCapture(0)
import numpy as np

while True:
    #BLOQUE EN MODO CONTINUO , STREAMING DEL VIDEO
    if OK==False:
        #MOSTRAR LOS FRAMES EN LA INTERFAZ GRAFICA
        # Leer frame por frame
        ret, frame = video.read()
        frame2=frame.copy()
        frame2=cv2.resize(frame2,(480,480),interpolation=cv2.INTER_AREA)
        frame_ref=frame2.copy()
        # Convertir a escala de grises
        gris = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        # ECUALIZAR HISTOGRAMA
        gris = cv2.equalizeHist(gris)
        # DETECTAR ROSTROS
        faces = deteccion_face(gris, param1=1.3, param2=5)
        if faces is not None:
            # determinar si hay caras
            for (x, y, w, h) in faces:
                frame2 = cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 0, 255), 1)
        # convertir el array frame en imagen PIL
        image = pilimg.fromarray(cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB))
        # convertir a  PhotoImage
        imgt = ImageTk.PhotoImage(image)
        fils = np.shape(frame2)[0]
        cols = np.shape(frame2)[1]
        canv.create_image(0 + fils // 2, 0 + cols // 2, image=imgt)
        try:
            # actualizar tareas
            api.update()
            # actualizar tareas
            api.update_idletasks()
        except:
            # LIBERAR LA CAMARA
            video.release()
            print("FIN CODIGO")
            break
    #BLOQUE EN MODO CAPTURA
    else:
        #SE ENCONTRO UNA CARA 
        canv.create_image(0 + fils // 2, 0 + cols // 2, image=imgc)
        try:
            # actualizar tareas
            api.update()
            # actualizar tareas
            api.update_idletasks()
        except:
            # LIBERAR LA CAMARA
            video.release()
            print("FIN CODIGO")
            break
