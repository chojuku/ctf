s1 = "Gur svefg cneg bs gur synt vf: pgs4o{a0zber"
s2 = "Lzw kwugfv hsjl gx lzw xdsy ak: _uDskk!usd_u"
s3 = "Rypt0graphy}"

def add(c, n):
    oc = ord(c)
    if oc >= 65 and oc <= 90:
        return chr((ord(c)-65+n) % 26 + 65)
    elif oc >=97 and oc <= 122:
        return chr((ord(c)-97+n) % 26 + 97)
    else :
        return c

for i in range(26):
    l = list(s3)
    print ("".join(map(lambda x: add(x, i), l)))
