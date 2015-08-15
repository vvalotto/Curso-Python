#server.py

import socket
import time

#crear el objeto demo_socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#obtiene el nombre de la maquina local
host = socket.gethostname()

port = 9999

#enlaza el puerto
serversocket.bind((host, port))

#encola hasta 5 pedidos
serversocket.listen(5)

while True:
    #Establece al conexion
    clientsocket, addr = serversocket.accept()

    print("Tenemos una conexion desde %s" % str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()

