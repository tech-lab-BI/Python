l = []
for i in range(10,100):
    length = len(str(i))
    if i == (i**2 % 10**length):
        l.append(i)
print(l)