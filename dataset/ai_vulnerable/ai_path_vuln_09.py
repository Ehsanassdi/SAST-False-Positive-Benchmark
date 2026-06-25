filename = input("Enter filename: ")

path = "./files/" + filename

with open(path, "r") as file:
    print(file.read())
