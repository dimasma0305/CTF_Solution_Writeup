s='ocip{FTC0l_I4_t5m_ll0m_y_y3n4cdbae52ÿ}'
from contextlib import suppress
print()
for x in range(0,len(s),4):
    with suppress(Exception):
        print(s[x+3],end="")
    with suppress(Exception):
        print(s[x+2],end="")
    with suppress(Exception):
        print(s[x+1],end="")
    with suppress(Exception):
        print(s[x],end="")

print("\n")