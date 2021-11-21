import random
f=open("random.txt","w")
for x in range(50):
    f.write(f"{str(random.randint(100,999))}""\n")
f.close()