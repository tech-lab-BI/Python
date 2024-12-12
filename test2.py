n = 7
a = []
for i in range(n):
    print(">>>>>>>>>>i = ",i,"<<<<<<<<<<<<")
    l1=[]
    p=0
    for j in range(i):
        # print(j)
        l1.append(j)
    print("      l1 : ",l1)
    for k in l1:
        p += 1
        a.append(p)
    print("      a = ",a)
k = 0
print("final a = ",a)
for l in a:
    k += 1
    print(k)