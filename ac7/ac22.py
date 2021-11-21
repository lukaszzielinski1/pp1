f=open("power.txt","w")
for x in range(1,11):
    f.write(f"{str(x)},{str(x**2)},{str(x**3)}""\n")
f.close()