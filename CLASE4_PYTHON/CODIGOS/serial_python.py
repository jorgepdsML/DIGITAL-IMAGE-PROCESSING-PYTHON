#importar modulo serial
import serial
#usar la clase Serial
#creando un objeto Serial
objeto_serial=serial.Serial()
#CONFIGURANDO LA VELOCIDAD DE COMUNICACIÓN DEL OBJETO SERIAL
objeto_serial.baudrate=9600
objeto_serial.port="COM16"
objeto_serial.open()
objeto_serial.write("sfadg")
dato=objeto_serial.read()
objeto_serial.close()

