# MacroHard WeakEdge
#### Description

I've hidden a flag in this file. Can you find it? [Forensics is fun.pptm](https://mercury.picoctf.net/static/c0da20f29337e87ffb58ea987d8c596e/Forensics%20is%20fun.pptm)

## Hints


## Solving
Menggunakan binwalk
```
binwalk -e Forensics\ is\ fun.pptm
```
cari file yang bernama hiden, klik maka akan ketemu
```
Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q
```
decode menggunakan base64 ke ascii
## Flag
picoCTF{D1d_u_kn0w_ppt........
## Referensi
