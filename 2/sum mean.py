L=0
sum=0
mean=0
for x in range(100):
    L=int(input("podaj licbze: "))
    sum += L
    mean += L
    if L==0:
        print(f"RESULTS: Quantity={x}, Sum={sum}, Mean={mean/x}")
        break