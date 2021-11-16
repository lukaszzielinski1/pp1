arr1=[2,5,6,8]
arr2=[1,2,5,6,7,8]
z=0
for x in arr1:
    if x in arr2:
        z+=1
        if z==len(arr1):
            print(True)
if z!=len(arr1):
    print(False)