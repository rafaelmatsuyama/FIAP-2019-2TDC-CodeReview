#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Ola Mundo!')
    data = s.recv(1024)

print('Recebido', repr(data))