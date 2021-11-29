from pwn import * 
import sys 

# Use sys to get parameters from command line 
if len(sys.argv) != 2:
    print("Invalid arguments.")
    print(">> {} <sha256sum>".format(sys.argv[0]))
    exit()

# Pass sys argv of hash to a variable 
wanted_hash = sys.argv[1]

# Assign password file 
password_file = "rockyou.txt"
attempts = 0 

with log.progress("Attempting to hack: {}.\n".format(wanted_hash)) as p: 
    with open(password_file, "r", encoding = 'latin-1') as password_list:
        for password in password_list: 
            # Get rid of new line 
            password = password.strip("\n").encode('latin-1')
            # Get hash from password list iteration
            password_hash = sha256sumhex(password)
            p.status("[{}] {} == {}".format(attempts, password.decode('latin-1'), password_hash))
            # Make comparison 
            if password_hash == wanted_hash: 
                p.success("Password hash found after {} attempts. {} hashes to {}.".format(attempts, password.decode('latin-1'), password_hash))
                exit()
            attempts += 1 
        p.failure("Password hash not found.")