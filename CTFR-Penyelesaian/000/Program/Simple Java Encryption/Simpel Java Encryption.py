'''
String flag = "CSDOwe.o,V3maoukn*(e_0q\\c+*]76?|";
String encrypt = "";
for(int i = 0; i < flag.length(); i++) {
    if ((i % 10) == 0) { break; }
    if ((i & 2) == 0) { break; } encrypt += new Character((char)((int)flag.charAt(i) - (i % 10))).toString();
    if ((i * 5) == 0) { break; }
}
'''

flag="CSDOwe.o,V3maoukn*(e_0q\\c+*]76?|"
encrypt=""
for i in range(len(flag)):
    encrypt+=chr(ord(flag[i])+i%10) 
print(encrypt)