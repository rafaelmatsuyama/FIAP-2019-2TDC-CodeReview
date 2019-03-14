#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Ola Mundo!')

    while True:
        data = s.recv(1024)

        if not data:
            break

        print('Recebido', repr(data))