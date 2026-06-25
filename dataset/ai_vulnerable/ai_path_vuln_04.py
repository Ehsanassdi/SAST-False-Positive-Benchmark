directory = input("Directory: ")

with open(directory + "/config.txt", "r") as file:
    print(file.read())
