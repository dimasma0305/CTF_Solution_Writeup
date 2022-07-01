
BLOCK = "\xdc\x84r\x8f\xdc\xf8\x9d\x93u\x1d\x10\xa7\xc7\\\x8c\xf2"
print("Len Block: "+str(len(BLOCK)))


def genkey(enc):
    key = ''
    block = ''
    for i in range(0, len(enc)):
        for j in range(300):
            xor = ord(enc[i]) ^ j
            if chr(xor) == "a":
                key += "{0:02x}".format(j)
                break
    print("key: " + key)


def byt2hex(byt):
    dec = ''
    for i in range(len(byt)):
        dec += "{0:02x}".format(ord(byt[i]))
    print("hex: "+dec)


def decode(key):
    xor = ''
    for i in range(0, 16):
        xor += chr(ord(BLOCK[i]) ^ key[i])
    print(xor)


genkey(BLOCK)
byt2hex(BLOCK)
