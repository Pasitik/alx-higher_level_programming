#!/usr/bin/python3
import urllib.request

req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
with urllib.request.urlopen(req) as response:
    data = response.read()
    utf8_content = data.decode('utf-8')

print("Body response:")
print("\t- type:", type(data))
print("\t- content", data)
print("\t- utf8 content", utf8_content)
