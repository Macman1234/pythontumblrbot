#!/usr/bin/python
import pytumblr
keyfile = open("/home/maclean/keys.txt", "r+")
str = keyfile.read(204)
keys = str.split( )

client = pytumblr.TumblrRestClient(
    str[0],
    str[1],
    str[2],
    str[3],
)

client.create_text("macmarkov", state="published", slug="test-post", title="test", body="test post please ignor")
