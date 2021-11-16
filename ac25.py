def minmax(array):
    array.sort()
    result=[array[0],array[-1]]
    return result
arr=[4,2,8,4,7,9,5,12,-1]
print(minmax(arr))