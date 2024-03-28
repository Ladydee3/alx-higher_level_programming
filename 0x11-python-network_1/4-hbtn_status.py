#!/usr/bin/python3
"""
fetches https://alx-intranet.htbn.io/status
"""

import requests

if __name__ == '__main__':
    r = requests.get('https://alx-intranet.htbn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
