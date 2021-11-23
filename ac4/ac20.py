def power(x,n):
    if x==0:
        return 0
    if n==0:
        return 1
    if n==1:
        return x
    if x==1:
        return 1
    if n>1 and x>1:
        return x**n
print(power(5,3))