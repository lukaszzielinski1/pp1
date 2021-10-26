PIN=int(2115)
first=int(input("Enter the PIN code:"))
if first == PIN:
    print("Correct.")
else:
    print("Incorrect...")
    second=int(input("Enter the PIN code:"))
    if second == PIN:
        print("Correct.")
    else:
        print("Incorrect...")
        third=int(input("Enter the PIN code:"))
        if third==PIN:
            print("Correct.")
        else:
            print("Incorrect...")
            print("Sorry, your payment card has been blocked.")