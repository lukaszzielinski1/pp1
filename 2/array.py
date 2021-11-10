def sum(array):
    suma=0
    for i in array:
        suma=suma+i
    return suma

def array2str(array):
    result=""
    for j in array:
        result+=" " +str(j)
    return(result)

array=[4,3,7,1,3]
print(f"Array: {array2str(array)}")
print(f"Sum of values: {sum(array)}")