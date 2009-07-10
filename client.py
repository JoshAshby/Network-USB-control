#!/usr/bin/env python
import socket
import sys


if (len(sys.argv) > 1):#looks for text to send in the argument line
    text = sys.argv[1]
    host = 'localhost'
    port = 5000
    size = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    s.send(text)
    s.close()
else:
    pass

def send(text):
    host = 'localhost'
    port = 5000
    size = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    s.send(text)
    s.close()

def recieve():
    host = 'localhost'
    port = 5000
    size = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    data = s.recv(size)
    return data
    s.close()