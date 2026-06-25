backup = input("Backup file: ")

path = "backup/" + backup

with open(path, "r") as f:
    print(f.read())
