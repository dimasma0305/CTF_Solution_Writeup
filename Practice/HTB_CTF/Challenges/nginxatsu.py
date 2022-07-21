from Crypto.Cipher import AES
import base64
import json
import urllib.parse
from Crypto.Util.Padding import pad, unpad
from phpserialize import unserialize


KEY = "cgxs+3SOT4QBcNDUWBOA5/FoS/Tao9k5y2vHTP3lP0E="
COOKIE = "eyJpdiI6ImNac05UQTJhRWV3NHUxMXg4eEdvWEE9PSIsInZhbHVlIjoiaVVuTVlYNFhVOExkZitBWWNjUkZWK3YzZ0E4clJsS2xma0s2R3dBcXVLaGpLNzBEclRNRHViUDQxVm5vQ1JXODhYMzNjOUNMQ0Vnb2RGOG1qTTRBa2VVM0QwaE9ZSm1YYWI4YWJ2XC8wb2lnbU82UEFiYitybXMrcHBkazg5VVZ0bmxPY3grXC9IRzVZWVl1OUlDUTNLb084ZHhyZzBiV3pmQkRiQmo4RFVGMHJMdjRQM0tyVEV1VFlFMHNjUTA2amVhdXN3QmtlRW1XVVQyTlwvK1JyMWlTdm56QjVrR3hoQ0Rsa0R1NXhMd2pQcnJobFk3aEluT250YlJZWXFLXC85cjZGV2F2Q0pHRFZ6S2FETmI3emNyN3ZORE1OaWZTWElcL05YRFNTc0dpTGxwMk9lVjZDMmUrXC80UFpRamJPalNVOXVSalA2RTZSMk4zK3F4enJQS0xFd1VUR1FsV3hZMzNRZE9WQldEZ2JRTzRmaGRkd0ZYYVVcL3JmZ1gycUhQeGNpR0Z0dWJYbXdoajVqclwvXC9hcU5RVzRQWnpoNmVIdCtkK3EzcEI1cndOYTJnMFN4NlpUWnVWcWpibTAraGUrQkJlNXd4UWNXWldLb2xhelM3QndaVms0REE9PSIsIm1hYyI6ImRiOWU0ZGE0YmI5Mjc4MTEyNjE3Yjk3YjViMjgwZjMyY2RlOWIwOTY4YzZhNDg5OGE3YzM4YmY0NGE4NDY0ZjAifQ%3D%3D"


class Laravel:
    def __init__(cls, key):
        cls.key = base64.b64decode(key)

    def decrypt_value(cls:str, text:str) -> str:
        decoded_text = json.loads(base64.b64decode(
            urllib.parse.unquote_plus(text)))
        iv = base64.b64decode(decoded_text['iv'])

        crypt_object = AES.new(key=cls.key, mode=AES.MODE_CBC, IV=iv)

        decoded = base64.b64decode(decoded_text['value'])
        decrypted = unpad(crypt_object.decrypt(decoded), len(decoded)).decode()
        decoded_text['value'] = decrypted
        return decoded_text

    def encrypt_value(cls:str, decstr:str, encstr:str) -> str:
        decoded_text = json.loads(base64.b64decode(
            urllib.parse.unquote_plus(encstr)))
        iv = base64.b64decode(decoded_text['iv'])

        crypt_object = AES.new(key=cls.key, mode=AES.MODE_CBC, IV=iv)

        encoded = decstr
        encrypted = crypt_object.encrypt(encoded)
        decoded_text['value'] = base64.b64encode(encrypted)
        return decoded_text
    


lar = Laravel(KEY)
print(lar.decrypt_value(COOKIE))