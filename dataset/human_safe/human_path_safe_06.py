import os

base_dir = "downloads"
filename = "manual.pdf"

safe_path = os.path.join(base_dir, filename)
print(safe_path)
