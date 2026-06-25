folder = input("Folder: ")
filename = input("Filename: ")

with open(folder + "/" + filename) as file:
    print(file.read())
