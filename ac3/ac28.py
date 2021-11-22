a=0
b=1
for x in range(50):
    if x<=1:
        print(x,end=' ')
    else:
        fibo=a+b
        a=b
        b=fibo
        print(fibo,end=' ')