import random
import string

password_length = int(input("Enter password length: "))
x = int(input("1. letter\n2. number\n3. symbol::\n"))
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
number = "0123456789"
symbol = "!@#$%^&*~+-*/?"
password = ""

match x :
    case 1:
        for _ in range(password_length):
            c = random.choice(letter)
            password += c
    case 2:
        for _ in range(password_length):
            c = random.choice(number)
            password += c
    case 3:
        for _ in range(password_length):
            c = random.choice(symbol)
            password += c


print("Generated password: ", password)