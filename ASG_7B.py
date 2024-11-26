def fibo_s(a,b,n):
    if n > 0 :
        print(a,end=" ")
        fibo_s(b,a+b,n-1)
n = int(input("Enter the number of term : "))
print(f"The 1st {n} term of the fibonacci series are :")
fibo_s(0,1,n)
