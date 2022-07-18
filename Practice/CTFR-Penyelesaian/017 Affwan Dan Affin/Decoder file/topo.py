import sys, string, binascii
karakter = string.printable
key=1990
message="7"
# jika H adalah output
keyA=1990//len(karakter)
#print(keyA)
keyB=1990%len(karakter)
#print(keyB)
#print(karakter)

for i in range(1):
    symbolIndex = karakter.find(message[0])
    message=karakter[(symbolIndex * keyA + keyB) % len(karakter)]

print(message)
#print(symbolIndex)
#print(karakter[(symbolIndex * keyA + keyB) % len(karakter)])
#print(karakter[(symbolIndex * 19 + 90) % 100])
# make below statement become true
#print(43==(symbolIndex + len(karakter)))
#print((symbolIndex*keyA+keyB)%len(karakter))