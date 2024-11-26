st = input("Enter the string : ")

inp = input("Enter the position to slice :")
index = inp.split(" ")
# print(index)

slice = st[(int(index[0]) - 1):int(index[1])]

if slice == slice[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

# print(slice)