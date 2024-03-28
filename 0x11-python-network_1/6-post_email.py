#!/usr/bin/python3
"""script that takes url and email address, sends a POST request
to the passed URL with the email as parameter, and finally displays
the body of response.
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    r = requests.post(url, data={'email': email})
    print(r.text)
