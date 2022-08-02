# open file dot
enc=open("dot.txt","r").read().split(" ")
for i in range(len(enc)):
    print(chr(len(enc[i])),end="")