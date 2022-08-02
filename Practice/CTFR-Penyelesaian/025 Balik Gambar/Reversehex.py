#import image viewer
import os
import sys
# open a file as hex bin
a = open("balikgambarnya.png", "br")
b = a.read()
# reverse the image binary
c = b[::-1]
# save the reversed image
d = open("balikgambarnya.png", "bw")
d.write(c)
# open image with image viewer
os.system("hexdump -C balikgambarnya.png")
# close the file
a.close()