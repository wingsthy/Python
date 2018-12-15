#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 6688))

data = raw_input()
data = data.encode('utf-8')
client.sendall(data)
rec_data = client.recv(1024)
print(b'form server receive:' + rec_data)

client.close()


