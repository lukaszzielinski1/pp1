arr=[2,3,2,5,8,1,9,8]
for x in range(len(arr)):
    z=arr.count(arr[x])
    if z<=1:
        print(arr[x],end=' ')