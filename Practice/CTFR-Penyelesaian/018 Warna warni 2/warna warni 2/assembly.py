def key():
    k=0xc
    k=k<<0xa
    k=k>>0x5
    k=k+0xa
    k=k-0xc2
    while k <= 0x190:
        k=k+1
    k=k>>0x2
    while k <= 0xff:
        k=k+1
    if k==0x100:
        k=k+1
        k=k-1
        k=k+1
        k=k-1
        k=k*0x1a
        k=k*0x368
        k=k*0x9210a4*0x9210a4*0x9210a4*0x9210a4
        return k
    else:
        return
print(key())