# Enkripsi :
# .**.*.*.*.**
# **.*.**.**
# *.**.*.*.**
# *.*.*.**.**
# .**.*****
# .**.*.***
# *.***.***
# .**.**.***
# *.*.*.****
# .*.*.*.***
# ****.***
# .*.**.***
# .*.*.*.***
# .*****.**
# .***.*.***
# **.*.***
# *.***.***
# *.*.**.***
# .*.*.*.***
# **.**.***
# .*****.**
# .***.*.***
# .**.*.***
# *.***.***
# **.*.***
# ****.***
# .*****.**
# .**.*.****
# .**.*.***
# *.*.*.****
# .*.**.****
# .*****.**
# .**.**.***
# **.*.***
# *.***.***
# .*.******

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