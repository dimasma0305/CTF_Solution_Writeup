# Gambar Rusak
hilangkan "REMOVETHIS"

# Simpel Login

![](imgdump/Pasted%20image%2020220201071042.png)
```bash
curl -d "data[username]=admin&data[password]=a&data[target_password]=a" -X POST https://web.ctf.rasyidmf.com/chal14/
```
# Bukan SQL Injection
![](imgdump/Pasted%20image%2020220121112707.png)
![](imgdump/Pasted%20image%2020220121112752.png)
![](imgdump/Pasted%20image%2020220121112855.png)
# Salju
Disini saya menggunakan aplikasi bernama "stegsnow", download:
```
sudo apt install stegsnow
```
dan mengetikkan perintah
```
stegsnow -C solve.txt
```
# strcpy #1
disini saya menggunakan radare2
```
r2 strcpy
```
![](Pasted%20image%2020220121223429.png)maka akan terlihat beberapa string yang ada di dalam file, kemudian itu kita pilih dan sambungkan menjadi
CTFR{5tr_c0mp4r3_w1th_5strin9}
## Referensi
https://blog.d4rk5idehacker.or.id/2021/04/writeup-ctfr-strcpy-1-reversing.html
# strcpy #2
https://mrcyal.medium.com/writeup-ctfr-reverse-engineering-a38039bcf8da
# mall bogor
https://malbolge.doleczek.pl/ **clue**
# Substring JS
```
var flag = ""; if (flag.substring(0, 4) == "CTFR") { if (flag.substring(2, 7) == "FR{s1") { if (flag.substring(5, 10) == "s1mpl") { if (flag.substring(9, 13) == "l3_j") { if (flag.substring(10, 13) == "3_j") { if (flag.substring(13, 18) == "4v45c") { if (flag.substring(18, 26) == "r1pt}") { console.log("Here is your flag: " + flag); } } } } } } }

```
CTFR{s1mpl3_...}
# Cukup Copas
Eksploit 
```
preg_replace("/CTFR2020/", "", $data);
```
ex:
didimasmas
# Kocheng Poteh
gambar di dalam gambar
pakai formost
# Access Denied
```
Referer: https://www.hacker.com/
Cookie: status=admin
Accept: flag
Accept-Language: indonesia
```

```
curl -H 'Referer: https://www.hacker.com/' http://web.ctf.rasyidmf.com/chal19/ --cookie 'status=admin' -H 'Accept: flag' -H 'Accept-Language: indonesia'
```
## Referensi
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language
https://www.youtube.com/watch?v=tlafCw0edGs

# JS Brut3force
just guest it
CTFR{j5_brut3_f0rc3_1s_4m4z1ng}
# Huruf dan Angka
copas
http://www.unicode-symbol.com/u/0002.html
# Skripsi Mimin
use binwalk
# Eksekusi Code
$flag
# S1mpl3
use jsteg
# Pacar Laki-Laki
bf encryption
# JS Obfuscate 1
fOo('0X1') = 5_s4f3}
gabungkan mereka
#  Numeric Influence
zero in php still counted as number
# Troll Face
Least Significant Bit steganography is one **such technique in which least significant bit of pixels of the image is replaced with data bits**. This approach has the advantage that it is simplest one to understand, easy to implement and results in stego-images that contain embedded data as hidden.

https://wiki.bi0s.in/steganography/zsteg/
#  Penyuka Warna
## sql injection

```
SELECT * FROM items
WHERE owner = 'wiley'
AND itemname = 'name' OR 'a'='a';
```

```
' OR 'a'='a';
```

https://owasp.org/www-community/attacks/SQL_Injection
https://www.youtube.com/watch?v=af06TyUUfac
# Pop
```
gdb ./first_gdb
disas main
```

cari pop
# Authentication
https://www.md5hashgenerator.com/
?flag=[md5]
https://www.youtube.com/watch?v=6BIAJ1bYVVg

# Kawat Hiu 2
follow the tcp stream
# Salah Halaman
https://github.com/maurosoria/dirsearch
scan
# Sambungkan Request
https://www.ethic.ninja/2017/06/pengertian-remote-file-inclusion-rfi.html#:~:text=Remote%20File%20Incusion%20(RFI)%20adalah,akan%20dipanggil%20dan%20kemudian%20diproses.

https://www.youtube.com/watch?v=k5MEd4XmeQo

input
```
http://google.com
http://localhost
http://google.com
```
