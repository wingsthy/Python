#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 6688))
server.listen(5)
print(server.getsockname())

print('waiting for connect...')
connect, (host, port) = server.accept()
peer_name = connect.getpeername()
sock_name = connect.getsockname()
print('the client %s:%s has connected.' % (host, port))
print('The peer name is %s and sock name is %s' % (peer_name, sock_name))

data = connect.recv(1024)
connect.sendall('your words has received.')
print('the client say:' + data)

server.close()

