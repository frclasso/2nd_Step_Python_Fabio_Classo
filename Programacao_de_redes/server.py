
#!/usr/bin/env python3

import socket

# create a socket object

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 999

# bind the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish connection
    clientesocket,addr = serversocket.accept()

    print("Got a connection from %s" % str(addr))

    msg = 'Thank you for connecting' + "\r\n"

    clientesocket.send(msg.encode('ascii'))
    clientesocket.close()