"""IMPORTAR LOS MODULOS NECESARIOS"""
import pyautogui as pd
import serial
from sys import exit
from time import sleep
#dimensión de la pantalla
dimension=pd.size()
#------DIMENSIÓN ANCHO
W=dimension[0]
#-----DIMENSIÓN ALTO
H=dimension[1]
#PROTOTIPO DE FUNCIONES
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
Baudios=115200
Puerto="COM3"
#CREAR objeto para la comunicación serial
puerto_serial = serial.Serial()
puerto_serial.timeout=5
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
            print(dato,'s')
    except:
        print("EXISTE ALGUN ERROR EN LA COMUNICACIÓN!!!!")
        for i in range(3,0,-1):
            print("SALIENDO EN ",i)
            sleep(1)
        print("FIN DEL PROGRAMA---VUELVA A CONECTAR EL DISPOSITIVO ")
        exit()