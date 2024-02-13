#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# udp_client.py

import socket

HOST = '127.0.0.1' #Standard loopback interface address (localhost)
PORT = 9997

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 1 - criando um objeto socket
client.send(b"AAABBBCCC", (HOST, PORT)) #conecte o cliente

data, address = client.recvfrom(4096)
print(data.decode('utf-8'))
print(address.decode('utf-8'))

client.close()