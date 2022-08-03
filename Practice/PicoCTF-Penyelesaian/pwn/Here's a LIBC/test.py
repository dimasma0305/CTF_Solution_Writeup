from pwn import *

checksec = False

exe = ELF("./vuln_patched", checksec=checksec)
libc = ELF("./libc.so.6", checksec=checksec)
ld = ELF("./ld-2.27.so", checksec=checksec)

rop_exe = ROP(exe)
rop_libc = ROP(libc)
rop_ld = ROP(ld)

print(exe.got) # Global Offset Table of exe
print(exe.plt) # Procedure Linkage Table of exe

print(rop_exe.find_gadget(['pop rdi', 'ret'])) 
print(rop_libc.find_gadget(['pop rdi', 'ret'])) 
print(rop_ld.find_gadget(['pop rdi', 'ret'])) 

print(exe.symbols["puts"])
print(libc.symbols["puts"])
print(ld.symbols)