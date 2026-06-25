config = input("Config file: ")

with open("configs/" + config, "r") as f:
    print(f.read())
