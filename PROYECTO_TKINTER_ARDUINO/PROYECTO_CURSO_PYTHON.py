from tkinter import *
import serial
from PIL import ImageTk,Image
interfaz=Tk()
#geometry()
interfaz.geometry("500x500")
#metodo title()
interfaz.title("PROYECTO ARDUINO Y PYTHON")
#CARGAR IMAGEN CON FORMATO png
load=Image.open("hola2.png")
#reducir el tamaño de la imagen
load=load.resize((100,100))
#CREAR OBJETO PARA MOSTRAR LA IMAGEN EN EL TKINTER
img=ImageTk.PhotoImage(load)
lugar=Label(image=img)
#posicionar la imagen dentro de la interfaz grafica
lugar.place(x=200,y=50)
#DEFINCIÓN DE CONSTANTES
Baudios=9600
Puerto="COM4"
Estado_registro=0
Estado_conexion=0
FLAGG=0
#CREAR objeto para la comunicación serial
puerto_serial = serial.Serial()
puerto_serial.timeout=3
#-definir funciones para cada boton
def conectar():
    global Estado_conexion,FLAGG,puerto_serial
    FLAGG=1
    print("CONEXIÓN HACIA EL ARDUINO")
    #REALIZAR CONEXIÓN CON LAS CONFIGURACIONES HECHAS
    try:
        puerto_serial.port=Puerto[:len(Puerto)-1]
        puerto_serial.baudrate=int(Baudios)
        print(Baudios,len(Baudios),Puerto,len(Puerto))
        puerto_serial.open()
        texto_con.delete(1.0, END)
        texto_con.insert(1.0, "CONECTADO")
        Estado_conexion=1
    except serial.SerialException:
        Estado_conexion=0
        puerto_serial.close()
        texto_con.delete(1.0, END)
        texto_con.insert(1.0, "ERROR EN LA CONEXIÓN")
    except :
        Estado_conexion=0
        puerto_serial.close()
        #error en la conexión
        texto_con.delete(1.0, END)
        texto_con.insert(1.0, "ERROR EN LA CONEXIÓN")
    finally:
        #CERRAR RECURSO DE COMUNICACIÓN SERIAL
        pass
def desconectar():
    global  FLAGG,Estado_conexion,Estado_registro
    #SI EN CASO NO HUBO NINGUNA CONEXIÓN ANTERIOR NO HACER NADA
    if FLAGG==1:
        #CERRAR PUERTO SERIAL
        puerto_serial.close()
        FLAGG=0
        #PONER A CERO EL ESTADO DE CONEXIÓN
        print("SE HA DESCONECTADO")
        texto_con.delete(1.0, END)
        texto_con.insert(1.0, "DESCONECTADO")
    else:
        print("NO HUBO CONEXIÓN PREVIA")
    Estado_conexion = 0
    Estado_registro=0

def configurar():
    global Baudios,Puerto
    #CONSEGUIR EL VALOR ACTUAL DE LOS TEXTOS DE BAUDIOS Y PUERTO SERIAL
    Baudios=texto2.get(1.0,END)
    Puerto=texto1.get(1.0,END)
    texto_con.delete(1.0,END)
    texto_con.insert(1.0,"CONFIGURADO")
def registrar():
    #función que realizara el inicio del registro de las variables
    #de temperatura y humedad
    global Estado_registro
    Estado_registro=1
    texto_con.delete(1.0, END)
    texto_con.insert(1.0, "REGISTRANDO")
def detener():
    # función para detener el registro de temperatura y humedad
    global Estado_registro
    Estado_registro=0
    texto_con.delete(1.0, END)
    texto_con.insert(1.0, "STOP")
def exportar():
    #función para exportar la data en un archivo especificado por un nombre
    pass

def ver_archivo():
    #función para abrir el archivo donde esta la data de temperatura y humedad
    pass
def visualiar():
    #función para visualizar la data en tiempo real mediante matplotlib
    pass

#BOTON PARA INICIAR UNA CONEXIÓN CON LAS CONFIGURACIONES DEFINIDAS
boton1=Button(interfaz,text="CONECTAR",bg="brown",fg="white",command=conectar)
yo,xo=50,50
boton1.place(x=100+xo,y=450-yo)
#----ELEMENTOS PARA LA CONEXIÓN CON EL PUERTO SERIAL
etiqueta1=Label(interfaz,text="PUERTO SERIAL")
etiqueta1.place(x=25+xo,y=310-yo)
texto1=Text(interfaz,width=10,height=1)
texto1.place(x=20+xo,y=330-yo)
#------ELEMENTOS PARA LA CONFIGURACIÓN DE VELOCIDAD EN BAUDIOS
boton2=Button(interfaz,text="CONFIGURAR",bg="brown",fg="white",command=configurar)
y1=170
boton2.place(x=22+xo,y=370-yo)
etiqueta2=Label(interfaz,text="BAUDIOS")
etiqueta2.place(x=25+xo,y=380-y1)
texto2=Text(interfaz,width=10,height=1)
texto2.place(x=20+xo,y=400-y1)
#ELEMENTOS DE LA FUNCIÓN DESCONECTAR
boton_desconectar=Button(interfaz,text="DESCONECTAR",bg="brown",fg="white",command=desconectar)
boton_desconectar.place(x=250,y=400)
#-------------------------------------
#ELEMENTOS PARA VISUALIZAR RESPUESTA DE LA CONEXIÓN
texto_con=Text(interfaz,width=25,height=1)
texto_con.place(x=200,y=370)
#ELEMENTOS PARA EL INICIO DE REGISTRO
inicio_reg=Button(interfaz,text="INICIO DE REGISTRO",bg="brown",fg="white",command=registrar)
inicio_reg.place(x=250,y=170)
#ELEMENTOS PARA VISUALIAR LA TEMPERATURA
y3=50
eti_temp=Label(interfaz,text="TEMPERATURA C°")
#TEXTO PARA MOSTRAR TEMPERATURA
temp=Text(interfaz,width=10,heigh=1)
eti_temp.place(x=250,y=180+y3)
temp.place(x=250,y=210+y3)
#ELEMENTOS PARA VISUALIZAR LA HUMEDAD
eti_hum=Label(interfaz,text="HUMEDAD %")
#TEXTO PARA MOSTRAR HUMEDAD
hum=Text(interfaz,width=10,heigh=1)
eti_hum.place(x=250,y=230+y3)
hum.place(x=250,y=250+y3)
import time
n=0
while True:
        #actualizar la interfaz  grafica
        try:
            interfaz.update()
            interfaz.update_idletasks()
            #Preguntar si esta en estado de registro de datos
            if Estado_registro==1 and Estado_conexion==1:
                #mostrar datos en los textos de temperatura y humedad respectivamente
                #LEER DATO
                #CANTIDAD DE BYTES DISPONIBLES
                if puerto_serial.inWaiting()>0:
                    dato=puerto_serial.read()
                    dato=dato.decode()
                    #se registrara la temperatura
                    if dato=="-":
                        temp.delete(1.0, END)
                        #LEER HASTA ENCONTRAR EL SIMBOLO "*"
                        datox=puerto_serial.read_until("*".encode("utf-8"),6)
                        datox=datox.decode()
                        #LEER TODO MENOS EL SIMBOLO "*"
                        datox=datox[0:len(datox)-1]
                        print(datox)
                        #MOSTAR EN EL TEXTO
                        temp.insert(1.0,datox)
                    #se registrara la humedad relativa
                    elif dato=="+":
                        #LEER HASTA ENCONTRAR EL SIMBOLO "h"
                        pass

            #o esta en estado de detener el registro de datos
            else:
                pass
        except:
            #Cerrar aplicación
            break
            pass
print("FIN CODIGO")

