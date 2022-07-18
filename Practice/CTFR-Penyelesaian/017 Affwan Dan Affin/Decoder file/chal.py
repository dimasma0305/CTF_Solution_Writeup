import sys, string, binascii

karakter = string.printable
# print(len(karakter))

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def getKeyParts(key):
    keyA = key // len(karakter)
    keyB = key % len(karakter)
    return (keyA, keyB)

def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        sys.exit('Jika kunci A=1 Enkripsi terlalu lemah, silahkan pilih kunci lain')
    if keyB == 0 and mode == 'encrypt':
        sys.exit('Jika kunci B=0 Enkripsi terlalu lemah, silahkan pilih kunci lain')
    if keyA < 0 or keyB < 0 or keyB > len(karakter) - 1:
        sys.exit('Kunci A harus lebih besar dari 0 dan Kunci B harus berada diantara 0 dan %s.' % (len(karakter) - 1))
    if gcd(keyA, len(karakter)) != 1:
        sys.exit('Kunci A (%s) dengan jumlah karakter (%s) secara relative bukan angka prima. Pilih Kunci lain.' % (keyA, len(karakter)))

def encryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    #print(keyA)
    ciphertext = ''
    for symbol in message: # symbol=H
        if symbol in karakter:
            symbolIndex = karakter.find(symbol) # output=43
            #print(karakter[symbolIndex])
            #print(symbolIndex)
            s = karakter[(symbolIndex * keyA + keyB) % len(karakter)]
            #print((symbolIndex * keyA + keyB) % len(karakter))
            print(s)
            #print((symbolIndex*keyA+keyB))
            ciphertext += s
        else:
            ciphertext += symbol
    return binascii.hexlify(ciphertext.encode())

enc = encryptMessage(1990, "Halo Affwan")
print(enc)