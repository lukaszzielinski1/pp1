def range(n,x,y):
    if n>=x and n<=y or n<=x and n>=y:
        return True
    else:
        return False
n=int(input("Enter the number: "))
x=int(input("Enter the x: "))
y=int(input("Enter the y: "))
print(range(n,x,y))