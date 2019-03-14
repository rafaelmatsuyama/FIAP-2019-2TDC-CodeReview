#!/usr/bin/env python3

import array
import socket

HOST = '127.0.0.1'
PORT = 1234
MAX_SIZE = 8
buf = bytearray(MAX_SIZE)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print('Dados Cliente: ', addr)

        while True:
            nbytes, sender = conn.recvfrom_into(buf)
            print('Recebido: ', buf)
            print(nbytes)
            conn.sendall(buf)

            if nbytes < MAX_SIZE:
                break
