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
good = "Congratulations. This browser is configured to use Tor."

r = requests.get(url, headers=headers, proxies=proxies, verify=False)
print(r.headers)
print(r.headers.get)

if r.status_code == requests.codes.ok and good in r.text:
    print("You have successfully connected through the Tor network.")
else:
    print("You are not connected through the Tor network.")
