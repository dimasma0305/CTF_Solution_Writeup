# Information

Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://mercury.picoctf.net/static/b4d62f6e431dc8e563309ea8c33a06b3/cat.jpg)

## Solving
Pakai ini untuk melihat extensi file yang sebenarnya
>file cat.jpg

buka terminal:
```
exiftool cat.jpg
```
cari kode yang mencurigakan seperti ini
>cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9

lalu encode pakai base64 di website
https://www.base64decode.org/
## Flag
picoCTF{the_m3tadata_1s_......}
## Referensi
https://infosecwriteups.com/beginners-ctf-guide-finding-hidden-data-in-images-e3be9e34ae0d