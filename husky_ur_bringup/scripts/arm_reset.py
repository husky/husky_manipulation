#! /usr/bin/python

import socket
import sys
import time


# Create a TCP/IP socket
sock = socket.create_connection(('192.168.131.40', 29999))

try:
    # Send data
    message = 'close safety popup' + '\n'
    print >>sys.stderr, 'sending "%s"' % message
    sock.send(message)

    data = sock.recv(4096)
    print("Received", (data))

    message = 'power on' + '\n'
    print >>sys.stderr, 'sending "%s"' % message
    sock.send(message)

    data = sock.recv(4096)
    print("Received", (data))

    message = 'brake release' + '\n'
    print >>sys.stderr, 'sending "%s"' % message
    sock.send(message)

    data = sock.recv(4096)
    print("Received", (data))



finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
