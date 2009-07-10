#!/usr/bin/env python
import socket
import serial
import client

usbport = '/dev/ttyUSB0'
ser = serial.Serial(usbport, 9600, timeout=1)

host = 'localhost'
port = 5000
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
while 1:
    client, address = s.accept()
    data = client.recv(size)
    if data:
        print data
        ser.write(data)
        client.send(data)
    client.close()
