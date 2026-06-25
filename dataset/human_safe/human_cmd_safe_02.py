import subprocess

filename = "notes.txt"

subprocess.run(["cat", filename], check=True)
