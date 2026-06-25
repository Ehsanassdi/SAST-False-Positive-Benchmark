import os

base_dir = "exports"
filename = "results.csv"

safe_path = os.path.normpath(os.path.join(base_dir, filename))
print(safe_path)
