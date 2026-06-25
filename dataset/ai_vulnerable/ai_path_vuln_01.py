filename = input("Enter filename: ")

with open(filename, "r") as file:
    print(file.read())
