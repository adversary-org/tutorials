Tor
---

If you require the use of an anonymity enhancing connection through
the Tor network then this is readily achieved through the use of
proxies in conjunction with either one of the Vidalia bundles or Tor
directly (compiled from source).  Tor ships with both a SOCKS and a
proxy server, the former runs on port 9050 by default and the latter
on port 8118.

To configure a script to use access Tor, assuming Tor is running on
the same host as Requests, simply use the following proxy
configuration:

    proxies = {
        "http": "http://127.0.0.1:8118",
        "https": "https://127.0.0.1:8118",
    }

An example which just checks the site used by the Tor Project to check
if a connection is running through the Tor network or not is as
follows:

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

    if r.status_code == requests.codes.ok and good in r.text:
        print("You have successfully connected through the Tor network.")
    else:
        print("You are not connected through the Tor network.")

All other aspects of using Requests remain unchanged, save for the
following considerations.  First, the Tor Browser Bundle changes the
port the proxy server operates on each time it runs, so Tor should be
run solely through the one of theVidalia bundles or compiled from
source.  Second, Tor depends on OpenSSL and will inevitably connect to
servers without SSL certificates, so always include "verify=False" in
the GET or POST request.  Third, connecting to hidden services should
always use HTTP in the connection method, not HTTPS.  For example:

    import requests
    from pprint import pprint

    headers = {
        "User-Agent": "Requests over Tor"
        }

    proxies = {
        "http": "http://127.0.0.1:8118",
        "https": "https://127.0.0.1:8118",
    }

    url = "http://ic6au7wa3f6naxjq.onion/"

    r = requests.get(url, headers=headers, proxies=proxies, verify=False)
    pprint(r.text)

The output of that script ought to be the HTML for the GPG website
(www.gnupg.org).
