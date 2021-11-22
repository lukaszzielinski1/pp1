pin=int("0805")
x=int(input("Enter the PIN code: "))
if x==pin:
    print("Correct.")
else:
    print("Incorrect...")
    y=int(input("Enter the PIN code: "))
    if y==pin:
        print("Correct.")
    else:
        print("Incorrect...")
        z=int(input("Enter the PIN code: "))
        if z==pin:
            print("Correct.")
        else:
            print("Incorrect...")
            print("Sorry, your payment card has been blocked.")