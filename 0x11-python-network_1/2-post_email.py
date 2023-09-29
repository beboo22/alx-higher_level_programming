#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response
"""
if __name__ == "__main__":
    import urllib.parse as parse
    import urllib.request as request
    from sys import argv
    v = {'email': argv[2]}
    data = parse.urlencode(v).encode('utf-8')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as f:
        print(f.read().decode('utf-8'))
