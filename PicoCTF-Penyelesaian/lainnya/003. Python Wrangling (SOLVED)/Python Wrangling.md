# Python Wrangling

Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/ende.py) using [this password](https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/pw.txt) to get [the flag](https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/flag.txt.en)?

# Hints

1.  Get the Python script accessible in your shell by entering the following command in the Terminal prompt: $ wget [https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/ende.py](https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/ende.py)
2.  $ man python

# Solving
run in terminal:
>python3 '/home/dimas/Documents/Dimas Knowledge Database/PicoCTF/Python Wrangling/ende.py' -d '/home/dimas/Documents/Dimas Knowledge Database/PicoCTF/Python Wrangling/flag.txt.en' 

open this file to see the password:
>cat '/home/dimas/Documents/Dimas Knowledge Database/PicoCTF/Python Wrangling/pw.txt' 
