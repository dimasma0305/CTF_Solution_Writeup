from base64 import b64decode
import requests
import urllib.parse

URL = "http://natas28.natas.labs.overthewire.org"
AUTH = ("natas28", "JWwR438wkgTsNKBbcJoowyysdM82YjeF")


def query_len(test_query):
    r = requests.get(URL+f"/?query={test_query}", auth=AUTH)
    _, query = (r.url).split("=")
    query = urllib.parse.unquote_plus(query)
    print(query)
    query = len(b64decode(query))
    return query


diff = 0
for i in range(1, 16):
    query = query_len("a"*i)
    print(f"len {i}: "+str(query))
    diff = query - diff
    # print("diff: "+str(diff))
    # diff = query
