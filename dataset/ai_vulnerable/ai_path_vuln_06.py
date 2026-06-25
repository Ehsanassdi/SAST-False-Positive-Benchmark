import os

name = input("Filename: ")

filepath = os.path.join("/tmp", name)

with open(filepath) as file:
    print(file.read())
