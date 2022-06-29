# Wireshark twoo twooo two twoo...
#### Description

Can you find the flag? [shark2.pcapng](https://mercury.picoctf.net/static/a7b4ce62a4f4313a6e5b0b03b97be953/shark2.pcapng).
## Hints
- Did you really find _the_ flag?
- Look for traffic that seems suspicious.
## Solving
```sh
tshark -nr shark2.pcapng -Y 'dns && ip.src == 192.168.38.104 && frame contains "local" && ip.dst==18.217.1.57' | awk '{ print $12 }' | awk -F. '{ print $1 }' | tr -d "\n"|base64 -d
```
## Flag

## Referensi
https://github.com/Dvd848/CTFs/blob/master/2021_picoCTF/Wireshark_twoo_twooo_two_twoo.md