# Mind your Ps and Qs
In RSA, a small `e` value can be problematic, but what about `N`? Can you decrypt this? [values](https://mercury.picoctf.net/static/51d68e61bb41207a55f24e753f07c5a3/values)

## Hints
1. Bits are expensive, I used only a little bit over 100 to save money

## Solving
>cat values

Maka akan keluar output:
>Decrypt my super sick RSA:
>c:62324783949134119159408816513334912534343517300880137691662780895409992760262021
>n:1280678415822214057864524798453297819181910621573945477544758171055968245116423923
>e:65537
### Mendapatkan Phi(n) dari konverter online
kita akan mencari Euler's notion-nya di https://www.alpertron.com.ar/ECM.HTM
hasilnya:
![](CTF/PicoCTF-Penyelesaian/lainnya/010.%20Mind%20your%20Ps%20and%20Qs%20(SOLVED)/Screenshot%20from%202021-12-11%2014-51-20.png)
Phi(n)
>1280 678415 822214 057864 524798 453297 819181 234364 596418 349127 352680 639289 550089 776560

### Menggunakan Python untuk mencari Phi(n) sekaligus mencari flagnya
Kode program:
```
#Diketahui:

#ciper text/text yang tersandi

c= 62324783949134119159408816513334912534343517300880137691662780895409992760262021

#n

n= 1280678415822214057864524798453297819181910621573945477544758171055968245116423923

#e

e= 65537

  

#Faktorisasi pertama dari n adalah:

prime_n= [1899107986527483535344517113948531328331, 674357869540600933870145899564746495319033]

#start value dari Phi(n)

phi_n= 1

#Dijawab:

#Rumus:

phi_n_hasil = (prime_n[0]-1)*(prime_n[1]-1)

#hasil :Phi(n)/Euler's totient = 1280678415822214057864524798453297819181234364596418349127352680639289550089776560

print()

d=pow(e,-1, phi_n_hasil)#=(e^-1)%phi_n_hasil

ans=pow(c,d,n)#=(c^d)%n

print(bytes.fromhex(hex(ans)[2:]).decode('ascii'))#convert hex ke ascii

```
Jalankan lalu akan ketemu flagnya
## Flag
picoCTF{sma11_N_n0_g0od_.......}
## Referensi
https://ctftime.org/writeup/26977
https://ctftime.org/writeup/26977
https://www.pythonindo.com/tag/fungsi-pow-di-python/

