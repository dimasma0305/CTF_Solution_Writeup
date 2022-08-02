cipher_text = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_MAZyqFQj}"
for i in cipher_text:
    if i.isupper():
        print(chr((ord(i) - ord('A') - 13) % 26 + ord('A')), end='')
        continue
    if i.islower():
        print(chr((ord(i) - ord('a') - 13) % 26 + ord('a')), end='')
        continue
    print(i, end='')
    
# out: picoCTF{next_time_I'll_try_2_rounds_of_rot13_ZNMldSDw}