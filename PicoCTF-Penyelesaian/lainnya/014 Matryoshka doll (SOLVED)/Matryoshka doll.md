# Matryoshka doll
#### Description

Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](https://mercury.picoctf.net/static/5ef2e9103d55972d975437f68175b9ab/dolls.jpg)
## Hints
- Wait, you can hide files inside files? But how do you find them?
- Make sure to submit the flag as picoCTF{XXXXX}
## Solving
### Steps
```
binwalk dolls.png 
```
Kita akan melihat
![](CTF/PicoCTF-Penyelesaian/lainnya/014%20Matryoshka%20doll%20(SOLVED)/Screenshot%20from%202021-12-28%2017-22-51.png)
Nah disitu kita akan melihat beberapa file yang disisipkan disisipkan di gambar itu.
```
binwalk -e dolls.png
```
Perintah diatas akan mengekstrak semua file yang ada di gambar tersebut. Kemudian kita buka <code>"_dolls.png.extracted"</code> , buka "base_images" kita extrak lagi gambar yang ada di folder tersebut menggunakan perintah
```
binwalk -e dolls.png
```
ulangi step di atas sampai kalian menemukan "flag.txt" yang didalamnya akan ada flag
## Flag
picoCTF{e3f378fe6c1ea7f..........}
## Command example
Merubah nama agar gambarnya bisa dilihat
```
mv dolls.jpg dolls.png
```
Mengekstrak semua yang terlist di decimal
```
binwalk --dd='.*' dolls.jpg
```
## Referensi
