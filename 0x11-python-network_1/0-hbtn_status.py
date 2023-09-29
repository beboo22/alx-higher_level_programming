#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import urllib.request as request

url = "https://alx-intranet.hbtn.io/status"
data = request.Request(url)
with request.urlopen(data) as f:
    r = f.read()
    print("Body response:")
    print("\t- type: {}".format(type(r)))
    print("\t- content: {}".format(r))
    print("\t- utf8 content: {}".format(r.decode('utf-8')))
