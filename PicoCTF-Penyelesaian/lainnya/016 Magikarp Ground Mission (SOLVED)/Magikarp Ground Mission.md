# Magikarp Ground Mission
#### Description

Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `6d448c9c`
## Hints
Finding a cheatsheet for bash would be really helpful!
## Solving
pertama kita hidupkan "on demand isntance" yang diberikan.
setelah itu jalankan ssh
```
ssh ctf-player@venus.picoctf.net -p 55468
```
```
ctf-player@venus.picoctf.net's password: 
```
masukkan password:
```
6d448c9c
```
setelah itu jalankan ls untuk melihat apa yang ada di direktori instance tersebut

```
ctf-player@pico-chall$ ls
1of3.flag.txt  instructions-to-2of3.txt
ctf-player@pico-chall$ cat instructions-to-2of3.txt 
Next, go to the root of all things, more succinctly `/`
ctf-player@pico-chall$ cat 1of3.flag.txt 
```
ikuti instruksi di setiap file yang ada di instance tersebut, dan temukan "flag.txt".
## Flag
picoCTF{xxsh_0ut_0f_\/\/4t........}