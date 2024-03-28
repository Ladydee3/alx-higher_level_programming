#!/usr/bin/python3
"""
take in a URL, sends a request to the URL and displays
the body of the response (decode in utf-8).
"""

import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.arg[1]

    own_request = request.Request(url)
    try:
        with request.urlopen(own_request) as respond:
            print(response.read().decode("ascii"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
