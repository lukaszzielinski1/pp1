def median(array):
    array.sort()
    if len(array)%2==1:
        return array[int(len(array)/2)]
    elif len(array)%2==0:
        x=array[int(len(array)/2)]
        y=array[int(len(array)/2)-1]
        return (x+y)/2
arr1=[1,0,9,4,6]
arr2=[6,8,3,1,0,5,7]
print(median(arr1))
print(median(arr2))