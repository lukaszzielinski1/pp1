x=int(input("Podaj x:"))
y=int(input("Podaj y:"))
if x>0 and y>0:
    print(f"Punkt P({x},{y}) znajduje sie w pierwszej cwiartce ukladu.")
if x<0 and y>0:
    print(f"Punkt P({x},{y}) znajduje sie w drugiej cwiartce ukladu.")
if x>0 and y<0:
    print(f"Punkt P({x},{y}) znajduje sie w czwartej cwiartce ukladu.")
if x<0 and y<0:
    print(f"Punkt P({x},{y}) znajduje sie w trzeciej cwiartce ukladu.")
if x==0 and y != 0:
    print(f"Punkt P({x},{y}) znajduje sie na osi x.")
if x != 0 and y==0:
    print(f"Punkt P({x},{y}) znajduje sie na osi y.")
if x==0 and y==0:
    print(f"Punkt P({x},{y}) znajduje sie w pozycji (0,0).")