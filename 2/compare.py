def compare(array1,array2):
    if len(array1)==len(array2):
        for x in range(len(array1)-1):
            if array1[x]!=array2[x]:
                return False
            return True
    else:
        return False

print(f"""a) ["water","book","sky"],["water","book","sky"] : {compare(["water","book","sky"],["water","book","sky"])}""")
print(f"""b)[True,False],[True,False,True] " {compare([True,False],[True, False, True])}""")