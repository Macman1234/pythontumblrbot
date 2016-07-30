#!/usr/bin/python
import pytumblr # installs the library that makes talking to Tumblr possible through this coding
import markov
import os
import random
keyfile = open("~/pythonresources/keys.txt", "r+") # opens the file containing all the security stuff
str = keyfile.read(204) # using that file object, makes a text (a string) object
keys = str.split( ) # seperates all 4 keys (first two have to do with the API itself or something,
# second half have to do with my specific account)

client = pytumblr.TumblrRestClient( # starts the stuff for talking to Tumblr
    keys[0],
    keys[1],
    keys[2],
    keys[3],
)

print("updating Steve")

genfile = open("~/pythonresources/genfile.txt", "r+")

asklist = client.posts('macmarkov')

for ask in asklist['posts']:
    if ask['type'] == 'answer':
        genfile.write(ask['question'] + '\n')

genfile.close()

markov.Parse("askgen", 2, "~/pythonresources/genfile.txt")

asklist = client.submission('macmarkov')

for ask in asklist['posts']:
    if ask['type'] == 'answer':
        if ask['state'] == 'submission':
            client.edit_post('macmarkov', id=ask['id'], answer=markov.Gen("askgen", random.randrange(4, 6, 1)), state='published'); # edit a post

os.remove('askgen.db')
