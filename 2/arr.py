test=[-15,8,-31,47,-2,19]
min=test[0]
max=test[0]
for i in test:
    if i>max:
        max=i
    if i<min:
        min=i
print(f"max:{max}, Min:{min}")