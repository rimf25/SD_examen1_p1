from socket import *
from sunau import AUDIO_FILE_ENCODING_ALAW_8
import sys
import gc

IPServer = "localhost"
puertoServer = 9099

socketClient = socket(AF_INET, SOCK_STREAM)
socketClient.connect((IPServer, puertoServer))

while True:

    mensaje = input()

    if mensaje == 'count':
        print(gc.get_count())

    if mensaje == 'collect':
        gc.collect()
        print(gc.get_count())     

    if mensaje != 'stop':

        socketClient.send(mensaje.encode())
        respuesta = socketClient.recv(4096).decode()
        print (respuesta)

    else:
        socketClient.send(mensaje.encode())
        socketClient.close()
        sys.exit()    
