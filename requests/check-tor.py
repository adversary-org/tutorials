#!/usr/bin/env python3

import requests

headers = {
    "User-Agent": "Requests over Tor"
    }

proxies = {
    "http": "http://127.0.0.1:8118",
    "https": "https://127.0.0.1:8118",
    }

url = "https://check.torproject.org/"

r = requests.get(url, headers=headers, proxies=proxies, verify=False)
print(r.headers)
print(r.headers.get)
