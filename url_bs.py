import urllib2
import sys
from bs4 import BeautifulSoup

# python2 install BeautifulSoup by python2
# HTML parser : Get Title
# Using bs4
try:
    url = str(raw_input("Input URL: "))
    response = urllib2.urlopen(url)
    soup = BeautifulSoup(response.read(),"html.parser")
    response.close()
    print soup.title.string
except ValueError:
    print "Value Error, check URL(:3"
