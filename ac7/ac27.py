f=open("countries.txt","r")
import re
y=re.findall("\w\w\w\w\w\w+",f.read())
for x in y:
    print(x)
f.close()