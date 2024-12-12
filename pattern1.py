n = int(input("No. of lines :- "))
for i in range(n):
    for j in range(n-i):#space
        print(" ",end="")
    ch = ord('A') + i   #ord for getting ascii value
    for j in range(i+1):
        print(chr(ch),end="")   #ascii value to charecter
        ch = ch - 1
    print("\n")