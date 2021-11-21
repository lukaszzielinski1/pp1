f=open("countries.txt","r")
e=open("copylines.txt","w")
for x in f:
    e.write(x)
    y=f.readline()
    e.write(y)
e.close()
f.close()