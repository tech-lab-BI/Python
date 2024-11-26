val = input("Enter a lists ::  ").split()
l1 = [int(v) for v in val]

final_list = [0] * (max(l1) + 1)

for num in l1:
    final_list[num] = num

print(final_list)