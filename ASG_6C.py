ip1 = input("Enter 1st string :: ").split(" ")
ip2 = input("Enter 2nd string :: ").split(" ")

s1 = { v for v in ip1}
s2 = { v for v in ip2}

st1 = s2.union(s1)
st2 = s2.intersection(s1)
st3 = s2.difference(s1)


print("1. ",st1)
print("2. ",st2)
print("3. ",st3)





# print(s1)
# print(s2)