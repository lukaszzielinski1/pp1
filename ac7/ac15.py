f=open("countries.txt","r")
count=0
for line in f:
    count+=1
print(f"""File name: {f.name}
Number of lines:{count}""")
f.close()