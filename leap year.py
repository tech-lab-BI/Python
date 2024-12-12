carry=0
year=int(input("Enter year:"))
if(year%400==0):
    carry=1
elif(year%100==0):
    pass
elif(year%4==0):
    carry=1
if(carry==1):
    print(year,"is leap year.")
else:
    print(year,"is not leap year.")