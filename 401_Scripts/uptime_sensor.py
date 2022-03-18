#!/usr/bin/python3

import os, time, datetime;

# Declare functions

def check_ping(target):
    response = os.system("ping -c 1 " + target)

    # check the response
    print(response)
    if response == 0:
        pingstatus = "Network Active"
    else: 
        pingstatus = "Network Error"

    return pingstatus

# Handle function output

pingstatus = check_ping("8.8.8.8")

# Infinite ping loop 
while True:
    now = datetime.datetime.now()
    print(str(now) + " " + pingstatus + " to 8.8.8.8")
    time.sleep(2)
