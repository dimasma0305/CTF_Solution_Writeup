
from pwn import *

context.clear(arch='i386')
context.terminal = ['konsole', '-e']
binary = ELF("./libc.so.6")
binary.symbols = {'read': 0xdeadbeef, 'write': 0xdecafbad, 'execve': 0xcafebabe, 'exit': 0xfeedface}
rop = ROP(binary)

print(rop.find_gadget(['pop eax', 'ret']).address)