# import package to ignore errors
from asyncio import exceptions
from contextlib import suppress
Enkripsi ='''.**.*.*.*.**
**.*.**.**
*.**.*.*.**
*.*.*.**.**
.**.*****
.**.*.***
*.***.***
.**.**.***
*.*.*.****
.*.*.*.***
****.***
.*.**.***
.*.*.*.***
.*****.**
.***.*.***
**.*.***
*.***.***
*.*.**.***
.*.*.*.***
**.**.***
.*****.**
.***.*.***
.**.*.***
*.***.***
**.*.***
****.***
.*****.**
.**.*.****
.**.*.***
*.*.*.****
.*.**.****
.*****.**
.**.**.***
**.*.***
*.***.***
.*.******'''

Enkripsi=Enkripsi.split('\n')
for i in range(len(Enkripsi)):
    # reverse Enkripsi[i]
    Enkripsi[i] = Enkripsi[i][::-1]
char_var0=0

decode_var=[]
print(Enkripsi)
for i in range(len(Enkripsi)):
    char_var1=1
    for j in range(len(Enkripsi[i])):
        if Enkripsi[i][j] == '*':
            char_var1=char_var1*2
        elif Enkripsi[i][j] == '.':
            char_var1=char_var1-1
            if char_var1==0:
                char_var1=char_var1+1
    char_var1=char_var1
    decode_var.append(char_var1)
for a in range(len(decode_var)):
    print(chr(decode_var[a]),end="")
        
            

            
# Tata cara enkripsi :
# Setiap jumlah ascii yang memiliki sifat genap, maka hasil result bertambah "*". Kemudian di bagi 2
# hasil += "*"
# ascii = ascii / 2
# Sedangkan jika ascii memiliki sifat ganjil, maka hasil result bertambah ".". kemudian ditambah 1
# hasil += "."
# ascii = ascii + 1
# Hal tersebut di lakukan sampai nilai ASCII menjadi 1
# Contoh : 
# "C" akan menjadi ".**.*.*.*.**"
# "T" akan menjadi "*.***.***"
# "F" akan menjadi "*.**.*.*.**"