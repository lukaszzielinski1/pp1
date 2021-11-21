f=open("countries.txt","r")
count=0
for line in f:
    count+=1
    print(line)
    if count%5==0:
        input("Press Enter to continue...")
        print()