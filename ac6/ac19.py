arr=[2,3,2,5,8,1,9,8]
arr2=[]
arr3=[]
for x in arr:
    if x not in arr2:
        arr2.append(x)
    elif x in arr2:
        arr3.append(x)
for z in arr:
    if z not in arr3:
        print(z,end=' ')