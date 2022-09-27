#!/usr/bin/python3
"""script that,takes in a URL,send request to URL & display value of the
X-Request-Id variable found in  header ofthe response.use request & sys package
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
