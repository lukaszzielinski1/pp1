f=open("grades.txt","r")
import re
y=re.findall("\d.\d",f.read())
suma=0
for x in range(len(y)):
    z=y[x]
    suma+=float(z)
print(round(suma/len(y),2))