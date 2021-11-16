arr=[4,36,12,28,9,44,5]
arr2=[5,1,36]
for x in range(len(arr)):
    if arr[x] not in arr2:
        print(arr[x],end=' ')