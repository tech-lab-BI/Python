file_name = "Welcome.txt"
with open(file_name,"w") as file:
    file.write("Welcome to python")
print(f"Welcome to python has been written to {file_name}")