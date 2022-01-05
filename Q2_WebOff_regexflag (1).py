#homepage regex flag - final version
import requests, re

url = 'http://10.12.0.30/index.php'
requests.session()
resp = requests.get(url)
r = "\{\w{32}\}"
flag = re.findall(r,resp.text)
print(flag)