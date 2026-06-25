import os

path = input("Path: ")

with open(os.path.normpath(path), "r") as file:
    print(file.read())
