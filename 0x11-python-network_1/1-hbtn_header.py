#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        if 'X-Request-Id' in response.headers:
            x_req_id = response.headers['X-Request-Id']
            print(x_req_id)
