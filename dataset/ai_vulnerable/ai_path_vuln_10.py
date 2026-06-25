import os

filename = input("Filename: ")

filepath = os.path.join("storage", filename)

with open(filepath) as file:
    print(file.read())
