# Shop
#### Description

Best Stuff - Cheap Stuff, Buy Buy Buy... Store Instance: [source](https://mercury.picoctf.net/static/d2c8c9ee59822de6776dd8f20af63b91/source). The shop is open for business at `nc mercury.picoctf.net 34938`.

## Hints
Always check edge cases when programming
## Solving
Di terminal ketik
```
nc mercury.picoctf.net 34938
```
belilah menggunakan angka negatif, maka kamu akan mendapatkan uang yang cukup untuk membeli flag.
```
Flag is:  [112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 98 97 54 98 56 99 100 102 125]
```
kamu akan mendapat pesan seperti ini setelah membeli flag.
kode diatas merupakan desimal, jadi untuk melihat kodenya kita memerlukan konverter desimal ke ascii. Disini saya menggunakan https://onlineasciitools.com/convert-decimal-to-ascii
## Flag
picoCTF{b4d_brogrammer_..........
## Referensi
https://github.com/vivian-dai/PicoCTF2021-Writeup/blob/main/Reverse%20Engineering/Shop/Shop.md