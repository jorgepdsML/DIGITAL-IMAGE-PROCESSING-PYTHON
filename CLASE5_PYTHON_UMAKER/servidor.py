"""
ESTE ARCHIVO ES DEL LADO DEL SERVIDOR
"""
import socket,pickle
HOST="192.168.2.106"#localhost
PORT=65432
#IPV4 , TCP
servidor=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#REALIZAR EL bind del HOST Y PORT A NUESTRO PYTHON
servidor.bind((HOST,PORT))
#ESUCHAR CONEXIONES DE LOS CLIENTES
print("SERVIDOR ESCUCHANDO CONEXIONES--")
servidor.listen()
#EL SERVIDOR SE HA CONECTADO A UN CLIENTE
#ACEPTAR LA CONEXIÓN
#cliente,su dirección
cliente,direccion=servidor.accept()

with cliente:
    dato=cliente.recv(1000)
    #el cliente esta conectado?
    if not dato:
        print("CLIENTE DESCONECTADO")
    #el cliente no se ha conectado
    else:
        #convertir de bytes al tipo de dato original
        dato_original = pickle.loads(dato)
        print(dato_original)
        cesar="""
        import socket,pickle
HOST="192.168.2.106"#localhost
PORT=65432
#IPV4 , TCP
servidor=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#REALIZAR EL bind del HOST Y PORT A NUESTRO PYTHON
servidor.bind((HOST,PORT))
#ESUCHAR CONEXIONES DE LOS CLIENTES
print("SERVIDOR ESCUCHANDO CONEXIONES--")
servidor.listen()
#EL SERVIDOR SE HA CONECTADO A UN CLIENTE
#ACEPTAR LA CONEXIÓN
#cliente,su dirección
cliente,direccion=servidor.accept()

with cliente:
    dato=cliente.recv(1000)
    #el cliente esta conectado?
    if not dato:
        print("CLIENTE DESCONECTADO")
    #el cliente no se ha conectado
    else:
        #convertir de bytes al tipo de dato original
        dato_original = pickle.loads(dato)
        print(dato_original)
#cerrar el recurso de la comunicación
servidor.close()"""
        cebyte=pickle.dumps(cesar)
        cliente.sendall(cebyte)
#cerrar el recurso de la comunicación
servidor.close()