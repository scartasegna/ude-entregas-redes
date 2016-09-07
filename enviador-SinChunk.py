#!/usr/bin/python
#coding:utf8

import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5566

print ("UDP IP Destino: {}".format(UDP_IP))
print ("UDP Puersto destino: {}".format(UDP_PORT))
mensaje = ""

while (mensaje != "Adios!"):

    mensaje = input("Escriba el mensaje a enviar (Adios! para terminar): ")
    
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    
    sock.sendto(mensaje.encode('utf-8'), (UDP_IP, UDP_PORT))
