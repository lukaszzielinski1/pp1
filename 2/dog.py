age=int(input("Enter the dog's age in human years:"))
if age <= 2:
    pies=age*10.5
elif age > 2:
    pies=age*4-8+21

print(f"The dog's age in dog years is {pies} years.")