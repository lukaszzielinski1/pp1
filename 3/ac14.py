arr=["Genowefa","Onufry","Celestyna","Alojzy","Pankracy"]
max=len(arr[0])
for x in range(len(arr)):
    if len(arr[x])>int(max):
        max=len(arr[x])
        imie=arr[x]
print(f'longest name = {imie}')
