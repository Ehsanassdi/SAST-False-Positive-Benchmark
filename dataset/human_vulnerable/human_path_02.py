file_name = input("File: ")

path = "documents/" + file_name

with open(path, "r") as f:
    print(f.read())
