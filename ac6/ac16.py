def star(n):
    return n*'*'

arr=[12,6,4,9,3]
for x in range(len(arr)):
    print(f'{arr[x]}:{star(arr[x])}')