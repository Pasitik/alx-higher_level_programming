#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urlib package
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        data = response.read()
        utf8_content = data.decode('utf-8')

    print("Body response:")
    print("\t- type:", type(data))
    print("\t- content", data)
    print("\t- utf8 content", utf8_content)
