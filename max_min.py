a=int(input("Enter 1st number:"))
b=int(input("Enter 2st number:"))
c=int(input("Enter 3st number:"))
if(a>b):
    if(b>c):
        maxi=a
        mini=c
    else:
        if(a>c):
            maxi=a
            mini=b
        else:
            maxi=c
            mini=b
else:
    if(b<c):
        maxi=c
        mini=a
    else:
        if(a>c):
            maxi=b
            mini=c
        else:
            maxi=b
            mini=a
#print(max(a,b,c),min(a, b, c))
print(maxi,mini)