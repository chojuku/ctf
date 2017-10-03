# -*- coding: utf-8 -*-

import base64, uu

f = open('onion','r')
text = f.read()
str = text.replace('\n','')

for _ in range(0,16):
    str = base64.b64decode(str) 
    print str
print str.decode("uu")
f.close()
