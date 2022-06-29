flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰㑣〷㘰摽"
for i in range(len(flag)):
    print(chr(ord(flag[i])>>8),end="")
    print(chr((ord(flag[i]))-((ord(flag[i])>>8)<<8)),end="")

print("\n")