#!/usr/bin/python3
"""script that takes in a URL,send POST request to passed URL,takes email as a
parameter,display body of response,use with statement,only use sys and urllib
"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
