
from pwn import *

libc = ELF('./libc.so.6')
libc = ROP(libc)

print(hex(libc.find_gadget(["pop rcx","ret"])[0]+0x7f7b9b351000))