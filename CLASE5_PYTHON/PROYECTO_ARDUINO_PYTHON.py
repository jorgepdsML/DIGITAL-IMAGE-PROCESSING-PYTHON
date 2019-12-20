#uso de la comunicación serial
import serial
#importar todo del modulo tkinter
from tkinter import *
#arduino=serial.Serial()
#Crear objeto serial
arduino=serial.Serial()
# definir atributo baudrate
arduino.baudrate = 9600
arduino.port = "COM8"
#intentar conectarse al objeto serial
try :
    #INICIAR COMUNICACIÓN EN EL PUERTO port
    arduino.open()
    print("CONEXIÓN CON ARDUINO EXITOSA")
    #CREAR INTERFAZ GRAFICA
    interfaz=Tk()
    #geometry()
    interfaz.geometry("500x500")
    #metodo title()
    interfaz.title("PROYECTO ARDUINO Y PYTHON")
    def prender():
        print("PRENDIENDO LED DEL ARDUINO")
    def apagar():
        print("APAGANDO LED DEL ARDUINO")
    #crear botones
    boton1=Button(interfaz,text="LED ON",command=prender)
    boton2=Button(interfaz,text="LED OFF",command=apagar)
    #metodo place de cada boton
    boton1.place(x=220,y=300)
    boton2.place(x=300,y=300)
    mainloop()
#CODIGO QUE SE EJECUTA CUANDO SE DETECTA UN ERROR
except serial.SerialException:
    print("SE ENCONTRO UN ERROR EN EL BLOQUE try,REVISAR POR FAVOR")
#CODIGO QUE SE EJECUTA INDEPENDIENTEMENTE SI SE ENCONTRO UN ERROR O NO
finally:
    arduino.close()
    print("CERRANDO RECURSO DE MANEJO DE COMUNICACIÓN SERIAL")




