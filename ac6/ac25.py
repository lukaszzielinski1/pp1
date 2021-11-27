def minmax(array):
    arr2=[]
    array.sort()
    arr2.append(array[0])
    arr2.append(array[-1])
    return arr2
arr1=[4,2,8,4,7,9,5]
print(minmax(arr1))