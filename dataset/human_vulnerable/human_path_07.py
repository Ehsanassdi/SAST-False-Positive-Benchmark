document = input("Document: ")

path = "uploads/" + document

with open(path, "r") as f:
    print(f.read())
