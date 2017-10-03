import urllib2
import sys
import re

# HTML parser : Get Title
# Using regexp
try:
    url = str(raw_input("Input URL: "))
    response = urllib2.urlopen(url)
    html = response.read()
    response.close()
    pattern = "(?<=<title>)(.*)(?=</title>)"
    print(re.compile(pattern).search(html).group(0))
except ValueError:
    print "Value Error, check URL(:3"


