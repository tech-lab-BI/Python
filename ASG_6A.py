val = input("Enter the number : ").split()
valInt = [int(v) for v in val]
sort_val = sorted(valInt)

print("2nd Maximun = ",sort_val[-2])
print("2nd Minimun = ",sort_val[1])


# print(valInt)
# print(val)
# print(sort_val)
