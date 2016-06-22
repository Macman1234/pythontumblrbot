#!/usr/bin/python
import pytumblr # installs the library that makes talking to Tumblr possible through this coding
keyfile = open("/home/maclean/keys.txt", "r+") # opens the file containing all the security stuff
str = keyfile.read(204) # using that file object, makes a text (a string) object
keys = str.split( ) # seperates all 4 keys (first two have to do with the API itself or something,
# second half have to do with my specific account)

client = pytumblr.TumblrRestClient( # starts the stuff for talking to Tumblr
    keys[0],
    keys[1],
    keys[2],
    keys[3],
)

print(client.blog_info('macmarkov')) # outputs the info of the blog to my screen when I run it (just for debugging)

client.create_text("macmarkov", state="published", slug="test-post", title="test", body="test post please ignor")
# ^ actually makes the post
