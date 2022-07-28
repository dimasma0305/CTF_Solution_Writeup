import os

from werkzeug.urls import url_fix

name = "..\ asd"
name = url_fix(name)
print(name)

# with open(name, "w") as f:
#         f.write("asd")
        
# # remove file
# os.remove(name)