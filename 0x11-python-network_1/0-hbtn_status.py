#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == '__main__':
    import urllib.request
    url = 'https://alx-intranet.hbtn.io/status'
    req = urllib.request.Request(url, method='GET')
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content.decode('utf8'))
