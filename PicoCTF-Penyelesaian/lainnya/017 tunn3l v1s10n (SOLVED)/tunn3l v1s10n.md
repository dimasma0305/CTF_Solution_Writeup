# tunn3l v1s10n
#### Description

We found this [file](https://mercury.picoctf.net/static/da18eed3d15fd04f7b076bdcecf15b27/tunn3l_v1s10n). Recover the flag.
## Hints
Weird that it won't display right...
## Solving
Untuk melihat imagenya, saya menggunakan aplikasi ImageMagick
![](CTF/PicoCTF-Penyelesaian/lainnya/017%20tunn3l%20v1s10n%20(SOLVED)/Pasted%20image%2020211230082816.png)
dilihat dari gambar diatas hanya ada "notaflag{sorry}"
Karena tidak mendapatkan klue, saya menggunakan exiftool untuk melihat informasi gambar
```
exiftool tunn3l_v1s10n
```

```
ExifTool Version Number         : 11.88
File Name                       : tunn3l_v1s10n
Directory                       : .
File Size                       : 2.8 MB
File Modification Date/Time     : 2021:12:30 07:17:50+08:00
File Access Date/Time           : 2021:12:30 07:27:46+08:00
File Inode Change Date/Time     : 2021:12:30 07:26:09+08:00
File Permissions                : rw-rw-r--
File Type                       : BMP
File Type Extension             : bmp
MIME Type                       : image/bmp
BMP Version                     : Unknown (53434)
Image Width                     : 1134
Image Height                    : 306
Planes                          : 1
Bit Depth                       : 24
Compression                     : None
Image Length                    : 2893400
Pixels Per Meter X              : 5669
Pixels Per Meter Y              : 5669
Num Colors                      : Use BitDepth
Num Important Colors            : All
Red Mask                        : 0x27171a23
Green Mask                      : 0x20291b1e
Blue Mask                       : 0x1e212a1d
Alpha Mask                      : 0x311a1d26
Color Space                     : Unknown (,5%()
Rendering Intent                : Unknown (826103054)
Image Size                      : 1134x306
Megapixels                      : 0.347
```
diatas bisa dilihat bahwa file "tunn3l_v1s10n" merupakan image berformat BMP, dan memiliki size 2,8 mb yang terbilang besar untuk ukuran gambar 1134x306.

karena file size dari gambar ini mencurigakan, saya mencoba untuk memperbesar gambarnya dengan menambahkan height di hex gambar tersebut. Saya menggunakan tool ghex
![](CTF/PicoCTF-Penyelesaian/lainnya/017%20tunn3l%20v1s10n%20(SOLVED)/Pasted%20image%2020211230085320.png)
Saya mengubah height-nya di ofset 0017h dari 0x01 menjadi 0x03.Buka lagi file-nya menggunakan ImageMagick, maka akan terlihat flag-nya
## Flag
picoCTF{qu1t3_a_v.........
## Referensi
http://www.ece.ualberta.ca/~elliott/ee552/studentAppNotes/2003_w/misc/bmp_file_format/bmp_file_format.htm
http://www.novell.com/documentation/ndsv8/usnds/c1help/novell_common/hexeditor.html
https://github.com/vivian-dai/PicoCTF2021-Writeup/blob/main/Forensics/tunn3l%20v1s10n/tunn3l%20v1s10n.md
https://qiita.com/housu_jp/items/bb0d41be153e7ee2b148
https://github.com/vivian-dai/PicoCTF2021-Writeup/blob/main/Forensics/tunn3l%20v1s10n/tunn3l%20v1s10n.md