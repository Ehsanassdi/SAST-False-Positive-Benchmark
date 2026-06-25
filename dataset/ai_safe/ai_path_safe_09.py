import os

directory = "reports"
file_name = "summary.txt"

print(os.path.normpath(os.path.join(directory, file_name)))
