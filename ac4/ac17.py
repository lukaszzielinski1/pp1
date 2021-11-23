def calculations(n):
    txt='You never get a second chance to make a first impression'
    count=0
    for x in txt:
        if x==n:
            count+=1
    return count
print(calculations('e'))