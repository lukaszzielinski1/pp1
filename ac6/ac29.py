arr1=[4,2,8,4,7,9,5,3,12,8]
arr2=[2,9,5,7]
z=[]
for x in arr2:
    if x not in arr1:
        z.append(1)
    else:
        z.append(0)
if 1 in z:
    print(False)
if 1 not in z:
    print(True)