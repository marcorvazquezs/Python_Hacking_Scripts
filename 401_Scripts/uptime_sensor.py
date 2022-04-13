#!/bin/python3

# Script: 401 Ops Challenge Day 3
# Purpose: Uptime Sensor Pt 2 of 2

# Import libraries
import smtplib
import datetime, time, os
from getpass import getpass

# Declare variables
up = " Network is ACTIVE"
down = " Network is DOWN"
last = 0
ping_result = 0
email = input("Enter your email: ")
password = getpass()
ip = input("What address would you like to monitor?")

# Declare functions

# Send the email (two options)

def send_upAlert():
	now = datetime.datetime.now()
	timestamp = now.strftime('%m-%d-%Y %H:%M:%S %p')
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.ehlo()
	server.login(email, password)
	msg1= "Hello! \nYour system has recovered.\n %s" % timestamp
	server.sendmail('mailbot@myserver.com', email, msg1)
	server.quit()

def send_downAlert():
	now = datetime.datetime.now()
	timestamp = now.strftime('%m-%d-%Y %H:%M:%S %p')
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.ehlo()
	server.login(email, password)
	msg2 = "ALERT! \nYour system has gone DOWN.\n %s" % timestamp
	server.sendmail('mailbot@myserver.com', email, msg2)
	server.quit()

# Ping test
def ping():
	now = datetime.datetime.now()
	timestamp = now.strftime('%m-%d-%Y %H:%M:%S %p')

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
	print(timestamp + ping_result + " to " + ip)

# Main

while True:
	ping()
	time.sleep(2)

# End
