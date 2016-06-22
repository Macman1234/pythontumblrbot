#!/usr/bin/python
import pytumblr
keyfile = open("/home/maclean/keys.txt", "r+")
str = keyfile.read(102)
keys = str.split( )

client = pytumblr.TumblrRestClient(
    str[0],
    str[1],
    str[2],
    str[3],
)

client.create_text("macmarkov", state="published", slug="huh-did-not-know-you-could-do-this", title="test", body="test post please ignor")
