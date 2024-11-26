def is_prime(x):
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def is_palindrome(s):
    st = s[::-1]
    if s == st:
        return True
    else:
        return False
