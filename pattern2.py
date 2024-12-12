row=int(input("How many row u want:"))
for i in range(1,2*row):
    if i < row:
        print("* " * i)
    elif i == row :
        print("* " * (2*row - 1))
    else:
        print("  " * (i-1),end="")
        print("* " * (2*row - i))
