#!/usr/bin/python3

import socket
import threading

bind_ip = "127.0.0.1"
bind_port = 22

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print ("[*] Listening on %s:%d" % (bind_ip,bind_port))

# This is our client-handling thread
def handle_client(client_socket):
        # print out what the client sends
        request = client.socket.recv(1024)

        print ("[*] Received: %s" % request)

        # send back a packet
        client_socket.send("ACK!")

        client_socket.close()
