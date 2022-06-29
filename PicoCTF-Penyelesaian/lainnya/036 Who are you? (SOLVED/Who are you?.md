# Who are you?l
#### Description

Let me in. Let me iiiiiiinnnnnnnnnnnnnnnnnnnn [http://mercury.picoctf.net:1270/](http://mercury.picoctf.net:1270/) 
## Hints
It ain't much, but it's an RFC [https://tools.ietf.org/html/rfc2616](https://tools.ietf.org/html/rfc2616)
## Solving
### Only people who use the official PicoBrowser are allowed on this site!
```
User-Agent: PicoBrowser
```
### I don't trust users visiting from another site.
```
Referer: http://mercury.picoctf.net:1270/
```
### I don't trust users who can be tracked.
```
DNT: 1
```
### Sorry, this site only worked in 2018.
```
Date: Wed, 21 Oct 2018 07:28:00 GMT
```
### This website is only for people from Sweden.
```
X-Forwarded-For: 31.3.152.55
```
### You're in Sweden but you don't speak Swedish?
```
Accept-Language: sv,en;q=0.9
```


## Flag
picoCTF{http_h34d3rs_v3ry_c0Ol_much_...........
## Referensi
