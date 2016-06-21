#!/usr/bin/python
import pytumblr
keyfile = open("/home/maclean/keys.txt", "r+")
str = keyfile.read(102)
keys = str.split( )
print("Public key is: " + keys[0])
print("Secret key is: " + keys[1])
