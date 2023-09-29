#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    v = {'email': argv[2]}
    req = requests.post(argv[1],parmeter=v)
    print(req.text)
