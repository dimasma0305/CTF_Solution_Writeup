
from pwn import *

libc = ELF('./libc.so.6')
libc = ROP(libc)

print(libc.find_gadget(["pop rdx", "ret"]))