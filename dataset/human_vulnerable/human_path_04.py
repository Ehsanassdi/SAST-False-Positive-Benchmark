logfile = input("Log file: ")

path = "logs/" + logfile

with open(path, "r") as f:
    print(f.read())
