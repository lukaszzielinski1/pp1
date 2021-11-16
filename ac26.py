arr=[4,7,8,2,5,9]
z=[]
y=[]
for x in range(len(arr)):
    if arr[x]%2==0:
        z=arr[x]
        print(z,end=' ')
for x in range(len(arr)):
    if arr[x]%2==1:
        y=arr[x]
        print(y,end=' ')