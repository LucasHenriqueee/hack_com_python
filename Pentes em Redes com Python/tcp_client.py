#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# tcp_client.py

import socket

HOST = 'www.google.com'
PORT = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 1 - criando um objeto socket
client.connect((HOST, PORT)) #conecte o cliente

client.send(b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n') # envie algum dado
response = client.recv(4096) # recebemos algum tipo de dado
print(response.decode('utf-8')) # imprimimos atela

client.close()