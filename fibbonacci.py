n = int(input("Enter number :- "))
pre = 0
post = 1
temp = 1
l = []
for i in range(1,n+1):
    if(i == 1):
        l.append(0)
    else:
        l.append(temp)
        temp = pre + post
        pre = post
        post = temp
print(l)