import os

filename = input("Enter filename: ")

path = "uploads/" + filename

with open(path, "r") as file:
    print(file.read())
