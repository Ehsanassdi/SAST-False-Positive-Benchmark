report = input("Report name: ")

with open("reports/" + report, "r") as f:
    print(f.read())
