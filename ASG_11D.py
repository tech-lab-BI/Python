def read_and_display_file(filename):
    try:
        with open(filename,"r") as file:
            lines = file.readlines()
            print("Contents of file:")
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occured:{e}")
filename = input("Enter the name of the text file to read (with extension): ")
read_and_display_file(filename)