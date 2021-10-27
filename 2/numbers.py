def numbers():
    for x in range(1,8,+3):
        for y in range(0,3):
            print(f"{x+y}",end=' ')
        print()
numbers()