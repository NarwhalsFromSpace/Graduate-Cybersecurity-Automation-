#xor challenge

import base64, codecs
def xorcrypt(plain,key):
    c = ""
    for i in range(len(plain)):
        c1 = plain[i]
        c2 = key[i%len(key)]
        c += chr(ord(c1)^(ord(c2)))
    return c
# with open('xor_challenge.txt', 'rb') as f:
#   contents = f.read()
# contents = (contents).encode('latin1').decode('utf8')
# contents.decode('unicode_escape')
f = codecs.open('xor_challenge.txt', "r", "utf-16")
encrypted = base64.b64decode(f).decode("UTF-8")
i = "CNS"
# i = 'żՄƠ䑊ᓷ½ħą'
rslt = xorcrypt(encrypted, i)
print(rslt)

import chardet
# with open('xor_challenge.txt', 'rb') as f:
#   contents = f.read()
chardet.detect(xL/UirHHs5Pkl+SQsZfhkrSXsZOyw7OV5pXkxbSS5cW+k7fJ+g==)

import codecs
with open('xor_challenge.txt', 'rb') as f:
  contents = f.read()
# contents.decode('unicode_escape')
# contents.decode('ascii')
unicode_string=codecs.decode(contents, 'utf-8')
print(unicode_string)

import codecs
with codecs.open('xor_challenge.txt', 'r', encoding='ascii',errors='ignore') as fdata:
    contents = fdata.read()