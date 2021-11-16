def median(array):
    array.sort()
    x=array[int(len(array)/2)]
    if len(array)%2==1:
        return x
    elif len(array)%2==0:
        return (x+(x+1))/2
arr1=[1,0,9,4,6]
arr2=[6,8,3,1,0,5,7]
print(median(arr1))
print(median(arr2))