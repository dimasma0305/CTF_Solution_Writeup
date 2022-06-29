# keygenme-py
## Description

[keygenme-trial.py](https://mercury.picoctf.net/static/a6d9cac3bfa4935ceb50c145d3ff5586/keygenme-trial.py)
## Hints

## Solving
Pertama buka file keygenme-trial.py
disitu kita bisa melihat kode
![](CTF/PicoCTF-Penyelesaian/lainnya/013%20keygenme-py%20(SOLVED)/Screenshot%20from%202021-12-23%2023-55-45.png)
disini saya bisa mengambil kesimpulan bahwa flag tersusun dari
```
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
```
kalau kita susun menjadi "picoCTF{1n_7h3_|<3y_of_xxxxxxxx}" disitu saya mencoba untuk memasukkan flagnya, tapi hasilnya nihil. Saya mengambil kesimpulan bahwa "xxxxxxxx" merupakan banyak digit dari program tersebut.
Setelah saya menelusuri apa saja yang memakai variable "key_part_static1_trial", "key_part_dynamic1_trial", "key_part_static2_trial", dan "key_full_template_trial". Saya menemukan fungsi "check_key" yang memakai variabel global "key_full_template_trial"
![](CTF/PicoCTF-Penyelesaian/lainnya/013%20keygenme-py%20(SOLVED)/Screenshot%20from%202021-12-24%2008-27-34.png)
dalam baris tersebut saya menemukan variabel "username_trial" dan dibaris itu saya juga menemukan perintah hexdigest yang berjumlah 8 sama dengan digit "xxxxxxxx".
Saya mencari variabel "username_trial"
![](CTF/PicoCTF-Penyelesaian/lainnya/013%20keygenme-py%20(SOLVED)/Screenshot%20from%202021-12-24%2008-42-32.png)
disitu variabel "username_trial" memiliki value "PRITCHARD".
![](CTF/PicoCTF-Penyelesaian/lainnya/013%20keygenme-py%20(SOLVED)/Pasted%20image%2020211224085333.png)
di fungsi "check_key" kita bisa lihat bahwa value variabel "username_trial" di konvert menjadi sha256. Saya konversikan dulu "PRITCHARD" ke sha256 kemudian saya membuat program python dibawah:
```a
# sha didapat dari konversi "PRITCHARD" ke sha256

sha = "496e54f222f256b023f33cdda0270853f39d7bf24fa1ca6b72d4b4fd1a9cae56"

# nomor 4, 5, 6, dan seterusnya diperoleh dari "hexdigest()" di function "check_key"

print(sha[4] + sha[5] + sha[3] + sha[6] + sha[2] + sha[7] + sha[1] + sha[8])
```
nah, kemudian akan keluar outputnya "54ef6292" kita ganti "xxxxxxxx" dengan outputnya, dan kita akan mendapatkan flagnya.
### Merubah ascii menjadi sha256 hash
kita bisa menggunakan website:
https://timestampgenerator.com/generate-hash/sha256
masukkan
```a
PRITCHARD
```
menjadi
```a
496e54f222f256b023f33cdda0270853f39d7bf24fa1ca6b72d4b4fd1a9cae56
```
## Flag
picoCTF{1n_7h3_|<3y_of_54e.......}
## Referensi
