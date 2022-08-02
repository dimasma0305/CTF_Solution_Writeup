
BLOCK = "\xc0\x87-\xee\x8b\xc9\x0b\x11V\x91;\x08\xa2#\xa3\x9e"
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
