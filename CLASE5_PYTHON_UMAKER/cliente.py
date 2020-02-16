import socket,pickle,time
HOST="192.168.1.38"#localhost
PORT=2000
cliente=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    # método connect para conectarse a un servidor
    cliente.connect((HOST, PORT))
    #ENVIAR UN MENSAJE
    msje="http://gen.lib.rus.ec/search.php?req=Adrian+Rosebrock&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def"
    #CONVERTIR A FLUJO DE BYTES
    dato=pickle.dumps(msje)
    #ENVIAR all LO QUE CONTENGA DATO
    cliente.sendall(dato)

except:
    print("ERROR EN LA CONEXIÓN , VERIFICAR SERVIDOR")
finally:
    #CERRAR LA COMUNICACIÓN CON EL SERVIDOR
    cliente.close()
