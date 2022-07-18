file1 = open('/home/wowon/Downloads/apple.txt', 'r')
file1 = file1.read()
file2 = open('/home/wowon/Downloads/coconut.txt', 'r')
file2 = file2.read()
print(len(file2))
for i in range(len(file1)):
    if file1[i] != file2[i]:
        print(file1[i],end='')
    elif file1[i] == file2[i]:
        print('',end='')