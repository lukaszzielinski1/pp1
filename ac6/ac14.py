arr=['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
maxlen=arr[0]
for x in range(len(arr)):
    if len(arr[x]) > len(maxlen):
        maxlen=arr[x]
print(maxlen)