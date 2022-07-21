
import base64
import json
from urllib.parse import unquote_plus
from Crypto.Cipher import AES
from itsdangerous import base64_decode
from phpserialize import loads
import hashlib
import hmac


KEY = "cgxs+3SOT4QBcNDUWBOA5/FoS/Tao9k5y2vHTP3lP0E="
COOKIE = "eyJpdiI6InkyRmpwUGt6dkhTbjdzbERrM1ZWWWc9PSIsInZhbHVlIjoiK2RXS3M4RVlpOTZndE9MSkVsWDdlcXJ0ZnJ0TWM0TEdzTFFMeWo2TzBUV21HXC9UQmsxNWE0YWdvZHIwM0VpZ0oiLCJtYWMiOiJjZjRiNmE4OWIyNzlmNmQ1NjY5NmM0MGI1ODQyZTg2MmI5YzI4ZTYyNDJlZmFmM2VlMTE1NWE1NmI1YTQ0ZjZkIn0%3D"

def decrypt(payload, key):
    """
    Decrypt strings that have been encrypted using Laravel's encrypter (AES-256 encryption).
    Plain text is encrypted in Laravel using the following code:
    >>> ciphertext = Crypt::encrypt('hello world');
    The ciphertext is a base64's json-encoded array consisting of the following keys:
       [
          'iv' => 'generated initialization vector (iv)',
          'value' => 'encrypted, base64ed, signed value',
          'mac'  => 'message authentication code (mac)'
       ]
    The 'value' is signed using a message authentication code (MAC) so verify that the value has not changed during
    transit.
    Parameters:
    payload (str): Laravel encrypted text.
    key (str): Encryption key (base64 decoded). Make sure 'base64:' has been removed from string.
    Returns:
    str: plaintext
    """

    data = json.loads(base64.b64decode(payload))
    if not valid_mac(key, data):
        print(key)
        return None

    value = base64.b64decode(data['value'])
    iv = base64.b64decode(data['iv'])

    return unserialize(mcrypt_decrypt(value, iv, key)).decode("utf-8")

def mcrypt_decrypt(value, iv, key):
    AES.key_size=128
    crypt_object=AES.new(key=key,mode=AES.MODE_CBC,IV=iv)
    return crypt_object.decrypt(value)

def unserialize(serialized):
    return loads(serialized)

def valid_mac(key, data):
    dig = hmac.new(key, digestmod=hashlib.sha256)
    dig.update(data['iv'].encode('utf8'))
    dig.update(data['value'].encode('utf8'))
    dig = dig.hexdigest()
    return dig==data['mac']

print(decrypt(unquote_plus(COOKIE), base64.b64decode(KEY).decode('latin-1')))