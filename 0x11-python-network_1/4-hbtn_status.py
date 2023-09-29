#!/usr/bin/python3

import requests

r = requests.get('https://alx-intranet.hbtn.io/status')
content = r.text

print("Body response:")
print("\t- type:", type(content))
print("\t- content:", content)
