#!/usr/bin/env python3

from pwn import *
from struct import pack

exe = ELF("./vuln", checksec=False)

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

    def start(self):
        '''start the exploit'''
        proc : process = eval(self.process)
        if self.debug:
            script = """
            """
            gdb.attach(proc, gdbscript=script)
        proc.interactive()
        proc.close()

if __name__ == "__main__":
    Exploit().start()