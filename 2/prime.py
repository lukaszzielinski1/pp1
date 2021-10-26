N=int(input("how many?: "))
for x in range(2,N+1):
    if x%1==0 and x%x==0:
        print(f"Prime numbers:"" {x}", end=' ')