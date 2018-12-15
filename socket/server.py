#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 6688))
server.listen(5)
print(server.getsockname())

print(u'waiting for connect...')
connect, (host, port) = server.accept()
peer_name = connect.getpeername()
sock_name = connect.getsockname()
print(u'the client %s:%s has connected.' % (host, port))
print('The peer name is %s and sock name is %s' % (peer_name, sock_name))

data = connect.recv(1024)
connect.sendall(b'your words has received.')
print(b'the client say:' + data)

server.close()

