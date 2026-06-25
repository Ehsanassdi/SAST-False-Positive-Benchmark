import subprocess

folder = "dataset"

subprocess.run(["find", folder, "-type", "f"], check=True)
