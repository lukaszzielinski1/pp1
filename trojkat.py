a=int(input("Podaj dlugosc boku a:"))
b=int(input("Podaj dlugosc boku b:"))
c=int(input("Podaj dlugosc boku c:"))
p=(1/2)*(a+b+c)
pole=(p*(p-a)*(p-b)*(p-c))**(1/2)
print(f"Pole trojkata wynosi: {pole}")