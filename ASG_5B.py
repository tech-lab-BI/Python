st = input("Enter email id : ")

roll,col = st.split("@")

domain = col.split(".")

#print(type(roll))

print(roll,domain[0].upper())