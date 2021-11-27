arr=[6,8,3,1,0,5,7]
count=0
n=int(input("enter the number: "))
for x in arr:
    if n<x:
        count+=1
print(count)