# RSA
RSA di bidang kriptografi adalah sebuah algoritme pada enkripsi public key. RSA merupakan algoritme pertama yang cocok untuk digital signature seperti halnya enkripsi, dan salah satu yang paling maju dalam bidang kriptografi public key. RSA masih digunakan secara luas dalam protokol electronic commerce, dan dipercaya dalam mengamankan dengan menggunakan kunci yang cukup panjang.

## RSA Algorithm Example

-   Choose p = 3 and q = 11
-   Compute n = p * q = 3 * 11 = 33
-   Compute φ(n) = (p - 1) * (q - 1) = 2 * 10 = 20
-   Choose e such that 1 < e < φ(n) and e and φ (n) are coprime. Let e = 7
-   Compute a value for d such that (d * e) % φ(n) = 1. One solution is 
```
d = 3 [(3 * 7) % 20 = 1]
```

-   Public key is (e, n) => (7, 33)
-   Private key is (d, n) => (3, 33)
-   The encryption of _m = 2_ is _c = 27 % 33 = 29_
-   The decryption of _c = 29_ is _m = 293 % 33 = 2_