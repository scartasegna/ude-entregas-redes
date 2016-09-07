#!/usr/bin/python
#coding:utf8

#coding:utf8

import socket

# En esta seccion se configura la IP y Puerto donde estara el servicio
# en caso de querer probarlo todo en el mismo host, podemos usar 127.0.0.1 
UDP_IP = "192.168.0.108"
UDP_PORT = 5566

# Creamos un socket por medio de su constructor, utilizando las constantes que
# indican que se usara IP y UDP

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

# Hacemos que nuestro socket "escuche" en la ip y puerto configurados

sock.bind((UDP_IP, UDP_PORT))

print("Servicio iniciado, escuchando en {}:{}".format(UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # El tamanio del buffer es 1024 bytes
    mensaje = data.decode('utf-8')
    print ("Mensaje Recibido desde {}: ".format(str(addr)))
    print(mensaje)
    print("")
