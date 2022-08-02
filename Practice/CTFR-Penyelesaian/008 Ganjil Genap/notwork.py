# import package to ignore errors
from asyncio import exceptions
from contextlib import suppress
from imp import source_from_cache
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
print(Enkripsi)
var_range = range(1, 128)
var_range = list(var_range)
new_var = var_range
new_var2 = []
for i in range(len(Enkripsi)):
    for j in range(len(Enkripsi[i])):
        # var range is an int in range 1 - 120
        loop_range = var_range
        for a in range(len(Enkripsi[i])):
            if Enkripsi[i][a]=='*':
                # remove all the odd number in loop_range list
                for b in range(len(loop_range)):
                    with suppress(IndexError):
                        if loop_range[b]%2!=0:
                            loop_range[b+1] = loop_range[b+1]/2
                            new_var.remove(loop_range[b])
                            loop_range.remove(loop_range[b])

            elif Enkripsi[i][a]=='.':
                # remove all the even number in loop_range list
                for b in range(len(loop_range)):
                    with suppress(IndexError):
                        if loop_range[b]%2==0:
                            loop_range[b+1] = loop_range[b-1]+1
                            new_var.remove(loop_range[b])
                            loop_range.remove(loop_range[b])
        new_var2+=new_var

for a in range(len(new_var2)):
    print(chr(new_var2[a]),end="")

            
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