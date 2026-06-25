import os

base_directory = "downloads"
file_name = "setup.exe"

safe_path = os.path.join(base_directory, file_name)

print(safe_path)
