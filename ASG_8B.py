import numpy
import random

a= []
b= []

m = int(input("Row = "))
n = int(input("Colom = "))

for i in range(m):
    tem = []
    for j in range(n):
        tem.append(int(input()))
    a.append(tem)

for i in range(n):
    tem = []
    for j in range(m):
        tem.append(random.randint(1,20))
    b.append(tem)

print("A= ",a)
print("B= ",b)
print("A * B =",numpy.dot(a,b))