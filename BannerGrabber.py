#!/usr/bin/python3

import socket 

def banner(ip, port):
    # Call socket module from socket class
    s = socket.socket()

    # Use socket to connect to provided IP and port 
    s.connect((ip, int(port)))
    s.settimeout(5)

    # Print out what is received
    print(str(s.recv(1024)))

def main():
    # Ask user for IP address and port
    ip = input("Please enter the IP address: ")
    port = str(input("Please enter the port: "))
    banner(ip, port)

main()