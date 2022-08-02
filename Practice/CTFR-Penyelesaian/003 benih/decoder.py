import random
# encoding unicode_
with open("encrypt.txt",'rb') as f:
    encrypted = f.read()
    print(encrypted)
    encrypt = ""
    random.seed('CTFR')
    for x in encrypted:
        encrypt += chr(ord(x) - random.randrange(0, 15))

    print(encrypt)