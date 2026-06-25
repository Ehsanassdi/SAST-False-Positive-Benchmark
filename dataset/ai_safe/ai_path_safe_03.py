import os

base_directory = "storage"
file_name = "data.csv"

safe_path = os.path.join(base_directory, file_name)

print(safe_path)
