import random
encrypted = open("encrypt.txt", "r").read()
encrypt = ""
for x in encrypted:
    p = random.randint(0, 14)
    encrypt += chr(ord(x) + p)

print encrypt