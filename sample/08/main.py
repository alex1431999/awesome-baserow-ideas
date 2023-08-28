#!python3

import requests
import json
from pynostr.key import PrivateKey
from csv import DictReader
        
print("Welcome e2e...")
welcome = input("Do you have an acount? y/n: ")
private_key = PrivateKey()
public_key = private_key.public_key
public_keybench32 = public_key.bech32()
private_keybench32 = private_key.bech32()

def writeFile(public_keybench32, private_keybench32):
    with open('password.csv','wb') as file:
        for line in text:
            file.write(public_keybench32)
            file.write(private_keybench32)
    file.close()

def readFile():
    with open('password.csv', 'r') as read_obj:
        csv_dict_reader = DictReader(read_obj)
        for row in csv_dict_reader:
            print(row['public_key'], row['private_key'])
        
if welcome == "y":
    while True:
        print("Welcome to login...")
        add_public_key = input("Enter a username:")
        add_private_key = input("Enter a password:")
        if add_public_key == row['public_key'] and add_private_key == row['private_key']:
            print("Welcome")
            break
        else:
            print("Incorrect username or password.")

if welcome == "n":
    while True:
        account  = input("Do you want create account? confirm/cancel: ")
        if account == "confirm":
            writeFile(public_keybench32, private_keybench32)
            print({'public_key': public_keybench32, 'private_key': private_keybench32})
            welcome = "y"
            break
        if account == "cancel":
            break
        else:
            print("Passwords do NOT match or Incorrect username, password!")
