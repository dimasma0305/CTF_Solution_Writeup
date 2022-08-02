#!/usr/bin/env python3

from pwn import *

exe = ELF("./vuln_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.27.so")

context.binary = exe
context.log_level = "CRITICAL"
context.terminal = ["konsole", "-e"]

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
            script = """
            """
            gdb.attach(proc, gdbscript=script)
        proc.interactive()

    def start(self):
        '''start the exploit'''
        with eval(self.process) as r:
            self.conn(r)


Exploit(local=True, debug=True).start()
