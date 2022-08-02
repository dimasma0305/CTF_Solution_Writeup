from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from base64 import b64decode, b64encode

URL = 'http://test.com/'
COOKIE = 'eyJpdiI6ImtcL1oyT2NkckJDZm1vWXFkeXB1RWdBPT0iLCJ2YWx1ZSI6IkRIdFd5RUl6WWVUYUNhakJcL2laQ3RtUm5MbXRxRXl1Zm5RYlhnY0ZRc050eDlhUE5HalwvbGR5WWtwd0tFTjVKbTJ2ZGNKdVJCOFlPMHpubEVKSDZ0bjBxbHlDRHpTWVFWVktUMFgzbHQ4czNESzllS2ZNdHU2SHpJZFJwOEZKb0pqZUlkeEdZUlVkaFwvd3JjUDVxYnlwTE0xUkJURnZnXC8rVjArWStVQnA5bXpEVE93eXhrNmxFOXNob2dWaDdrUDhmSk1RZXMwU1Nld3pMYlpkQmtMK1JwZDZvdk90SEZZVjYwWnVJY0hcLzJ1eDE4VXBRQTdTdWpOWlU5TXlsNnF2MUxiaHp3Q2hYcE5GTkFWRVhFZnpMbG9PMExwYVdDN29IcEFZNXhESkxSeW10eWpJQXB5citiXC9FbXIreFgzck0zQVRhRm9POGdka3B1TFRcL1hSYWx5K0VlNGMxbDl4elRRcmNQYjNnVUZnTlpVMUpycHAzdVQxQjg2WEpxQVwvaG00U0thTWZpaWhZQ2orWkFBNXdkV2QrNk8rSTJMSUFSTEg0OWV4dmo3bUtWOGt2b29ocldaVnVrZ0lsRkVhUk03OVNodzNFSkNwSStjSW9NZ09YSGppOFE9PSIsIm1hYyI6IjFjMjgzYTQ1MTc4ZWJjYmFmNzkwMGNhMzZkYThlMDdiNjhiNWQ2NDE3YTY4MTFiOWY0NjIwYTJhNzk3NTMxZDYifQ=='
KEY = 'GHXw+QM97EG1vWUzQI59o2IHYhE9XkYzYYBKMtx52+U='
class Aes:
	def __init__(self, key):
		self.key = key
		self.iv = None

	def encrypt(self, pt):
		cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
		return cipher.encrypt(pad(pt, 16))

	def decrypt(self, ct):
		cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
		return unpad(cipher.decrypt(ct), 16)

class Laravel:
    def __init__(self) -> None:
        self.url = URL
        self.cookie = COOKIE
        self.decode_cookie = self.__decode_cookie()
        
    def __decode_cookie(self):
        aes = Aes(self.cookie)
        return aes.decrypt(self.cookie)