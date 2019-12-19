#importar del modulo todo
from serial import *
objeto_serial=Serial()
objeto_serial.baudrate=9600
objeto_serial.port="COM20"