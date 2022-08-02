from socket import *


direccionServer = "localhost"
puertoServer = 9099

socketServer = socket( AF_INET, SOCK_STREAM )
socketServer.bind((direccionServer, puertoServer))
socketServer.listen()

while True:
    socketConexion, addr = socketServer.accept()
    print("Conexion", addr)
    while True:
        mensajeRecibido = socketConexion.recv(4096).decode()
        print(mensajeRecibido)

        if mensajeRecibido == 'stop':
            break
        mensaje = "\nIngrese Count, Collect o Stop para salir."
        socketConexion.send(mensaje.encode())

    print("Desconectado", addr)
    socketConexion.close()    
