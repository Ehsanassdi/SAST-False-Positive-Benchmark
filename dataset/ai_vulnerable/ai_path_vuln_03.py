import os

filename = input("Enter file: ")

path = os.path.join("documents", filename)

with open(path, "r") as file:
    print(file.read())
