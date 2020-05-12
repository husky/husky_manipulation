#! /usr/bin/python3

import socket
import sys
import time


# Create a TCP/IP socket
sock = socket.create_connection(('192.168.131.40', 29999))

try:
    # Send data
    message = 'close safety popup' + '\n'
    print('sending "%s"' % message, file=sys.stderr)
    sock.send(message)

    data = sock.recv(4096)
    print("Received", (data))

    message = 'power on' + '\n'
    print('sending "%s"' % message, file=sys.stderr)
    sock.send(message)

    data = sock.recv(4096)
    print("Received", (data))

    message = 'brake release' + '\n'
    print('sending "%s"' % message, file=sys.stderr)
    sock.send(message)

    data = sock.recv(4096)
    print("Received", (data))



finally:
    print('closing socket', file=sys.stderr)
    sock.close()
