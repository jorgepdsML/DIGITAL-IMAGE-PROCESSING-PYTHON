"""
GRUPO 1 PDS
"""
#INTERACTUAR CON EL PUNTERO DEL MOUSE
import pyautogui as pd
#libreria para comunicar python con el puerto serial (COM 3)
import serial
#Función exit para salir del programa
from sys import exit
#función sleep() retardo de tiempo
from time import sleep
#dimensión de la pantalla
dimension=pd.size()
W=dimension[0]
H=dimension[1]
def derecha(x,y):
    for k in range(x,x+35,5):
        pd.moveTo(k,y)
def izquierda(x,y):
    for k in range(x,x-35,-5):
        pd.moveTo(k,y)
def arriba(x,y):
    for k in range(y,y-35,-5):
        pd.moveTo(x,k)
        sleep(0.05)
def abajo(x,y):
    for k in range(y,y+35,5):
        pd.moveTo(k,y)
def click(x,y):
    pd.click(x=x,y=y)
    pass
#-------------------------------COMUNICACIÓN SERIAL
Baudios=9600#velocidad en baudios
Puerto="COM3"#puerto serial
#CREAR objeto para la comunicación serial
puerto_serial = serial.Serial()
puerto_serial.timeout=3
try:
    puerto_serial.port = Puerto
    puerto_serial.baudrate = Baudios
    print(puerto_serial.isOpen())
    puerto_serial.open()
    Estado_conexion = 1
except serial.SerialException:
    Estado_conexion = 0
    puerto_serial.close()
except :
    Estado_conexion = 0
    puerto_serial.close()
finally:
    if Estado_conexion==0:
        print("-----ERROR EN LA CONEXIÓN !!!")
        exit()
    else:
        print("-----CONEXIÓN CORRECTA :)--")
        print(puerto_serial.isOpen())
#---------------------BUCLE INFINITO
while True:
    #determinar si hay datos en el buffer de recepción
    try:
        if puerto_serial.inWaiting()>0:
            dato=puerto_serial.read()
            dato=dato.decode()
            #leer los datos de la posición actual del cursos del mouse
            xy = pd.position()
            x = xy.x
            y = xy.y
            #preguntar uqe caracter se ha recibido
            dato=dato.lower()
            if dato=='l':
                #MOVIMIENTO A LA IZQUIERDA DEL MOUSE
                print("izquierda")
                izquierda(x,y)
            if dato=='r':
                print("derecha")
                derecha(x,y)
            if dato=='u':
                print("arriba")
                arriba(x,y)
            if dato=='d':
                abajo(x,y)
            if dato=='c':
                print("click")
                click(x,y)
            if dato=='n':
                break
    except:
        print("EXISTE ALGUN ERROR EN LA COMUNICACIÓN!!!!")
        for i in range(3,0,-1):
            print("SALIENDO EN ",i)
            sleep(1)
        print("FIN DEL PROGRAMA---VUELVA A CONECTAR EL DISPOSITIVO ")
        exit()
