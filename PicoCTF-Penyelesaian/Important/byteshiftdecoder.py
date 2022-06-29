from contextlib import suppress
huruf = 'VYGT}l4un-5tf+dj2gy+2d+e42tfQ'
for a in range(0,len(huruf),5):
    with suppress(Exception):
        print(chr(ord(huruf[a])-19),end="")
    with suppress(Exception):
        print(chr(ord(huruf[a+1])-5),end="")
    with suppress(Exception):
        print(chr(ord(huruf[a+2])-1),end="")
    with suppress(Exception):
        print(chr(ord(huruf[a+3])-2),end="")
    with suppress(Exception):
        print(chr(ord(huruf[a+4])-2),end="")

print
