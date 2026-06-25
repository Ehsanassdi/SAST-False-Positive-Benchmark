image = input("Image name: ")

with open("images/" + image, "rb") as f:
    data = f.read()
