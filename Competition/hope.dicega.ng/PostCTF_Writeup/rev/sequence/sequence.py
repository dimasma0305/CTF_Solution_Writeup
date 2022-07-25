a = 12
print(a, end=' ')

for i in range(1, 6):
    a = (3*a+7)%16
    print(a, end=' ')
    
# reference: https://sechack.tistory.com/85