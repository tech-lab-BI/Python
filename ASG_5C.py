st = input("Enter a string : ")
uc = 0
lc = 0
for c in st :
    if c.isupper():
        uc += 1
    elif c.islower():
        lc += 1
print(uc," ",lc)