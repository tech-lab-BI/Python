import NumberCheck

n = int(input("Enter a number :"))
print(f"{n} is Prime = {NumberCheck.is_prime(n)} , Palindrome = {NumberCheck.is_palindrome(str(n))}")