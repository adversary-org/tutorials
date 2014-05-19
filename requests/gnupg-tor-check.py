#!/usr/bin/env python3

import requests
from pprint import pprint

headers = { "User-Agent": "Requests Over Tor" }
proxies = { "http": "http://127.0.0.1:8118",
            "https": "https://127.0.0.1:8118", }

url = "http://ic6au7wa3f6naxjq.onion/"

r = requests.get(url, headers=headers, proxies=proxies, verify=False)

pprint(r.text)
print(r.status_code)

if r.status_code == requests.codes.ok:
    print(True)
else:
    print(False)

