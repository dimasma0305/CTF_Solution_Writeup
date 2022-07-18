
import sys, string


karakter = string.printable
def encryptMessage(key, message):
    # make bytes into ascii
    message = bytes.fromhex(message).decode()
    # make message list
    message = list(message)

    keyA=key//len(karakter)
    keyB=key%len(karakter)
    ciphertext = ''
    for i in range(len(message)):
        for a in range(9):
            symbolIndex = karakter.find(message[i])
            message[i] = karakter[(symbolIndex*keyA+keyB)%len(karakter)]
        ciphertext += message[i]
    return ciphertext
#key=int(sys.argv[1])
enc = encryptMessage(3711, "2a412a58316a3d6a41265f413c2658263626612657583577772a416a58762a21576a5f58614e575d583d6552582a412a587761264a413c265876512971374142523e3c42723e0d4142523e5742523e6077774f412f3e7e4f21572f5f3e52425f0d78")
print(enc)