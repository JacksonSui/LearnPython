import re
f=open('1.txt','r')
for line in f:
    a=re.findall('\d+',line)
    print a
