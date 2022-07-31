#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

config = {
    'API_KEY' : "212817d980b9a03add91e5814d02"
}

class API(object):
    def __init__(self, apikey):
        self.apikey = apikey

    def renderHTML(self, templateHTML, title, text):
        return (templateHTML.format(self=self, title=title, text=text))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage : python3 "+sys.argv[0]+" TEMPLATE CONTENT")
    else :
        a = API(config['API_KEY'])
        print(a.renderHTML(sys.argv[1], "Vuln web render App", sys.argv[2]))