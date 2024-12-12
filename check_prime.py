n = int(input("Enter no :- "))
l = []
for i in range(2, n+1):  # Start the loop from 2, since 1 is not a prime number
    p = 1
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            p = 0
            break
    if p:
        l.append(i)  # Append the prime number to the list
print(l)
