def generate_fibonacci_upto(n):
    fibonacci_numbers = []
    a,b = 0,1
    while a <= n:
        fibonacci_numbers.append(a)
        a,b = b,a + b
    return fibonacci_numbers
def write_fibonacci_to_file(filename, fibonacci_numbers):
    with open(filename,"w") as file:
        for number in fibonacci_numbers:
            file.write(str(number) + "\n")

n = int(input("Enter the upper limit (n) for Fibonacci numbers: "))
filename = "fibonacci_number.txt"
fibonacci_numbers = generate_fibonacci_upto(n)
write_fibonacci_to_file(filename,fibonacci_numbers)
print(f"Fibonacci numbers up to {n} have been written to {filename}.")