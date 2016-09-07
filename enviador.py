#!/usr/bin/python
#coding:utf8

import socket

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n] 

def enviarMensaje(mensaje,UDP_IP,UDP_PORT):
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    
    sock.sendto(mensaje.encode('utf-8'), (UDP_IP, UDP_PORT))

UDP_IP = "192.168.0.108"
UDP_PORT = 5566

print ("UDP IP Destino: {}".format(UDP_IP))
print ("UDP Puersto destino: {}".format(UDP_PORT))
mensaje = ""

while (mensaje != "Adios!"):

    mensaje = input("Escriba el mensaje a enviar (Adios! para terminar): ")

    if len(mensaje) > 1000:
        mensajesSeparados = chunks(mensaje,1000)

        for m in mensajesSeparados:
            enviarMensaje(m,UDP_IP,UDP_PORT)
    else:
        enviarMensaje(mensaje,UDP_IP,UDP_PORT)
           
    
    
