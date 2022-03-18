#!/bin/python3

# Script:                   401 Ops Challenge Uptime Sensor 
# Author:                   Marco Vazquez
# Date of latest revision:  3/18/2022
# Purpose:                  Uptime Sensor Pt 2 of 2

from http import server
import smtplib;
import os, time, datetime
from sqlite3 import Timestamp;
from getpass import getpass;

# Declare variables 
up = "Network is ACTIVE"
down = "Network is DOWN"
last = 0
ping_result = 0
email = input("Enter your email: ")
password = getpass()
ip = input("What IP Address would you like to monitor?")

# Declare functions

# Send the emails

def send_upAlert():
    now = datetime.datetime.now()
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(email, password)
    up_messsage = "Your system has recovered. \n %s" % now 
    server.sendmail('statusbot@myservers.com', email, up_messsage)
    server.quit()

def send_downAlert():
    now = datetime.datetime.now()
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(email, password)
    down_message = "Your system is DOWN. \n %s" + now
    server.sendmail('statusbot@myservers.com', email, down_message)
    server.quit()
    

def ping():
    now = datetime.datetime.now()

    global ping_result
    global last

    if ((ping_result != last) and (ping_result == up)):
        last = up
        send_upAlert()
    elif ((ping_result != last) and (ping_result == down)):
        send_downAlert()
        last = down
    
    response = os.system("ping -c 1 " + ip)
    if response == 0:
        ping_result = up
    else: 
        ping_result = down
    print(now + ping_result + " to " + ip)
 
# Infinite ping loop 
while True:
    ping()
    time.sleep(2)


