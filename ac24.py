z=int(input("enter a number: "))
y=0
arr=[1,66,24,2,56,11,26,84,77,89,21]
for x in range(len(arr)):
    if z<arr[x]:
        y+=1
print(y)