import requests

URL = "https://jupiter.challenges.picoctf.org/problem/50522/flag"


def bypass(url=URL):
    session = requests.Session()
    session.headers.update({'User-Agent': 'picobrowser'})
    return session.get(url).text


n = bypass()

print(n)
