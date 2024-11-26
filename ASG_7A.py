def fibo_n(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo_n(n-1) + fibo_n(n-2)
n = int(input("Enter the number of term : "))
print(f"The {n}th term of the fibboacci series is : {fibo_n(n)}")
