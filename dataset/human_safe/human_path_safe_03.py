import os

base_dir = "uploads"
filename = "image.png"

safe_path = os.path.join(base_dir, filename)
print(safe_path)
