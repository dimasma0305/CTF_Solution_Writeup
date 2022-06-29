# Transformation
I wonder what this really is... [enc](https://mercury.picoctf.net/static/2b4cea9b07db22bf4f933fddd1b8caa9/enc) `''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`
## Solving
terminal
>cat enc

output:
>灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰㑣〷㘰摽

hint:
```
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`
```
bisa dilihat dari hint di atas bahwa kode yang diberikan di encode dengan bahasa python, oleh karena itu untuk men-decodenya kita perlu mereverse logika kode diatas.

setelah mereversing logika kode tersebut, kita membuat program untuk men-decode `灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰㑣〷㘰摽` kode disamping.

Python:

```
flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰㑣〷㘰摽"

for i in range(len(flag)):

	print(chr(ord(flag[i])>>8),end="")

	print(chr((ord(flag[i]))-((ord(flag[i])>>8)<<8)),end="")

  
print("\n")
```
Jalankan, lalu akan ketemu flagnya.

>**Penjelasan kasar**
>Program mengonversikan huruf ke-i menjadi dua huruf,
>huruf pertama diperoleh dari huruf ke-i yang di shift 8 bit ke kanan,
>dan huruf kedua diperoleh dari huruf ke-i dikurangi huruf ke-i yang sudah di shift 8 bit ke kanan lalu 8 bit kekiri. 
## Flag
picoCTF{16_bits_inst34d_of_8_0......}
## Referensi
https://github.com/vivian-dai/PicoCTF2021-Writeup/blob/main/Reverse%20Engineering/Transformation/Transformation.md
https://vishnuram1999.github.io/transformation_pico_ctf_2021.html