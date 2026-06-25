import subprocess

folder_path = "dataset"

subprocess.run(["find", folder_path, "-type", "f"], check=True)
