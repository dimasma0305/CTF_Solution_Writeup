>Link Download Reversing1 https://drive.google.com/file/d/0B73v7q0VGLSERWNjbmpXUFo5Z3c

# Reversing1
Kita akan menggunakan aplikasi Ghidra untuk mereversing aplikasi "reversing1" ini. Gas kita buka ghidranya....

Di ghidra kita akan menuju *function* "main" seperti dibawah ini

![](Pasted%20image%2020220326055855.png)

Main
```c
undefined8 main(void)

{
  int iVar1;
  long in_FS_OFFSET;
  undefined4 local_14;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  printf("Masukkan PIN yang benar: ");
  __isoc99_scanf(&DAT_0040075e,&local_14); // << Berfungsi untuk mengambil input dari user
  iVar1 = cek_pin(local_14); // << cek_pin()
  if (iVar1 == 0) {
    puts("PIN salah!\n");
  }
  else {
    puts("PIN benar!\n");
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```
bisa dilihat pada fungsi "cek_pin" kita tidak tahu fungsi itu digunakan untuk apa, tapi bisa diasumsikan bahwa fungsi "cek_pin" memberikan output berupa *boolean* karena fungsi "if" dibawahnya menggunakan "0"(false) sebagai pernyataan.

Sekarang coba kita intip ke fungsi "cek_pin" dengan mengekliknya 2x

![](Pasted%20image%2020220326061338.png)

cek_pin
```c
bool cek_pin(int param_1) // << funsi bertipe boolean

{
  return param_1 == valid_pin;
}
```

Ternyata pernyataan kita diatas benar, bahwa fungsi "cek_pin" bertipe boolean. Kita lihat ke bagian "param_1" bisa dilihat disana bahwa "param_1" memiliki tipe "int" yang berarti fungsi ini "param_1 == valid_pin;" , di bagian "valid_pin" juga merupakan "int"

Gas kita klik 2x variabel "valid_pin" untuk mendapatkan pinnya...

![](Pasted%20image%2020220326062456.png)

Melihat ke "004C7F9h" (value dari variabel "valid_pin") ini merupakan tipe data hex, kita harus merubahnya ke tipe data "int"/integer
> note: kita merubahnya ke tipe datanya ke integer karena "param_1 == valid_pin;" , kedua variabel harus bertipe sama

Saya merubah hex ke decimal menggunakan website https://www.rapidtables.com/convert/number/hex-to-decimal.html

![](Pasted%20image%2020220326063305.png)

Bomm... kita mendapatkan pinnya "313337", lalu kita masukkan ke programnya

![](Pasted%20image%2020220326063553.png)