user_file = input("File: ")

with open("storage/" + user_file, "r") as f:
    print(f.read())
