x=int(input("Enter number: "))
sume=x
quantity=0
while x!=0:
    x=int(input("Enter number: "))
    sume+=x
    quantity+=1
    if x==0:
        print(f"RESULT: Quantity={quantity}, Sum={sume}, Mean={sume/quantity}")