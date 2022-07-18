from pwn import *
from PIL import Image

img=Image.open('warnawarni2.png')
pix=img.load()
#print(pix[0,0])
#print(pix[0,1])
#print(pix[0,2])
#print(pix[0,3])

width, height = img.size

res=[]

for x in range(width):
    for y in range(height):
        if pix[x,y][0]==127 and pix[x,y][2]==127:
            res.append(pix[x,y][1])
# disamble the chr(res)
print(disasm(bytes(res), arch='amd64'))
