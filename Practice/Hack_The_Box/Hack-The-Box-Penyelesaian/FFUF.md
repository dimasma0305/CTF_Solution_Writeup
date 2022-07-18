#FFUF


```sh
ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/Common-PHP-Filenames.txt -u http://159.65.92.13:32381/blog/FUZZ
```

---

```sh
sudo sed -i 's/^\#.*$//g' /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-small.txt && sudo sed -i '/^$/d' /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-small.txt
```

---

```sh
ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-small.txt -u http://159.65.92.13:31600/forum/FUZZ -e .php
```

```sh
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://159.65.92.13:31600/FUZZ -recursion -recursion-depth 1 -e .php -v
```

---

```sh
ffuf -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u https://FUZZ.hackthebox.eu/
```

---

```sh
ffuf -w /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u http://academy.htb:PORT/ -H 'Host: FUZZ.academy.htb'
```

---

```sh
sudo sh -c 'echo "159.65.92.13  academy.htb" >> /etc/hosts'
ffuf -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u http://academy.htb:30418/ -H 'Host: FUZZ.academy.htb' -fs 986
```

---

```sh
ffuf -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u http://academy.htb:31427/ -H 'Host: FUZZ.academy.htb' -fs 986

ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt -u http://academy.htb:31427/FUZZ -H 'Host: admin.academy.htb' -fs 986
```

- menggunakan firefox developer edition untuk melihat admin.php

```sh
ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/burp-parameter-names.txt -u http://academy.htb:31427/admin/admin.php\?FUZZ\=1 -H 'Host: admin.academy.ht  
b' -fs 798
```

---

```sh
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://admin.academy.htb:PORT/admin/admin.php -X POST -d 'FUZZ=key' -H 'Content-Type: application/x-www-form-urlencoded' -fs xxx
```

```sh
curl http://admin.academy.htb:PORT/admin/admin.php -X POST -d 'id=key' -H 'Content-Type: application/x-www-form-urlencoded'
```

---

```sh
ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/burp-parameter-names.txt -u http://academy.htb:31427/admin/admin.php -X POST -d 'FUZZ=1' -H 'Host: admin.academy.htb' -H 'Content-Type: application/x-www-form-urlencoded' -fs 798
```

```sh
curl http://academy.htb:31427/admin/admin.php -X POST -d 'id=1' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Host: admin.academy.htb'
```

```sh
for i in {1..1000}; do;echo "$i" >> num.txt;done
```

```sh
ffuf -w ./num.txt -u http://academy.htb:30318/admin/admin.php -X POST -d 'id=FUZZ' -H 'Host: admin.academy.htb' -H 'Content-Type: application/x-www-form-url  
encoded' -fs 768
```

```sh
curl http://academy.htb:30318/admin/admin.php -X POST -d 'id=73' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Host: admin.academy.htb'
```

---

```sh
ffuf -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u http://academy.htb:30084/ -H 'Host: FUZZ.academy.htb' -fs 985
```

`/etc/host`
```sh
159.65.92.13  academy.htb
159.65.92.13  archive.academy.htb
159.65.92.13  test.academy.htb
159.65.92.13  faculty.academy.htb
```

```sh
ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/web-extensions.txt:FUZZ -u http://faculty.academy.htb:30084/courses/indexFUZZ
```

```sh
ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-small.txt -u http://faculty.academy.htb:30084/courses/FUZZ.php7 -t 1000
```

```url
http://faculty.academy.htb:30084/courses/linux-security.php7
```

```sh
ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/burp-parameter-names.txt -u http://faculty.academy.htb:30084/courses/linux-security.php7\?FUZZ\=  
1 -fs 774 -t 1000
```

```sh
ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/burp-parameter-names.txt -u http://faculty.academy.htb:30084/courses/linux-security.php7 -fs 774 -t 1000 -X POST -d 'FUZZ=1' -H 'Content-Type: application/x-www-form-urlencoded'
```

```sh
curl http://faculty.academy.htb:30084/courses/linux-security.php7 -X POST -d 'username=1' -H 'Content-Type: application/x-www-form-urlencoded'
```

```sh
ffuf -w /usr/share/wordlists/seclists/Usernames/xato-net-10-million-usernames.txt -u http://faculty.academy.htb:30084/courses/linux-security.php7 -fs 781 -X  
POST -d 'username=FUZZ' -H 'Content-Type: application/x-www-form-urlencoded' -t 100
```

```sh
curl http://faculty.academy.htb:30084/courses/linux-security.php7 -X POST -d 'username=harry' -H 'Content-Type: application/x-www-form-urlencoded'
```