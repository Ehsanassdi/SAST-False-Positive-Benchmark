user_file = input("File name: ")

with open(user_file) as file:
    print(file.read())
