from PIL import Image
from string import printable
from itertools import chain

img=Image.open('challenge_pygame.png')
pixel=img.load()

width,height=img.size
flag='_'*64
c=0

len_flag=len(flag)
max_height=int(round(height/len_flag))

pr="CTFR0123456789abcdefghijklmnopqrstu{}_?"

fl=[]
for ch in range(0,720,11):
    for x in printable:
        p=pixel[12,ch+25]
        v=p[2]^p[1]
        f=ord(x)
        if f>=65 and f<=90:
            f+=30
        elif f>=97 and f<=122:
            f+=49
        else:
            f+=8
        banding=f^p[2]
        if banding==p[1]:
            fl.append(x)
            break
print(''.join(fl).replace("I","_").replace("KNZ","CTFR"))