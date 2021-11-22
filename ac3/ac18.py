amount=int(input("Enter any amount: "))
piec=amount//5
dwa=(amount-(piec*5))//2
jeden=(amount-(piec*5)-(dwa*2))//1
print(f"""The amount of PLN {amount} in coins:
5 zł - {piec}
2 zł - {dwa}
1 zł - {jeden}""")