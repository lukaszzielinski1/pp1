human=int(input("Enter the dog's age in human years: "))
if human<=2:
    dog=10.5*human
else:
    dog=21+(human-2)*4
print(f"The dog's age in dog years is {dog} years.")