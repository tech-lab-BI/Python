def prime_check(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
prime_list = tuple(filter(prime_check,range(5500,250,-1)))
print(f"All prime number between 251 to 5500 are : {prime_list}")