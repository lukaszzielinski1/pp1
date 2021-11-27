arr=[1,23,5,382,1,17,4,906]
z='|'
for x in arr:
    z+=" "*(4-len(str(x)))+str(x)+'|'
print('-'*len(z))
print(z)
print('-'*len(z))