# Easy Peasy
#### Description

A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{}) `nc mercury.picoctf.net 64260` [otp.py](https://mercury.picoctf.net/static/338fdafc11b7fbfb9cca5edac5085d05/otp.py)
## Hints
Maybe there's a way to make this a 2x pad.
## Solving
Saat dijalankan menggunakan netcat akan terlihat encrypted flag-nya, dan jika kita menginputkan string hasil enkripsinya akan dikembalikan
```
nc mercury.picoctf.net 64260 
```

```
******************Welcome to our OTP implementation! ****************** 

This is the encrypted flag! 51466d4e5f575538195551416e4f5300413f1b5008684d5504384157046e4959

What data would you like to encrypt? hello 
Here ya go! 
582b301457

What data would you like to encrypt? hello 
Here ya go! 
5939145c0d

What data would you like to encrypt?
```
Jika Anda memeriksa pemrosesan otp.py, Anda dapat melihat bahwa itu dienkripsi dengan XOR.

Kunci XOR disiapkan untuk 50.000 byte. Itu dikonsumsi setiap kali dienkripsi, dan ketika mencapai 50.000 byte, ia kembali ke awal.
```python
#!/usr/bin/python3 -u
import os.path

KEY_FILE = "key"
KEY_LEN = 50000
FLAG_FILE = "flag"


def startup(key_location):
	flag = open(FLAG_FILE).read()
	kf = open(KEY_FILE, "rb").read()

	start = key_location
	stop = key_location + len(flag)

	key = kf[start:stop]
	key_location = stop

	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), flag, key))
	print("This is the encrypted flag!\n{}\n".format("".join(result)))

	return key_location

def encrypt(key_location):
	ui = input("What data would you like to encrypt? ").rstrip()
	if len(ui) == 0 or len(ui) > KEY_LEN:
		return -1

	start = key_location
	stop = key_location + len(ui)

	kf = open(KEY_FILE, "rb").read()

	if stop >= KEY_LEN:
		stop = stop % KEY_LEN
		key = kf[start:] + kf[:stop]
	else:
		key = kf[start:stop]
	key_location = stop

	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), ui, key))

	print("Here ya go!\n{}\n".format("".join(result)))

	return key_location


print("******************Welcome to our OTP implementation!******************")
c = startup(0)
while c >= 0:
	c = encrypt(c)
```
Panjang string flag adalah 32 byte, jadi pertama-tama masukkan string 50000 --32 byte untuk menghabiskan kuncinya. Anda kemudian dapat \x00 encrypt 32 byte untuk mengidentifikasi kunci yang awalnya digunakan.
```
python3 -c "print ('A' * (50000-32) +'\ n'+' \ x00' * 32)" | nc mercury.picoctf.net 64260 

<snip>

What data would you like to encrypt? Here ya go! 62275c786663615c783165725c786237225c7863315c7831375c7861305c7838
What data would you like to encrypt?
```
Sekarang kamu akan mengidentifikasi key-nya, kamu bisa men-decryted kuncinya menggunakan XOR cipher menggunakan [Cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'Hex','string':'62275c786663615c783165725c786237225c7863315c7831375c7861305c7838'%7D,'Standard',false)&input=NTE0NjZkNGU1ZjU3NTUzODE5NTU1MTQxNmU0ZjUzMDA0MTNmMWI1MDA4Njg0ZDU1MDQzODQxNTcwNDZlNDk1OQ)
![](CTF/PicoCTF-Penyelesaian/lainnya/018%20Easy%20Peasy%20(SOLVED)/Pasted%20image%2020211230143113.png)
## Flag
picoCTF{3a16944dad432717ccc3945d..........
## Referensi
https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'Hex','string':'62275c786663615c783165725c786237225c7863315c7831375c7861305c7838'%7D,'Standard',false)&input=NTE0NjZkNGU1ZjU3NTUzODE5NTU1MTQxNmU0ZjUzMDA0MTNmMWI1MDA4Njg0ZDU1MDQzODQxNTcwNDZlNDk1OQ
https://github.com/Dvd848/CTFs/blob/master/2021_picoCTF/Easy_Peasy.md
https://dev.to/dandan/picoctf-2021-easy-peasy-writeup-paf
https://tsalvia.hatenablog.com/entry/2021/04/08/110000#Easy-Peasy---40-points