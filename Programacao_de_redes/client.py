#!/usr/bin/env python3

import socket

# create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machina name
host = socket.gethostname()

port = 999


# connection to host name on the port
s.connect((host, port))

# Receive no more than  1024 bytes
msg = s.recv(1024)

s.close()

print(msg.decode('ascii'))