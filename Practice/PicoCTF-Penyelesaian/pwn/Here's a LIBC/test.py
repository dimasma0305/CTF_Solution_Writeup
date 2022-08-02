from pwn import *
from struct import pack

exe = ELF("./vuln_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.27.so")

rop = ROP(exe)

print(rop.find_gadget(['pop rdi', 'ret']))
print(next(libc.search(b"/bin/sh")))
print(rop.find_gadget(['pop rdi', 'ret']))