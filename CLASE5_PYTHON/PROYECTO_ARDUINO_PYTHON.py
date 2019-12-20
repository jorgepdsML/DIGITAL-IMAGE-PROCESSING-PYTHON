#uso de la comunicación serial
import serial
#arduino=serial.Serial()
#Crear objeto serial
arduino=serial.Serial()
# definir atributo baudrate
arduino.baudrate = 9600
arduino.port = "COM12"
#intentar conectarse al objeto serial
try :
    #INICIAR COMUNICACIÓN EN EL PUERTO port
    arduino.open()
    print("CONEXIÓN CON ARDUINO")
#CODIGO QUE SE EJECUTA CUANDO SE DETECTA UN ERROR
except:
    print("SE ENCONTRO UN ERROR EN EL BLOQUE try,REVISAR POR FAVOR")
#CODIGO QUE SE EJECUTA INDEPENDIENTEMENTE SI SE ENCONTRO UN ERROR O NO
finally:
    arduino.close()


