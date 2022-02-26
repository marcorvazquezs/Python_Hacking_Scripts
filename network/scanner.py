#!/usr/bin/python

import sys 
import socket
from datetime import datetime as dt
from unittest import result 

# Define the target 
if len(sys.argv) == 2:
    # Translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
else: 
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")

# Add a banner 
print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

# Try statement 
try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # returns an error indicator
        result = s.connect_ex((target,port))
        if result == 0: 
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror: 
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error: 
    print("Couldn't connect to server.")
    sys.exit()