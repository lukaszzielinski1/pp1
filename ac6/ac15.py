arr=['green','yellow','red','black','white']
f=open('colors.txt','w')
for x in range(len(arr)):
    f.write(arr[x])
    f.write('\n')
f.close()
y=open('colors.txt','r')
print(y.read())