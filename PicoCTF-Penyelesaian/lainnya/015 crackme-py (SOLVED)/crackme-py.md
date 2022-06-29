# crackme-py
#### Description

[crackme.py](https://mercury.picoctf.net/static/fd0e358d4b82695c220c0d6013c11484/crackme.py)

---
## Hints

## Solving
Buka file crackme.py, bisa dilihat dibawah ada variabel bezoz_cc_secret yang merupakan flag yang sudah di encode.
```
# Hiding this really important number in an obscure piece of code is brilliant!
# AND it's encrypted!
# We want our biggest client to know his information is safe with us.
bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE055a4ce`eN"

# Reference alphabet
alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"



def decode_secret(secret):
    """ROT47 decode

    NOTE: encode and decode are the same operation in the ROT cipher family.
    """

    # Encryption key
    rotate_const = 47

    # Storage for decoded secret
    decoded = ""

    # decode loop
    for c in secret:
        index = alphabet.find(c)
        original_index = (index + rotate_const) % len(alphabet)
        decoded = decoded + alphabet[original_index]

    print(decoded)

```
Bisa dilihat di bagian loop "for c in secret:" kita bisa menyimpulkan bahwa itu adalah loop untuk mendecode code "<code>bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE055a4ce`eN"</code>".

Cara men-encode ini cukup simple, kita perlu mengganti baris terakhir
```
choose_greatest()
```
menjadi
```
decode_secret("A:4@r%uL`M-^M0c0AbcM-MFE055a4ce`eN")
```
agar program men-execute fungsi "decode_secret" dan mendecode value yang ada di variabel "bezos_cc_secret"
## Flag
```
picoCTF{1|\/|_4_p34|\|u.......}
```
## Referensi
