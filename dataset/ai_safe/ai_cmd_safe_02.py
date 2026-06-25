import subprocess

file_name = "notes.txt"

subprocess.run(["cat", file_name], check=True)
