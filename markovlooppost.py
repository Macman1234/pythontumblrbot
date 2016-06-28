#!/usr/bin/python
import pytumblr # installs the library that makes talking to Tumblr possible through this coding
import markov
import os
import random
import time
keyfile = open("/home/maclean/pythonresources/keys.txt", "r+") # opens the file containing all the security stuff
str = keyfile.read(204) # using that file object, makes a text (a string) object
keys = str.split( ) # seperates all 4 keys (first two have to do with the API itself or something,
# second half have to do with my specific account)

client = pytumblr.TumblrRestClient( # starts the stuff for talking to Tumblr
    keys[0],
    keys[1],
    keys[2],
    keys[3],
)

# markov.Parse("omam", 2, "omam.txt")
# print(markov.Gen("omam", 2))

while True:
    print("Updating Blog")
    genfile = open("/home/maclean/pythonresources/genfile.txt", "r+")
    asklist = client.submission('macmarkov')
    for ask in asklist['posts']:
        if ask['type'] == 'answer':
            if ask['state'] == 'submission':
                genfile.write(ask['question'] + '\n')

    genfile.close()
    markov.Parse("askgen", 2, "/home/maclean/pythonresources/genfile.txt")

    for ask in asklist['posts']:
        if ask['type'] == 'answer':
            if ask['state'] == 'submission':
                client.edit_post('macmarkov', id=ask['id'], answer=markov.Gen("askgen", random.randrange(2, 5, 1)), state='published'); # edit a post

    os.remove('askgen.db')
    time.sleep(60)
