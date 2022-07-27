import pwn

p = pwn.remote("mercury.picoctf.net", 64260)

(p.recvuntil(b"What data would you like to encrypt?").decode())
p.sendline(b"\x00"*(50000-32))
(p.recvuntil(b"What data would you like to encrypt?").decode())
p.send(b"\x00"*33)
p.recvline()
key = p.recvline()