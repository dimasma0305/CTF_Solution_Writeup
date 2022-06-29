from contextlib import suppress
huruf = 'RFTCrt5{w_yp0c_r_ht1s1_3sr3v3r_43_ys}thg1r_'
for a in range(0,len(huruf),5):
    with suppress(Exception):
        print(huruf[a+3], end="")
    with suppress(Exception):
        print(huruf[a+2], end="")
    with suppress(Exception):
        print(huruf[a], end="")
    with suppress(Exception):
        print(huruf[a+1], end="")
    with suppress(Exception):
        print(huruf[a+7], end="")

print