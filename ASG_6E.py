# s = input("Enter a string : ")
# l = s.split()

# l.reverse()
# print(l)

# print(l[::-1])

def get_position(sub):
    return sub[-1]

s = input("Enter a string : ")
l = s.split()
# l = ['I','am',]
# print("The org. list : " + str(l))

l.sort(key = get_position)
print("Sorted : " + str(l))




