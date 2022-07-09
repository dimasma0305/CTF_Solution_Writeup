
from base64 import b64decode
import urllib.parse


QUERY = "G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6OezoKpVTtluBKA%2B2078pAPR3X9UET9Bj0m9rt%2Fc0tByJk%3D"

def decode(query):
    query = urllib.parse.unquote_plus(query)
    query = b64decode(query)
    return query

def parsing_to_16_block(query):
    foo = []
    j = 0
    for i in range(16, len(query), 16):
        foo.append(query[j:i])
        j += 16
    foo2 = ''
    for i in range(len(foo)) :
        foo2 += f"Block {(i+1)}: {foo[i]}\n"
    return foo2

query = decode(QUERY)
print(query)
query = parsing_to_16_block(query)
print(query)