#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == '__main__':
    import requests
    url = 'https://alx-intranet.hbtn.io/status'
    req = requests.get(url)
    data = req.text
    print("Body response:")
    print("\t- type:", type(data))
    print("\t- content:", data)
