# speeds and feeds
#### Description

There is something on my shop network running at `nc mercury.picoctf.net 7032`, but I can't tell what it is. Can you?

## Hints
What language does a CNC machine use?
## Solving
Di terminal jalankan
```
nc mercury.picoctf.net 7032
```
kita akan menemukan kode sepeti ini
```
G17 G21 G40 G90 G64 P0.003 F50
G0Z0.1
G0Z0.1
G0X0.8276Y3.8621
G1Z0.1
G1X0.8276Y-1.9310
G0Z0.1
G0X1.1034Y3.8621
G1Z0.1
G1X1.1034Y-1.9310
G0Z0.1
G0X1.1034Y3.0345
G1Z0.1
G1X1.6552Y3.5862
```
dilihat dari hint yang diberikan, ini adalah format untuk CNC machine, saya mencari di google "What language does a CNC machine use?", CNC machine menggunakan bahasa G-code, nah sekarang kita akan mengonvert kode-kode tadi menggunakan https://ncviewer.com/ , setelah itu akan terlihat flagnya

## Flag
picoCTF{num3r1cal_c0ntr0l_a067......
## Referensi
