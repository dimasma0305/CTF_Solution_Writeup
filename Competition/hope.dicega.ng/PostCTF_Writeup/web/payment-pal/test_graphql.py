import requests

URL = "https://payment-pal.mc.ax"
COOKIE = ("session", "w4W7qtsottfWjHoT9FlMVA8bIfWEw0q7xA%3D%3D.pwAcGEg9blIDiAOsjxYFbA%3D%3D.CzvzrZFffEYdgMUiUxvyMg%3D%3D") 

class grapql_api():
    def __init__(self, query, cookie=COOKIE, url=URL, proxy=None):
        self.session = requests.Session()
        self.session.cookies.set(cookie[0], cookie[1])
        self.session.proxies = proxy
        self.session.headers.update({'Content-Type': 'application/json'})
        self.query = query
        self.url = url

    def post(self):
        url = self.url + "/graphql"
        data = self.query
        response = self.session.post(url, data=data, proxies=self.session.proxies)
        return response.json()
        
    def get(self):
        url = self.url + "/graphql"
        data = {'query': self.query}
        response = self.session.get(url, params=data)
        return response.json()
        
        

query = """
{
  "query":"mutation($username: String!, $password: String!) {   register(username: $username, password: $password) {     username   } }",
  "variables":{"username":"asdasdasd","password":"asdasdasd"}
}"""

proxys = {"http": "http://localhost:8080"}
r = grapql_api(query, proxy=proxys).post()

print(r)