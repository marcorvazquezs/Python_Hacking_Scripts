#!/usr/bin/python3

import os, time, datetime

# Declare function check_ping
def check_ping(target):

	response = os.system("ping -c 1 " + target)
	if response == 0:
		pingstatus = "Network Active"
	else:
		pingstatus = "Network Inactive"

	return pingstatus

# Handle function output

pingstatus = check_ping("8.8.8.8")

# Infinite loop
while True:
	now = datetime.datetime.now()
	print(str(now) + " " + pingstatus + " to 8.8.8.8")
	time.sleep(2) 

