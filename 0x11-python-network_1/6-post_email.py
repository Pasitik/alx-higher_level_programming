#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    payload = {"email": sys.argv[2]}
    r = requests.post(url, data=payload)
    print("Your email is:", sys.argv[2])
    print(r.text)