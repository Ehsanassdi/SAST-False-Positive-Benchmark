template = input("Template: ")

with open("templates/" + template, "r") as f:
    print(f.read())
