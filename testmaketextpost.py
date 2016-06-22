#!/usr/bin/python
import pytumblr
keyfile = open("/home/maclean/keys.txt", "r+")
str = keyfile.read(204)
keys = str.split( )

client = pytumblr.TumblrRestClient(
    keys[0],
    keys[1],
    keys[2],
    keys[3],
)

print(client.blog_info('macmarkov'))

client.create_text("macmarkov", state="published", slug="test-post", title="test", body="test post please ignor")
