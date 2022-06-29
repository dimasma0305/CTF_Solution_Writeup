# The Numbers
#### Description

The [numbers](https://jupiter.challenges.picoctf.org/static/f209a32253affb6f547a585649ba4fda/the_numbers.png)... what do they mean?
## Hints
The flag is in the format PICOCTF{}
## Solving
dilihat dari angka di gambar tersebut
![](CTF/PicoCTF-Penyelesaian/lainnya/026%20The%20Numbers%20(SOLVED)/the_numbers.png)
angka tersebut merupakan urutan dari alphabet
- 16 = p
- 9 = i
- 3 = c
- 15 = o
nah, untuk mempercepat proses pen-decode-an saya membuat program python
```
key = (16,9,3,15,3,20,6,0,20,8,5,14,21,13,2,5,18,19,13,1,19,15,14,0)

alp = ("{abcdefghijklmnopqrstuvwxyz")

  

for a in key:

	print(alp[a], end="")

	print()
```
jalankan, dan anda akan menemukan flagnya
## Flag
picoctf{thenumbe.........
## Referensi
