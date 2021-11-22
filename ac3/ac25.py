a=int(input("Enter a: "))
b=int(input("Enter b: "))
for x in range(a):
    for y in range(b):
        if x==0 or x==a-1 or y==0 or y==b-1:
            print("*",end='')
        elif y!=0 or y!=b-1:
            print(end=" ")
    print()