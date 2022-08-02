from base64 import b64decode
import requests
import urllib.parse

URL = "http://natas28.natas.labs.overthewire.org"
AUTH = ("natas28", "JWwR438wkgTsNKBbcJoowyysdM82YjeF")

s = requests.Session()


def reqeust_decode(test_query):
    r = s.get(URL+f"/?query={test_query}", auth=AUTH)
    _, query = (r.url).split("=")
    decoded_query = b64decode(urllib.parse.unquote_plus(query)).hex()
    return decoded_query


def seperate(num, txt):
    '''Seperate txt by num'''
    foo = ''
    for i in range(0, len(txt), num):
        foo += txt[0+i:num+i] + "\n"
    return foo


def main():
    for i in range(1, 16):
        decode = reqeust_decode("a"*i)
        len_decode = len(decode)
        decode = seperate(32, decode)
        print(f"---request {i}---\nlen: {len_decode}\n---decode (hex)---\n{decode}")

main()