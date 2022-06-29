# Wireshark doo dooo do doo...
#### Description

Can you find the flag? [shark1.pcapng](https://mercury.picoctf.net/static/ea41c400c3c7b4a63406e5e607d362ab/shark1.pcapng).

---

## Hints

## Solving
Download filenya, kemudian buka dengan wireshark. Klik anlyze > follow > tcp stream. pilih chanel 5
![](CTF/PicoCTF-Penyelesaian/lainnya/030%20Wireshark%20doo%20dooo%20do%20doo...%20(SOLVED)/Screenshot%20from%202022-01-01%2007-02-01.png)
disini kita alan melihat isi packetnya, yaitu "Gur..." kita konversikan dari rot13 menjadi ascii
## Flag
picoCTF{p33kab00_1_s33_...........
## Referensi
https://github.com/vivian-dai/PicoCTF2021-Writeup/blob/main/Forensics/Wireshark%20doo%20dooo%20do%20doo/Wireshark%20doo%20dooo%20do%20doo.md