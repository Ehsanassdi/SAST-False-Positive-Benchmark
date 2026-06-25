filename = input("Enter filename: ")

with open("files/" + filename, "r") as f:
    print(f.read())
