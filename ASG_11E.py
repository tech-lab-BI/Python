import os
def get_file_size(filename):
    try:
        size = os.path.getsize(filename)
        print(f"The size of '{filename}' is {size} bytes.")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error ocurred: {e}.")
filename = input("Enter the name of the file (wwith extension): ")
get_file_size(filename)