# Leviathan Level 0
```sh
ssh leviathan0@leviathan.labs.overthewire.org -p 2223
# password: leviathan0
cd .backup/
cat bookmarks.html | grep password
# nextpass: rioGegei8m
```
# Leviathan Level 0 → Level 1
```sh
ssh leviathan1@leviathan.labs.overthewire.org -p 2223
# password: rioGegei8m
ls -a
ltrace ./check
# checkpass: sex
./check
# checkpass
cat /etc/leviathan_pass/leviathan2
# nextpass: ougahZi8Ta
```
# Leviathan Level 1 → Level 2
```sh
ssh leviathan2@leviathan.labs.overthewire.org -p 2223
# password: ougahZi8Ta
ltrace ./printfile /etc/leviathan_pass/leviathan3
gdb printfile
```
in gdb
```
b *main+101
r /etc/leviathan_pass/leviathan3
ni
i r
```
- explanation: https://securitytimes.wordpress.com/2017/07/18/leviathan2-3/
or
```sh
ltrace ~/printfile test\ file
```
- explanation: https://blvckb3vrd.wordpress.com/2015/12/11/overthewire-leviathan-level-2/
```sh
mkdir /tmp/mypassfor3/ && ln -s /etc/leviathan_pass/leviathan3 /tmp/mypassfor3/test
ln -s /etc/leviathan_pass/leviathan3 /tmp/mypassfor3/test
touch /tmp/mypassfor3/file\ test
cd /tmp/mypassfor3/
~/printfile test\ file
# Nestpass: Ahdiemoo1j
```
# Leviathan Level 2 → Level 3
```sh
ssh leviathan3@leviathan.labs.overthewire.org -p 2223
# Password: Ahdiemoo1j
ltrace ./level3
# The function `strcmp` compares _test_ with _snlprintf_ means the password is _snlprintf_.
./level3 
# the password
/bin/bash
cat /etc/leviathan_pass/leviathan4
# Nextpass: vuH0coox6m
```
# Leviathan Level 3 → Level 4
```sh
ssh leviathan4@leviathan.labs.overthewire.org -p 2223
# Password: vuH0coox6m
cd .trash
./bin
# Convert to ascii https://www.rapidtables.com/convert/number/binary-to-ascii.html
# Nextpass: Tith4cokei
```
# Leviathan Level 4 → Level 5
```sh
ssh leviathan5@leviathan.labs.overthewire.org -p 2223
# Password: Tith4cokei
ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log
./leviathan5
# Nextpass: UgaoFee4li
```
- explain: https://programmercave0.github.io/blog/2020/01/06/Leviathan-Level-5-to-6-Basic-Exploitation-Techniques
# Leviathan Level 5 → Level 6
```sh
ssh leviathan6@leviathan.labs.overthewire.org -p 2223
# Passowrd: UgaoFee4li
```
program
```sh
for i in {0001..9999}
do
    echo $i
    ./leviathan6 $i
done
```

```sh
cat /etc/leviathan_pass/leviathan7
# Nextpass: ahy7MaeBo9
```
# Leviathan Level 6 → Level 7
```sh
ssh leviathan7@leviathan.labs.overthewire.org -p 2223
# Password: ahy7MaeBo9

```